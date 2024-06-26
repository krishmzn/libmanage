from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .producer import ProducerRequest
from .serializers import BookSerializer
from rest_framework import status
from .models import BooksMgmtModel
import requests

# Create your views here.
class BooksViews(APIView):
    def get(self, request):
        received_token = request.headers.get('Authorization')

        validate_token_url = "http://127.0.0.1:8001/validate/user"
        headers = {'Authorization': received_token}
        response = requests.get(validate_token_url, headers=headers)

        # If the token is valid, proceed with fetching and returning the book data
        if response.status_code == 200:
            all_books = BooksMgmtModel.objects.all()
            all_books_serialized = BookSerializer(all_books, many=True)
            return Response(all_books_serialized.data)

        else:
            return Response({"msg": "User auth failed"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        received_request = json.loads(request.body)
        print(received_request)
        mgmt_serializer = BookSerializer(data=received_request)
        if(mgmt_serializer.is_valid()):
            mgmt_serializer.save()
            return Response({"msg": mgmt_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": mgmt_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class BookMgmtViews(APIView):
    def put(self, request, pk):
        try:
            book_instance = BooksMgmtModel.objects.get(pk=pk)
        except BooksMgmtModel.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

        # Assuming you have a serializer for your model
        serializer = BookSerializer(book_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk):
        try:
            book_instance = BooksMgmtModel.objects.get(book_id=pk)
            book_serializer = BookSerializer(book_instance)
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        except BooksMgmtModel.DoesNotExist:
            return Response({"error": "Data does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        try:
            book_instance = BooksMgmtModel.objects.get(book_id=pk)
            book_serializer = BookSerializer(book_instance)
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        except BooksMgmtModel.DoesNotExist:
            return Response({"error": "Data does not exist"}, status=status.HTTP_400_BAD_REQUEST)