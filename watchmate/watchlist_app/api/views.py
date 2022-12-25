from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models import WatchList,GamePlatform,Review
from watchlist_app.api.Serializers import WatchListSerializer,GamePlatformSerializer, ReviewSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import IsAdminOrReadOnly,IsReviewUserOrReadOnly
# from rest_framework import mixins

class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated] #Only Authenticated users can login
    def get_queryset(self):
        return Review.objects.all()
        

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        watchlist=WatchList.objects.get(pk=pk)

        review_user=self.request.user
        review_queryset=Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this game")

        if watchlist.number_rating==0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2

        watchlist.number_rating=watchlist.number_rating+1            
        watchlist.save()
        serializer.save(watchlist=watchlist, review_user=review_user)

                



class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[IsAuthenticated] #Only Authenticated users can login

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
        
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsReviewUserOrReadOnly]



class GamePlatformVS(viewsets.ModelViewSet):
    queryset=GamePlatform.objects.all()
    serializer_class=GamePlatformSerializer
    permission_classes=[IsAdminOrReadOnly]

        

class GamePlatformAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request):
        platform=GamePlatform.objects.all()
        serializer = GamePlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=GamePlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class GamePlatformDetailAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request, pk):        
        try:
            platform=GamePlatform.objects.get(pk=pk)
        except GamePlatform.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer=GamePlatformSerializer(platform)
        return Response(serializer.data)
    def put(self, request, pk):
        platform=GamePlatform.objects.get(pk=pk)                        
        serializer=GamePlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
    def delete(self, reqeust, pk):
        platform=GamePlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

            
class WatchListAV(APIView):
    permission_classes=[IsAdminOrReadOnly]

    def get(self, request):
        movies=WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class WatchDetailAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    def put(self, request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        



            