from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('task',views.add_task, name='add_task'),
    path('update<int:id>',views.update_task, name='update_task'),
    path('delete<int:id>',views.delete_task, name='delete_task'),
    path('complete_task<int:id>',views.complete_task, name='complete_task'),
    path('completed_task_clear',views.completed_task_clear, name='completed_task_clear'),
    path('cbv_home', views.TaskListView.as_view(), name='cbv_home'),
    path('cbv_details<int:pk>', views.TaskDetailView.as_view(), name='cbv_details'),
    path('cbv_update<int:pk>', views.TaskUpdateView.as_view(), name='cbv_update'),
    path('cbv_delete<int:pk>', views.TaskDeleteView.as_view(), name='cbv_delete'),

]

