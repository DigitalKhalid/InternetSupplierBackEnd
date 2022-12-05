from rest_framework.throttling import UserRateThrottle

class CustomerRateThrottle(UserRateThrottle):
    scope = 'customer'

class SubdealerRateThrottle(UserRateThrottle):
    scope = 'subdealer'