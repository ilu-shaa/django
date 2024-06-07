from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "О нас", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]  

data_db = [
    {'id':1,'title': 'Angelina djoli','content': 'biografi A. D.','is_publi':True},
    {'id':2,'title': 'Margo Robi','content': 'biografi M. R.','is_publi':False},
    {'id':3,'title': 'Djulia Robert','content': 'biografi D. R.','is_publi':True}
]

def index(request):
    data = {
        'title' : 'Главная страница',
        'main_title': "title",
        'menu' : menu,
        'posts': data_db,
        }
    return render(request, 'main/index.html', context=data)

def categori(request, cat_id):
    return HttpResponse(f"<h1>Мужчина</h1><p>id: {cat_id}</p>")

def categori_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Мужчинка</h1><p>slug: {cat_slug}</p>")

def show_post(request, post_id):
    return HttpResponse(f'Statia nomer {post_id}')

def arch(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport', ))
        return HttpResponseRedirect('uri') #HttpResponseRedirect это перемещение временое 301, HttpResponsePermanentRedirect постояное 302
        #return redirect('cat_slug', "music")
        #return redirect('/', permanent=True) #permanent типо страницу перенесли на совсем
    return HttpResponse(f"<h1>godic</h1><p> {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>страница не найдена</h1>")

def about(request):
    return render(request, 'main/about.html', {'title':'O сайте', 'menu': menu})


def addpage(request,):
    return HttpResponse(f'New page')


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')