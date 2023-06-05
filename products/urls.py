from django.urls import path
from . import views

app_name="products"

urlpatterns = [
    path('list/',views.product_list_view,name="list"),
    path('detail/<id>/',views.product_detail_view,name="detail"),
    path('create/',views.create_view,name="create"),
    path('update/<id>/',views.blog_update_view,name="update"),
    path('delete/<id>/',views.blog_delete_view,name="delete")
]
