import json
from django.http import JsonResponse
from django.shortcuts import render
from tools.login_dec import login_check
from topic.models import Topic
from message.models import Message
# Create your views here.


@login_check  # 调用效验token函数，只有登录后才能评论
def message_view(request,topic_id):
    if request.method != 'POST':
        result = {'code':10400,'error':'please use POST'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    content = json_obj['content']
    parent_id = json_obj.get('parent_id',0)
    # 从前端ajax中的post_data中获取，当parent_id只有在有回复的时候才能get到，没有回复只有评论时,get不到，故默认为0

    # 检查topic_id是否有效
    try:
        topic = Topic.objects.get(id = topic_id)  # 从路由获取topic_id
    except Exception as e:
        result = {'code':10401,'error':'the topic is error'}
        return JsonResponse(result)
    # 获取登录用户
    user = request.myuser   #从login_check中的request中获取user
    Message.objects.create(topic=topic,content=content,user_profile=user,parent_message=parent_id)
    return JsonResponse({'code':200})

