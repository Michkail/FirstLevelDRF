from django.urls import path
from slurp.api.views import (
    SlurpOfferDetailAPIView,
    SlurpOfferListCreateAPIView
)

urlpatterns = [
    path(
        'slurp/',
        SlurpOfferListCreateAPIView.as_view(),
        name="slurp-list"
    ),

    path(
        'slurp/<int:pk>/',
        SlurpOfferDetailAPIView.as_view(),
        name="slurp-detail"
    )
]