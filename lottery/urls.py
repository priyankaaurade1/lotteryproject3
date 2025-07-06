from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', LogoutView.as_view(next_page='custom_login'), name='logout'),

    # path('adminpanel/update/<int:pk>/', views.update_result, name='update_result'),
    path('adminpanel/edit/', views.edit_results, name='edit_results'),
    path('adminpanel', views.results_history, name='results_history'),
    path('adminpanel/update/', views.update_all_results, name='update_all_results'),
    path('api/next_draw_time/', views.next_draw_time_api, name='next_draw_time_api')

]
