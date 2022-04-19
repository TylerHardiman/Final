from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Log, User
from .serializers import UserSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import User, Comment, Log
from .serializers import UserSerializer, CommentSerializer, AbuseLogSerializer
from django.contrib.auth.models import User


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_users(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = User(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = User.objects.filter(user_id=request.user.id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_abuse_log(request):
    Log = Log.objects.all()
    serializer = AbuseLogSerializer(Log, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_abuse_log(request):
    if request.method == 'POST':
        serializer = AbuseLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        Log = Log.objects.filter(user_id=request.user.id)
        serializer = AbuseLogSerializer(Log, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_abuse_log(request, pk):
    try:
        Log = Log.objects.get(pk=pk)
    except Log.DoesNotExist:
        raise Http404
    serializer = AbuseLogSerializer(Log, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    try:
        Log = Log.objects.get(pk=pk)
    except Log.DoesNotExist:
        raise Http404
    if request.method == 'DELETE':
        operation = Log.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_comments(request):
    comment = Comment.objects.all()
    serializer = AbuseLogSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_comments(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        comment = Comment.objects.filter(user_id=request.user.id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        raise Http404
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        raise Http404
    if request.method == 'DELETE':
        operation = comment.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
    return Response(status=status.HTTP_204_NO_CONTENT)
