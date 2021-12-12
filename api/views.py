# Importing Modules
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Importing Models and Serializers
from .models import Member
from .serializers import MemberSerializer


def getAscinding(model_objs: list[Member]):
    model_class = type(model_objs[0])

    if model_class == Member:
        indexes = [obj.Id for obj in model_objs]
        indexes.sort()
        return [model_objs.filter(Id=id).first() for id in indexes]


# Create your views here.
@ csrf_exempt
def memberApi(request, id=0):
    if request.method == 'GET':
        if id:
            members = Member.objects.filter(Id=id)
        else:
            members = getAscinding(Member.objects.all())
        members_serializer = MemberSerializer(members, many=True)
        return JsonResponse(members_serializer.data, safe=False)

    elif request.method == 'POST':
        member_data = JSONParser().parse(request)
        members_serializer = MemberSerializer(data=member_data)
        if members_serializer.is_valid():
            members_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        member_data = JSONParser().parse(request)
        member = Member.objects.get(
            Id=member_data['Id'])
        members_serializer = MemberSerializer(member, data=member_data)
        if members_serializer.is_valid():
            members_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        member = Member.objects.get(Id=id)
        member.delete()
        return JsonResponse("Deleted Successfully", safe=False)
