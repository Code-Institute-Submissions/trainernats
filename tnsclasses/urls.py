from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_classes, name="all_classes"),
    path("<int:theclass_id>/", views.class_detail, name="class_detail"),
    path("add/", views.add_class, name="add_class"),
    path("edit/<int:theclass_id>/", views.edit_class, name="edit_class"),
    path("delete/<int:theclass_id>/", views.delete_class, name="delete_class"),
    path("delete_class_confirmation/<int:theclass_id>/",
         views.delete_class_confirmation, name="delete_class_confirmation"),
]
