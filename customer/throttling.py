from rest_framework.throttling import UserRateThrottle

# This file is used when custom rate of throttle is required for each model
# Using this scope in settings.py, set the rate of throttle
# Import this file in views.py and set Throttling classes to below mentioned required class.

class CustomerRateThrottle(UserRateThrottle):
    scope = 'customer'

class SubdealerRateThrottle(UserRateThrottle):
    scope = 'subdealer'