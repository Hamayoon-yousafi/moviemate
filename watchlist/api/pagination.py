from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'watch_list_page' # by default the param is called page (?page=2) but we can override that.
    page_size_query_param = 'limit' # we have set the page_size or limit to 3 but we can accept limit from client side in the param set in the page_size_query_param as ?limit=10
    max_page_size = 10 # setting a limit to size of the records so client cannot exceed this limit
    last_page_string = 'last_page' # by default, last page string is 'last' as ?page=last which will take us to the last pasge but we can override it by setting last_page_string option.


class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10
    limit_query_param = 'movies_limit'
    offset_query_param = 'start'


class WatchListCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'created' # the field we wish to base the order of records upon
    cursor_query_param = 'page' # default value is cursor as cursor=cD0yMDIzLTA4LTAxKzA. the random text represents next page so hiding the page number