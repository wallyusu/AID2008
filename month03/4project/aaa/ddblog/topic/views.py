import html
import json
from django.utils.decorators import method_decorator
from tools.login_dec import login_check
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Topic
from tools.login_dec import get_user_by_request
from user.models import UserProfile

# Create your views here.
from tools.cache_dec import topic_cache


class TopicViews(View):  # 继承Django中的View视图类，可自动调用post,get方法。
    def make_topic_res(self, author, author_topic, is_self):
        # 上一篇和下一篇
        if is_self:
            next_topic = Topic.objects.filter(id__gt=author_topic.id,
                                              user_profile_id=author.username).first()

            last_topic = Topic.objects.filter(id__lt=author_topic.id,
                                              user_profile_id=author.username).last()
        else:
            next_topic = Topic.objects.filter(id__gt=author_topic.id,
                                              user_profile_id=author.username,
                                              limit='public').first()

            last_topic = Topic.objects.filter(id__lt=author_topic.id,
                                              user_profile_id=author.username,
                                              limit='public').last()
        if next_topic:
            next_id = next_topic.id
            next_title = next_topic.title
        else:
            next_id = None
            next_title = None

        if last_topic:
            last_id = last_topic.id
            last_title = last_topic.title
        else:
            last_id = None
            last_title = None
        # 生成详情页的返回值
        result = {'code': 200, 'data': {}}
        result['data']['nickname'] = author.nickname
        result['data']['title'] = author_topic.title
        result['data']['category'] = author_topic.category
        result['data']['content'] = author_topic.content
        result['data']['introduce'] = author_topic.introduce
        result['data']['author'] = author.nickname
        result['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        # 上一篇/下一篇
        result['data']['last_id'] = last_id
        result['data']['last_title'] = last_title
        result['data']['next_id'] = next_id
        result['data']['next_title'] = next_title
        # 评论相关
        result['data']['messages'] = []
        result['data']['messages_count'] = 0
        # 返回
        return result

    def make_topics_res(self, author, author_topics):
        # 1. 返回指定用户的文章列表
        topics_res = []
        for topic in author_topics:
            d = {}
            d['id'] = topic.id
            d['title'] = topic.title
            d['category'] = topic.category
            d['introduce'] = topic.introduce
            d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['author'] = author.nickname
            topics_res.append(d)
        res = {'code': 200, 'data': {}}
        res['data']['topics'] = topics_res
        res['data']['nickname'] = author.nickname
        return res

    @method_decorator(login_check)
    def post(self, request, author_id):
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj['content']
        content_text = json_obj['content_text']
        introduce = content_text[:20]
        title = json_obj['title']
        # 避免xss攻击，对用户输入做转义
        title = html.escape(title)
        limit = json_obj['limit']
        if limit not in ['public', 'private']:
            result = {'code': 10300, 'error': 'the limit is error'}
            return JsonResponse(result)
        category = json_obj['category']
        if category not in ['tec', 'no-tec']:
            result = {'code': 10301, 'error': 'the category is error'}
            return JsonResponse(result)

        author = request.myuser
        # 数据入库
        Topic.objects.create(title=title, content=content, limit=limit, category=category, introduce=introduce,
                             user_profile=author)
        return JsonResponse({'code': 200, 'username': author.username})

    @method_decorator(topic_cache(600))
    def get(self, request, author_id):
        print('-------get view in---------')
        try:
            author = UserProfile.objects.get(username=author_id)
        except Exception as e:
            result = {'code': 10302, 'error': 'the auther id is error'}
            return JsonResponse(result)

        print(author)
        # 返回文章列表前，确定访问者的身份
        # 如果是博主本身访问，返回所有文章
        # 如果非博客主人访问，只返回公开的文章
        # 从token中获取用户信息【博主】
        visitor_username = get_user_by_request(request)

        # 获取t_id
        t_id = request.GET.get('t_id')
        is_self = False  # 是否博主访问自己
        if t_id:
            # 获取的是文章详情页
            # 博主访问，可以看所有文章
            if visitor_username == author_id:
                is_self = True
                try:
                    author_topic = Topic.objects.get(id=t_id,
                                                     user_profile_id=author_id)
                except Exception as e:
                    result = {'code': 10310, 'error': 'the topic id is error'}
                    return JsonResponse(result)
            else:
                # 非博主访问，只能看public的文章
                try:
                    author_topic = Topic.objects.get(id=t_id,
                                                     user_profile_id=author_id,
                                                     limit='public')
                except Exception as e:
                    result = {'code': 10310, 'error': 'the topic id is error'}
                    return JsonResponse(result)
            # 按照前端需要的JsonResponse格式返回
            res = self.make_topic_res(author, author_topic, is_self)
            return JsonResponse(res)
        else:
            # 获取的是文章列表页

            # 1.从查询字符串中获取分类的值
            category = request.GET.get('category')
            # 2.判断在 ['tec','no-tec']中
            filter_category = False
            # 是否有分类 [定义一个变量，有分类赋值为True,否则为False]
            if category in ['tec', 'no-tec']:
                filter_category = True

            # 博主访问自己的博客（返回个人+公开的文章）
            if author_id == visitor_username:
                # 4. 是否需要增加分类条件
                if filter_category:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, category=category)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id)
            else:
                # 只返回该用户公开的文章
                # 4. 是否需要增加分类条件
                if filter_category:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public', category=category)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public')
            # 按照一定的格式返回
            res = self.make_topics_res(author, author_topics)
            return JsonResponse(res)