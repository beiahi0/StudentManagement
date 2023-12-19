from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    """中间件"""

    def process_request(self, request):

        # request.path_info 用户请求的url
        passed_url = ['/login/', '/image/code/']
        print(request.path_info)
        if request.path_info in passed_url:
            return
            # 读取访问当前用户的信息
        info_dict = request.session.get("info")
        if info_dict:
            return

        return redirect('/login/')

        # """请求到达之前"""
        # 如果没有返回值，继续往前走 , 否则退回去
        # print("M1 process_request")

        # return HttpResponse("无权访问")

    def process_response(self, request, response):
        """响应到达之前"""
        print("M1 process_response")
        return response
