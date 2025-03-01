from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EmailCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class IdCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login_id']


class SignUpRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'login_id', 'password', 'email', 'team', 'part']

    def create(self, validated_data):
        name = validated_data.get('name')
        login_id = validated_data.get('login_id')
        password = validated_data.get('password')
        email = validated_data.get('email')
        team = validated_data.get('team')
        part = validated_data.get('part')

        user = User(
            name=name,
            login_id=login_id,
            email=email,
            team=team,
            part=part
        )

        user.set_password(password)
        user.save()

        return user


class SignInRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login_id', 'password']


class DemoVoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['tname']


class CandidateVoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['cname', 'part']


class DemoVoteResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['tname', 'detail', 'count']


class CandidateVoteResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['cname', 'part', 'count']


class ResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    messages = serializers.CharField()




