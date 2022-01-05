from django.urls import path


from .views import index, pregoeiro, list_pregoeiro, processo, empresa, pregao, secretaria, secretario, list_pregao

urlpatterns = [
    path('', index, name='index'),
    path('pregoeiro/', pregoeiro, name='pregoeiro'),
    path('processo/', processo, name='processo'),
    path('empresa/', empresa, name='empresa'),
    path('pregao/', pregao, name='pregao'),
    path('secretaria/', secretaria, name='secretaria'),
    path('secretario/', secretario, name='secretario'),
    path('list_pregoeiro/', list_pregoeiro, name='list_pregoeiro'),
    path('list_pregao/', list_pregao, name='list_pregao')
]


