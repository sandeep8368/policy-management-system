from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Policy, Claim
from .serializers import PloicySerializer, ClaimSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


@api_view(['POST'])
def register_user(request):
    username = request.data['username']
    password = request.data['password']
    if User.objects.filter(username = username).exists():
        return Response({'error' : "User already exists"}, status=400)
    user = User.object.create_user(username=username, password=password)
    return Response({"msg" : "User created Successfully"})



@api_view(['POST'])
def get_tokens(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
        })
    return Response({"error" : "Invalid credentials "}, status=401)




class PolicyListCreate(ListCreateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PloicySerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class PolicyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Policy.objects.all()
    serializer_class = PloicySerializer
    permission_classes = [IsAuthenticated]
    
    
class ClaimCreate(ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated]