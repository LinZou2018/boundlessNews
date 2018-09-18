import json
from tornado.web import RequestHandler

from subject.app.allFunction import *
from subject.app.mydatabase import my_new, newsText


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', data=my_new)
    def post(self, *args, **kwargs):
        pass


class AlertsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('alerts.html')
    def post(self, *args, **kwargs):
        pass


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self, *args, **kwargs):
        pass


class RegisterHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('register.html')
    def post(self, *args, **kwargs):
        pass


class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        newsType = self.get_body_argument("type")
        source_url = self.get_body_argument('source_url')
        source_url = source_url.split()
        data = newsText(source_url[0], newsType)
        if newsType == "news":
            gain = to_obtain(source_url, data[0])
            number = 0
            for news in gain:
                if number == 10:
                    break
                news = combination(news)
                self.write(news)
                number += 1
        elif newsType == "alerts":
            if data[1]:
                number = 0
                for alerts in data[0]:
                    if number == 20:
                        break
                    alerts = combination_alerts(alerts)
                    self.write(alerts)
                    number += 1
            else:
                kong = notExist()
                self.write(kong)


class PageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        newsType = self.get_body_argument("type")
        source_url = self.get_body_argument('source_url')
        source_url = source_url.split()
        data = newsText(source_url[0], newsType)[1]
        page = self.get_body_argument("initial")
        if page == "first":
            initial = initialize_the(source_url, data)
            self.write(initial)
        else:
            pages = number_page(page, source_url)
            self.write(pages)



