from django.urls import path
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('admin_log', views.admin_log, name='admin_log'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('admin_settings', views.admin_settings, name='admin_settings'),
    path('admin_edit_picture', views.admin_edit_picture, name='admin_edit_picture'),
    path('admin_edit_profile', views.admin_edit_profile, name='admin_edit_profile'),
    path('admin_edit_password', views.admin_edit_password, name='admin_edit_password'),
    path('modelshow/(?P<id>\d+)', views.modelshow, name='modelshow'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('registration', views.registration, name='registration'),
    path('Signup_emailval', views.Signup_emailval, name='Signup_emailval'),
    path('', views.home, name='home'),
    path('userhome', views.userhome, name='userhome'),
    path('search', views.search, name='search'),
    path('new_page/(?P<id>\d+)', views.new_page, name='new_page'),
    path('sub/(?P<id>\d+)/(?P<key>[-:\w]+)', views.sub, name='sub'),
    
    #category
    path('category', views.show_category, name="category"),
    path('add_category', views.add_category, name="add_category"),
    path('cat_delete/(?P<cat_id>\d+)', views.cat_delete, name="cat_delete"),
    
    #models
    path('admin_models', views.admin_models, name='admin_models'),
    
    #add model
    path('addmodel', views.addmodel, name="addmodel"),
    path('createmodel', views.createmodel, name="createmodel"),
    
    #payment history
    path('admin_payment_history', views.admin_payment_history, name='admin_payment_history'),
    path('payment_table', views.payment_table, name='payment_table'),
    
    #registered users
    path('registeredusers', views.registeredusers, name='registeredusers'),
    path('delete/(?P<reg_id>\d+)', views.delete, name='delete'),
    
    #model edit
    path('adminedit/(?P<id>\d+)', views.adminedit,name="adminedit"),
    path('modeledit/(?P<id>\d+)', views.modeledit,name="modeledit"),

    #current models
    path('admin_current_models', views.admin_current_models, name='admin_current_models'),
    path('model_delete/(?P<id>\d+)', views.model_delete,name="model_delete"),
    path('test_page', views.test_page,name="test_page"),
    
    
   
	#Leave as empty string for base url
	# path('store', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)