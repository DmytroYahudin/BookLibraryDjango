from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("search_book/", views.SearchBook.as_view(), name="search_book"),
    path("book/<int:book_id>", views.BookView.as_view(), name="book"),
    path("book/<int:book_id>/delete/", views.DeleteBook.as_view(), name="delete_book"),
    path("book/<int:book_id>/edit_book/", views.EditBook.as_view(), name="edit_book"),
    path(
        "delete_comment/<int:comment_id>",
        views.DeleteComment.as_view(),
        name="delete_comment",
    ),
    path("add_book/", views.NewBook.as_view(), name="add_book"),
    path("add_author/", views.NewAuthor.as_view(), name="add_author"),
]
