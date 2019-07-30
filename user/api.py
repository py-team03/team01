from django.http import JsonResponse
from django.shortcuts import render

from user.models import User
# Create your views here.
def submit_phone(request):
    '''
    提交手机号，发送验证码提交短信验证码，登录
    :param request:
    :return:
    '''
    # phone = request.POST.get('phone')
    phone = request.GET.get('phone')
    print(phone)
    return 'hhh'


def submit_vcode(request):
    '''
    提交短信验证码，登录
    :param request:
    :return:
    '''
    pass


def get_profile(request):
    '''
    获取个人资料
    :param request:
    :return:
    '''
    return JsonResponse({'code':0,'data':None})


def set_profile(request):
    '''
    修改个人资料
    :param request:
    :return:
    '''
    pass


def upload_avatar(request):
    '''
    头像上传
    :param request:
    :return:
    '''
    pass
