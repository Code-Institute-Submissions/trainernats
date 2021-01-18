from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_classes, name="all_classes"),
    path("<int:theclass_id>/", views.class_detail, name="class_detail"),
    path("add/", views.add_class, name="add_class"),
    path("edit/<int:theclass_id>/", views.add_class, name="edit_class"),

]