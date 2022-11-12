from rest_framework.pagination import PageNumberPagination

# ============================================================================ #


# ============================= DEFAULTPAGINATION ============================ #


class DefaultPagination(PageNumberPagination):
    page_size = 10
