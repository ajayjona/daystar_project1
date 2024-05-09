from django.urls import path
from . import views



urlpatterns = [
    path('', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    #home path
    path('index/', views.index, name='index'),
    #sitters
    path('sitter/', views.sitter, name='sitter'),
    path('sitter/add', views.addsitter, name='sitteradd'),
    path('sitteredit/<int:id>', views.editsitter, name='sitteredit'),
    path('sitter/view/<int:id>', views.viewsitter, name='sitterview'),
    path('sitter/delete/<int:id>', views.deletesitter, name = 'sitterdelete'),
    

    #baby path
    path('baby/', views.baby, name='baby'),
    path('baby/add', views.addbaby, name='babyadd'),
    path('baby/view/<int:id>', views.viewbaby, name='babyview'),
    path('babyedit/<int:id>', views.edit_baby, name='babyedit'),
    path('baby/delete/<int:id>', views.deletebaby, name = 'babydelete'),

    #settings path
    path('settings/', views.settings , name='settings'),
    
    #payments path
    path('payments/', views.payment_view, name='payments'),
    
    #inventory path
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add', views.additem, name='additem')
]
