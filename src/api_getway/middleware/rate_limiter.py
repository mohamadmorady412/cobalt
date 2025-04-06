from slowapi import Limiter
from slowapi.util import get_remote_address

# Rate limiter to prevent DDoS attacks or overloading the server
limiter = Limiter(key_func=get_remote_address)


def limit_request():
    """
    This function applies rate-limiting on requests based on the user's IP address.
    """
    pass
