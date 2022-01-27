from rest_framework.routers import SimpleRouter

from main_app.views import MessageModelViewSet

router = SimpleRouter()

router.register('mail', MessageModelViewSet)

urlpatterns = []
urlpatterns += router.urls
