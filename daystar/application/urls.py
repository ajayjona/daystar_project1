from django.urls import path
from . import views



urlpatterns = [
    #home path
    path('', views.index, name='index'),
    #sitters
    path('sitter/', views.sitter, name='sitter'),
    path('sitter/add', views.addsitter, name='sitteradd'),
    path('sitteredit/<int:id>', views.editsitter, name='sitteredit'),
    path('sitter/view/<int:id>', views.viewsitter, name='sitterview'),

    #baby path
    path('baby/', views.baby, name='baby'),
    path('baby/add', views.addbaby, name='babyadd'),
    path('baby/view/<int:id>', views.viewbaby, name='babyview'),
    path('babyedit/<int:id>', views.edit_baby, name='babyedit'),

    #settings path
    path('settings/', views.settings , name='settings'),
    
    #payments path
    path('payments/', views.payment, name='payments'),
    #inventory path
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add', views.additem, name='additem')
]
