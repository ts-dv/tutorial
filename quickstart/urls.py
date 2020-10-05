from rest_framework import routers

from .views import PizzaList

router = routers.DefaultRouter()

router.register('', PizzaList, basename='pizza')

urlpatterns = router.urls
