from django.http import HttpResponse

def index(resquest):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://cdn.acwing.com/media/article/image/2023/03/17/1_067a3e9cc4-background.gif" width=2000>'
    return HttpResponse(line1 + line2)
