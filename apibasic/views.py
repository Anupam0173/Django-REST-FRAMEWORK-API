from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# below 3 line is sufficient for all crud operiation
# 127.0.0.1: 8000/viewset/articles                   #for list and create
# http://127.0.0.1:8000/viewset/article/1            #for delete,update,put and patch


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# below ArticleViewSet class 3 line is sufficient for all crud operiation
# 127.0.0.1: 8000/viewset/articles                   #for list and create
# http://127.0.0.1:8000/viewset/article/1            #for delete,update,put and patch

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# below ArticleViewSet class is sufficient for list and create operiation but here code is very large
# 127.0.0.1: 8000/viewset/articles                   #for list and create
# http://127.0.0.1:8000/viewset/article/1            #for delete,update,put and patch

# class ArticleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         print("hiiiiiiiii", serializer.data)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# below GenericAPIView and GenericAPIDetailView views are responsible for all crud operations and it has been implemented by GenericAPIView and mixins.


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class GenericAPIDetailView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    # below 2 lines is for basic authentication functionality
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # below line for token authentication
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # below line is for jwt authentication functionality
    permission_classes = (IsAuthenticated, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# below is the manual approach which is implemented APIView.


class ArticleAPIView(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def articles_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        print("hiiiiiiiii", serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
