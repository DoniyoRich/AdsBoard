from rest_framework.pagination import PageNumberPagination


class AdPaginator(PageNumberPagination):
    """
    Пагинатор для вывода ограниченного количества данных на странице.
    """
    page_size = 4
