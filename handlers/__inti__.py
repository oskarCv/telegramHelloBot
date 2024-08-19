# handlers/__init__.py
from .start import start_router
from .subscribe import subscribe_router
# from .validate import validate_router

# You can include routers here for easier access from the bot
all_routers = [start_router, subscribe_router]