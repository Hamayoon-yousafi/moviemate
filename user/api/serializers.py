from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'password2']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def validate(self, data):
        if not data['password'] == data['password2']:
            raise serializers.ValidationError('Passwords do not match!')
        
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email already exists')
        
        return data

    def save(self):
        password = self.validated_data['password']
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account