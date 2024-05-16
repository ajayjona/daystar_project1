from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
   
    path('', auth_views.LoginView.as_view(template_name='application/login.html'), name='login'),
    # path('', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
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

    #doll_store path
    path('doll_list/', views.doll_list , name='doll_list'),
    path('doll/add', views.doll_add, name='doll_add'),
    path('doll_edit/<int:id>',views.doll_edit, name='edit_doll'),
    path('doll_delete/<int:id>', views.shopitem_delete, name='doll_delete'),
    
    #doll transactions
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('transaction_add/',views.transaction_add, name='add_transaction'),
    path('transaction_edit/<int:id>',views.transaction_edit, name='edit_transaction'),
    path('transaction_delete/<int:id>',views.transaction_delete, name='delete_transaction'),
    
    #payments path
    # path('payment/',views.payment, name='payements'),
    path('payments/', views.payment, name='payments'),
    path('payment_success/<int:id>/', views.payment_success, name = 'payment_success'),
    
    #inventory path
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/add', views.additem, name='additem')
]
