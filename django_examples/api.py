from rest_framework import routers
from bookstore.serializers import BookViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
