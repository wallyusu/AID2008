import json

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from user.models import UserProfile
import hashlib
import time  # 设置过期时间导入的包
import jwt  # 设置共享秘钥导入的包
from django.conf import settings

# Create your views here.
from django.views import View
from tools.login_dec import login_check
import random
from tools.sms import YunTongXin


class UsersView(View):
    def get(self, request, username=None):
        if username:
            # 返回单个用户信息
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                print('-get user error is %s-' % e)
                result = {'code': 10104, 'error': '该用户不存在'}
                return JsonResponse(result)
            # 根据查询字符串获取指定数据
            keys = request.GET.keys()
            if keys:
                data = {}
                for k in keys:
                    if k == 'password':
                        continue
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username, 'data': data}
            else:
                # 获取用户的全量数据
                result = {'code': 200, 'username': username,
                          'data': {'info': user.info, 'sign': user.sign, 'nickname': user.nickname,
                                   'avatar': str(user.avatar)}}
            return JsonResponse(result)
        else:
            # 返回所有用户信息
            pass
        return HttpResponse('--users get--')

    def post(self, request):
        json_str = request.body  # 获取json串
        json_obj = json.loads(json_str)  # 反序列化 将json串转换为对象
        username = json_obj['username']  # 一个个字段通过键拿值
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        print(username, email, phone, password_1, password_2)
        sms_num = json_obj['sms_num']

        # 从redis数据库中获取验证码
        cache_key = 'sms_%s' % phone
        old_code = cache.get(cache_key)
        if not old_code:
            result = {'code': 10106, 'error': '验证码错误！'}
            return JsonResponse(result)
        if int(sms_num) != old_code:
            result = {'code': 10107, 'error': '验证码错误！'}
            return JsonResponse(result)
        # 1 用户名长度检查
        if len(username) > 11:
            result = {'code': 10100, 'error': '用户名太长'}
            return JsonResponse(result)  # JsonResponse 会自动返回为json串
        # 2 检查用户名是否可用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10101, 'error': '用户名已被占用'}
            return JsonResponse(result)
        # 3 两次密码要一致
        if password_1 != password_2:
            result = {'code0': 10102, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # 4 hash处理
        md5 = hashlib.md5()
        md5.update(password_1.encode())  # 添加欲hash的内容，类型为 bytes
        password_h = md5.hexdigest()  # 返回摘要，作为十六进制数据字符串值
        # 5 添加到数据库
        try:  # 使用try为了防止几个客户同时注册提交时账号一致报错
            user = UserProfile.objects.create(username=username,
                                              password=password_h,
                                              email=email,
                                              phone=phone,
                                              nickname=username)
        except Exception as e:
            print('create error is %s' % e)
            result = {'code': 10103, 'error': '用户名被占用'}
            return JsonResponse(result)
        # 签发token 生成token后，保存到客户端的本地存储中。本地存储的数据不会自动提交，需要时，通过代码提交。
        token = make_token(username)
        # 字节串表示的token转换为字符串
        token = token.decode()
        # res.data.token
        return JsonResponse({'code': 200, 'username': username, 'data': {'token': token}})

    @method_decorator(login_check)  # django提供的将函数装饰器转换成方法装饰器@method_decorator()
    def put(self, request, username):
        # 1. 获取用户提交的数据
        json_str = request.body  # 获取前端body体中数据
        json_obj = json.loads(json_str)  # 反序列化
        # 2. 从request.myuser中获取要修改的用户
        user = request.myuser
        user.sign = json_obj['sign']
        user.nickname = json_obj['nickname']
        user.info = json_obj['info']
        user.save()
        # 3. 响应（code 200 和用户名）
        result = {'code': 200, 'username': user.username}
        return JsonResponse(result)


def make_token(username, expire=3600 * 24):  # expire过期时间，设置token用户验证时效
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    return jwt.encode(payload, key, algorithm='HS256')
    # pyjwt方法 encode(payload, key, algorithm) 自动拼接,同base64(header) + '.' + base64(payload) + '.' +  base64(sign)


@login_check
def user_avatar(request, username):
    if request.method != 'POST':
        result = {'code': 10105, 'error': '必须是post请求'}
        return JsonResponse(result)
    # 获取已登录用户
    user = request.myuser
    print(user)
    user.avatar = request.FILES['avatar']
    user.save()

    result = {'code': 200, 'username': user.username}
    return JsonResponse(result)


def sms_view(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    # 获取用户输入的手机号
    phone = json_obj['phone']
    # 生成键
    cache_key = 'sms_%s' % phone
    # 生成随机的验证码
    code = random.randint(1000, 9999)
    # 存储到哪儿？键去什么名
    cache.set(cache_key, code, 65)
    print('--send code %s--' % code)
    # 目前是同步方式，方式一
    # 创建容联云对象
    x = YunTongXin(settings.SMS_ACCOUNT_ID, settings.SMS_ACCOUNT_TOKEN,
                   settings.SMS_APP_ID, settings.SMS_TEMPLATE_ID)

    # 发送短信
    res = x.run(phone, code)
    # 希望采用异步方式，方式二
    # 消费者函数名.delay()

    print('--send sms result is %s--' % res)
    return JsonResponse({'code': 200})