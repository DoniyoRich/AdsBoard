from rest_framework.pagination import PageNumberPagination


class UserPaginator(PageNumberPagination):
    """
    Пагинатор для вывода ограниченного количества пользователей на странице.
    """
    page_size = 4
