from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class ApiViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response("Este endpoint utiliza o verbo GET.")

    def create(self, request):
        return Response(f"Este endpoint utiliza o verbo POST.")

    action(detail=False, methods=['put'])
    def put(self, request):
        return Response("Este endpoint utiliza o verbo PUT.")

    action(detail=False, methods=['post'])
    def post_dado(self, request, dado): 
        request.data['dado']
        return Response(f"Este endpoint recebe o nome {dado} via URL.")

    action(detail=False, methods=['put'])
    def put_dado(self, request, *args, **kwargs):
        return Response(f"Este endpoint recebe o nome {dado} via URL.")

    action(detail=False, methods=['delete'])
    def delete(self, request):
        return Response(f"Este endpoint utiliza o verbo DELETE.")
