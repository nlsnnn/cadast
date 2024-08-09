from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Query
from .serializers import QuerySerializer
from .services import server


class QueryView(CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class ResultView(RetrieveAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    lookup_field = 'cad_num'


class PingView(APIView):
    def get(self, request):
        return Response(status=200)


class HistoryView(ListAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer