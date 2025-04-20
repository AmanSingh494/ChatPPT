from django.shortcuts import redirect
import logging
# Configure logging
logger = logging.getLogger('app')

def login_required(view_func):
    """
    Custom decorator to check if the user is authenticated.
    If not, it redirects the user to the login page.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
        # If the user is not authenticated, redirect to login page
            return redirect('login') # Replace 'login' with your URLname for login

        return view_func(request, *args, **kwargs)
    return _wrapped_view
