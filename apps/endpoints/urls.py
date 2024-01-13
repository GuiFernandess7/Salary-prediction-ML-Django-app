from rest_framework.routers import DefaultRouter
from django.urls import path, include

from endpoints.views import EndpointViewSet
from endpoints.views import MLAlgorithmViewSet
from endpoints.views import MLAlgorithmStatusViewSet
from endpoints.views import MLRequestViewSet
from endpoints.views import PredictView
from endpoints.views import ABTestViewSet
from endpoints.views import StopABTestView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path(
        "api/v1/<str:endpoint_name>/predict", PredictView.as_view(), name="predict"
    ),
    path(
        "api/v1/stop_ab_test/<str:test_id>", StopABTestView.as_view(), name="stop_ab"
    ),
]