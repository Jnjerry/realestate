from rest_framework.serializers import (
ModelSerializer,
EmailField,
CharField,
# HyperLinkedIdentityField,
SerializerMethodField,
ValidationError
)

from django.db.models import Q
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields =[
            'email',
            'username',
            'password',

        ]
        extra_kwargs={"password":{"write_only":True}}
    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
class UserLoginSerializer(ModelSerializer):
    token=CharField(allow_blank=True,read_only=True)
    email=EmailField(label='Email Address',required=False,allow_blank=True)
    username=CharField(allow_blank=True,required=False)
    class Meta:
        model=User
        fields =[
            'email',
            'username',
            'password',
            'token',

        ]
        extra_kwargs={"password":{"write_only":True}}


    def validate(self,data):
        email=data.get("email",None)
        username=data.get("username",None)
        if not email and not username:
            raise ValidationError("A username or email is required to login")
        return data
