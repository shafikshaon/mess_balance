from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def super_admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    # Decorator for views that checks that the logged in user is a super admin user,
    # otherwise redirects to login page.

    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_superuser, login_url=login_url,
                                        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    # Decorator for views that checks that the logged in user is a admin,
    # otherwise redirects to login page.

    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_admin and u.is_admin, login_url=login_url,
                                        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator


def website_user_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    # Decorator for views that checks that the logged in user is a website user,
    # otherwise redirects to login page.

    actual_decorator = user_passes_test(lambda u: u.is_active and u.is_website_user, login_url=login_url,
                                        redirect_field_name=redirect_field_name)
    if function:
        return actual_decorator(function)
    return actual_decorator
