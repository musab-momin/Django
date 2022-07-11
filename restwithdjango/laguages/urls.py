from django.urls import path, include
from rest_framework import routers
from laguages.views import LanguageView, LanguageInventorView, ProgrammerView


router = routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('language_inventor', LanguageInventorView)
router.register('programmer', ProgrammerView)


urlpatterns = [
    path('', include(router.urls)),
]