from rest_framework.serializers import ModelSerializer
# from django.config import settings
from apis.accounts.models import User, Profile




class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        field = '__all__'



class CreateUserSerializer(ModelSerializer):
    Profile_Serializer = ProfileSerializer()
    class Meta:
        model= User
        field= ('email', 'username', 'first_name', 'last_name', 'password')


    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
