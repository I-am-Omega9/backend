from django.urls import path
from .views import CommentAddView,comments_add
urlpatterns = [
    path('comments/', CommentAddView.as_view(), name='comment_add'),
	# path('comments/',  comments_add, name='comment_add'),
]
