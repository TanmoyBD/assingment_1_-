from django.urls import path
from app1.views import *
from app1.views import complete_task,ShowTaskPage

urlpatterns = [
     path('', ShowTask,name='showtask'),
     path('addtask/', AddTask, name = 'addtask'),
     path('complete_task/<int:id>', complete_task, name='complete_task'),
     path('delete_task/<int:id>', DeleteTask ,name = 'delete_task'),
     path('edit_task/<int:id>', EditTask ,name = 'edit_task'),
     path('completed/',CompletedPage,name='completedd'),
     path('showtask/',ShowTaskPage,name='showtaskk'),
     
]


