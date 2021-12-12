from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'Id', 'Name', 'Membership', 'ExperianceType',
            'Email', 'DateOfJoining', 'PhotoFile',
            'KnownLanguages', 'BooksWritten', 'WorkingHours', 'Projects', 'About'
        )

