from django.urls import path


from .views import index, pregoeiro, list_pregoeiro, processo, empresa, pregao, secretaria, secretario, list_pregao, \
    list_representante, list_secretario, list_secretaria, list_empresa, representante

urlpatterns = [
    path('', index, name='index'),
    path('pregoeiro/', pregoeiro, name='pregoeiro'),
    path('processo/', processo, name='processo'),
    path('empresa/', empresa, name='empresa'),
    path('representante/', representante, name='representante'),
    path('pregao/', pregao, name='pregao'),
    path('secretaria/', secretaria, name='secretaria'),
    path('secretario/', secretario, name='secretario'),
    path('list_pregoeiro/', list_pregoeiro, name='list_pregoeiro'),
    path('list_pregao/', list_pregao, name='list_pregao'),
    path('list_representante/', list_representante, name='list_representante'),
    path('list_secretario/', list_secretario, name='list_secretario'),
    path('list_secretaria/', list_secretaria, name='list_secretaria'),
    path('list_empresa/', list_empresa, name='list_empresa')
]


