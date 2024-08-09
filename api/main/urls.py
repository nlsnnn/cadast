from django.urls import path
from . import views


urlpatterns = [
    path('query/', views.QueryView.as_view()),
    path('result/<str:cad_num>', views.ResultView.as_view()),
    path('ping/', views.PingView.as_view()),
    path('history/', views.HistoryView.as_view())
]