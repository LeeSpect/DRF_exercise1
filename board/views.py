from .models import Board
from .serializers import BoardSerializer, CommentSerializer, BoardsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class BoardList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):   # request는 쓰이지 않지만, get()함수의 인자로 request가 입력되기 때문에 반드시 입력해야 한다.
        boards = Board.objects.all()
        serializer = BoardsSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BoardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        board = get_object_or_404(Board, pk=pk)
        return board
    
    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BoardUpdate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def put(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDestroy(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def delete(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        serializer = CommentSerializer(board.comments, many=True)   # board(pk)에 해당하는 모든 댓글을 가져옴
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post_id=pk)   # post_id는 url에서 pk로 받아온다.
            # 위 코드에서 post_id가 뜻하는 것은 CommentSerializer의 post필드이다.
            # post필드는 Board모델의(로 구성되는) 외래키이므로, post_id를 통해 Board모델의 pk를 받아온다.
            # 이를 통해 Comment모델의 post필드에 Board모델의(에서 가져온) pk를 저장한다.
            # post_id=pk가 아니라 post=pk로 저장하게 되면, Cannot assign "<pk>": "Comment.post" must be a "Board" instance. 라는 에러가 발생한다.
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnivBoardList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        boards = Board.objects.filter(user__university=pk)
        serializer = BoardsSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)