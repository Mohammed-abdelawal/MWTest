import time
from datetime import datetime

from django.db.models import F
from django.shortcuts import redirect
from django.utils import timezone
from user_agents import parse

from .models import PageAnalyticsCount


class EveryPageCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.start_time = time.time()
        response = self.get_response(request)
        costed = time.time() - self.start_time
        if request.path != "/error/":
            PageAnalyticsCount.objects.create(
                url=request.path,
                process_time=costed,
                lang=request.META['LANG'],
                method=request.META['REQUEST_METHOD'],
                user_agent=str(parse(request.META['HTTP_USER_AGENT'])),
                user_ip = request.META['REMOTE_ADDR'],
                )
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print(f'request to response cost: {costed}s')
        return response


class SiteVisitsCounterMiddleware:
    def __init__(self, get_response):
        self.total_requests = 0
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.total_requests+=1
        print(self.total_requests)
        return response


class LimitedRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        today_min = datetime.combine(timezone.now().date(), datetime.today().time().min)
        today_max = datetime.combine(timezone.now().date(), datetime.today().time().max)
        user_ip = request.META['REMOTE_ADDR']
        visit_count_last_day = PageAnalyticsCount.objects.filter(user_ip=user_ip,visit_time__range=(today_min, today_max)).count()
        if visit_count_last_day > 300 and  request.path != "/error/":
            return redirect('nomore')
        response = self.get_response(request)

        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print(f'request to response cost: {costed}s')
        return response
