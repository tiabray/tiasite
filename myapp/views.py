from django.http import HttpResponse

# page 1: login page. users prompted to enter ipa credentials.
# page 2: list page. users see and may select from list of available instrument queues.
# page 3: queue page. users see instrument queue. includes options to join, etc.
# page 4: admin page. only available to admin users: list of instrument queues. may perform changes.
# Create your views here.

# class MyView(View):
#     def get(Self, request):
#         # <view logic>
#         return HttpResponse('result')

class Instance(Instance):
    def get(name, request):
        # <view logic>
        return HttpResponse('result')