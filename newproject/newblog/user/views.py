import hashlib
import json
import random
import time
import jwt
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from user.models import UserProfile
from .tasks import send_sms


# Create your views here.


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
                          'data': {'email': user.email, 'phone': user.phone, }}
            return JsonResponse(result)
        else:
            # 返回所有用户信息
            pass
        return HttpResponse('--users get--')

    def post(self, request):
        json_str = request.body  # 获取json串
        json_obj = json.loads(json_str)  # 将json串转换成python对象
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        sms_num = json_obj['sms_num']
        print(username, email, phone, password_1, password_2)

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
            return JsonResponse(result)  # 自动返回为json串
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
                                              )
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


def make_token(username, expire=3600 * 24):  # expire过期时间，设置token用户验证时效
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    return jwt.encode(payload, key, algorithm='HS256')


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
    # x = YunTongXin(settings.SMS_ACCOUNT_ID, settings.SMS_ACCOUNT_TOKEN,
    #                settings.SMS_APP_ID, settings.SMS_TEMPLATE_ID)
    #
    # # 发送短信
    # res = x.run(phone, code)
    # 希望采用异步方式，方式二
    # 消费者函数名.delay()
    res = send_sms.delay(phone, code)
    print('--send sms result is %s--' % res)
    return JsonResponse({'code': 200})
