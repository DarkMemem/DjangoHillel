from teachers.views import TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView
from django.urls import path

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('create/', TeacherCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeacherUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TeacherDeleteView.as_view(), name='delete')
]
