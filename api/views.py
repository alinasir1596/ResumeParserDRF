from drf_yasg.openapi import Parameter, IN_QUERY
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Keyword, KeywordTag
from api.pagination import BasicPagination, PaginationHandlerMixin
from api.serializers import ParserSerializer, KeywordSerializer, KeywordTagSerializer
from parser.matcher import sentence_extract


def response_standard(response_data, message, status):
    return {
        "data": response_data,
        "message": message,
        "httpCode": status
    }


class ParserView(APIView):
    @swagger_auto_schema(
        request_body=ParserSerializer,
        responses={
            200: "Parsed",
            401: "Unauthorized",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        manual_parameters=[
            Parameter("experience", IN_QUERY, type="int"),
            Parameter("tool", IN_QUERY, type="int"),
            Parameter("job_title", IN_QUERY, type="int"),
        ],
    )
    def post(self, request):
        try:
            request_data = request.data
            header = request.headers
            filter_param = request.query_params
            serializer = ParserSerializer(data=request_data)
            if serializer.is_valid():
                if header['Authorization'] == '6251655368566D597133743677397A24':
                    response = sentence_extract(request_data, **filter_param)
                    return Response(response_standard(response_data=response, message=None, status=200), '200')
                else:
                    return Response(response_standard(response_data=None, message=f"Unauthorized", status=401), '401')
            else:
                return Response(response_standard(response_data=None, message=serializer.errors, status=400), '400')
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')


class TaggerRetrieveView(RetrieveAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer


class TaggerCreateView(CreateAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer


class TaggerListView(ListAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer
    pagination_class = PageNumberPagination


class TaggerDestroyView(DestroyAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer


class TaggerUpdateView(UpdateAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer


class KeywordManagementView(APIView):

    @swagger_auto_schema(
        operation_description="PUT keywords-management/1/",
        request_body=KeywordSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def put(self, request, pk):
        try:
            keyword = Keyword.objects.get(pk=pk)
            serializer = KeywordSerializer(data=request.data, instance=keyword)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, status=200), '200')
            else:
                return Response(response_standard(response_data=None, message=serializer.errors, status=400), '400')
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')

        except Keyword.DoesNotExist as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')

    @swagger_auto_schema(
        operation_description="DELETE keywords-management/1/",
        request_body=KeywordSerializer,
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def delete(self, request, pk):
        try:
            keyword = Keyword.objects.get(pk=pk)
            keyword.delete()
            return Response(response_standard(response_data=None,
                                              message=f"Keyword Object deleted successfully against id {pk}",
                                              status=200), '200')

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')

        except Keyword.DoesNotExist as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')


class KeywordView(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = KeywordSerializer

    @swagger_auto_schema(
        operation_description="POST keywords-management",
        request_body=KeywordSerializer,
        responses={
            201: "Created",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        try:
            data = request.data
            serializer = KeywordSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(response_standard(response_data=serializer.data, message=None, status=201), '201')
            else:
                return Response(response_standard(response_data=None, message=serializer.errors, status=400), '400')
        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')

    @swagger_auto_schema(
        operation_description="GET keywords-management",
        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
        manual_parameters=[
            Parameter("keyword_value", IN_QUERY, type="string"),
        ],
    )
    def get(self, request):
        try:
            if request.query_params.get('keyword_value'):
                keywords = Keyword.objects.filter(keyword_value__icontains=request.query_params.get('keyword_value'))
            else:
                keywords = Keyword.objects.all()
            page = self.paginate_queryset(keywords)
            if page is not None:
                serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
                return Response(response_standard(
                    response_data=serializer.data,
                    message=None,
                    status=200
                ),
                    status=status.HTTP_200_OK
                )
            else:
                serializer = self.serializer_class(keywords, many=True)
                return Response(response_standard(
                    response_data=serializer.data,
                    message=None,
                    status=200
                ),
                    status=status.HTTP_200_OK
                )

        except Exception as e:
            return Response(response_standard(response_data=None, message=e.args[0], status=500), '500')




