from django.utils.deprecation import MiddlewareMixin
from django.contrib import messages
from django.http import HttpResponseRedirect


ACCESS_URLS = ['/user/login/', '/', '/user/register/']


class BeforeAndAfterViewActions(MiddlewareMixin):
    def process_request(self, request):
        print(request.get_full_path())
        if not request.user.is_authenticated and not request.get_full_path() in ACCESS_URLS :
            messages.warning(request, 'Доступ запрещен')
            return HttpResponseRedirect('/')