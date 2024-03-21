from django.urls import path

from article.views import ListArticleViews, DetailArticleView, PostArticleView, DeleteArticleView

# api untuk memanggil adalah dengan path (urlnya, nama kelasnya)
urlpatterns =[
    path('shows/',ListArticleViews.as_view()),
    path('read/<slug:slug>', DetailArticleView.as_view()),
    path('', PostArticleView.as_view()),
    path('<slug:slug>/delete/',DeleteArticleView.as_view())

]