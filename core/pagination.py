from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    # Default number of items to display per page
    page_size = 12

    # Customize query parameter for page size
    page_size_query_param = 'size'

    # Maximum number of items per page (optional)
    max_page_size = 100

    def get_page_size(self, request):
        """
        Get the page size from the query parameters or use the default.
        """
        # Read the 'page_size' query parameter from the request
        page_size = request.query_params.get(self.page_size_query_param)

        # Check if the 'page_size' query parameter is valid and positive
        if page_size and page_size.isdigit():
            return int(page_size)
        
        # If 'page_size' is not provided or not valid, use the default
        return self.page_size
    
    def get_paginated_response(self, data):
        try:
            next = self.get_next_link()
        except:
            next = None
        try:
            previous_link = self.get_previous_link()
        except:
            previous_link = None
        try:
            total_data = self.page.paginator.count
        except:
            total_data = None
            
        return Response({
                'next': next,
                'previous': previous_link,
                'total_data' : total_data,
                'data': data
            })
    