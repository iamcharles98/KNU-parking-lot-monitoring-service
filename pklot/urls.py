app_name = 'pklot'
from pklot import views as v1
from cctv import views as v2
from django.urls import path

urlpatterns = [
    path('test/', v1.test),
    path('test2/', v1.test2),
    path('run/', v2.execute_detect_py),
]