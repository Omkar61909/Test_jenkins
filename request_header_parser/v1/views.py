from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
#from request_header_parser.v1 import serializers as app_serializer


class RequestHeaderParserDataDetail(APIView):

	def _ip_address(self, request):
		pass


	def get(self, request, *args, **kwargs):
		return Response({'hello': 'world you'}, status=status.HTTP_200_OK)