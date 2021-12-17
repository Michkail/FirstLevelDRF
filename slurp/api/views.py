from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from slurp.models import SlurpOffer
from slurp.api.serializers import SlurpOfferSerializer  

class SlurpOfferListCreateAPIView(APIView):
    def get(self, request):
        slurp = SlurpOffer.objects.filter(available=True)
        serializer = SlurpOfferSerializer(slurp, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SlurpOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlurpOfferDetailAPIView(APIView):
    def get_object(self, pk):
        slurp = get_object_or_404(SlurpOffer, pk=pk)
        return slurp

    def get(self, request, pk):
        slurp = self.get_object(pk)
        serializer = SlurpOfferSerializer(slurp)
        return Response(serializer.data)

    def put(self, request, pk):
        slurp = self.get_object(pk)
        serializer = SlurpOfferSerializer(slurp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        slurp = self.get_object(pk)
        slurp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListAPIView(APIView):
    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(
            journalists,
            many=True,
            context={
                "request": request
            }
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
