# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Contact
from .serializers import ContactSerializer

from django.core.mail import send_mail


def getAscinding(model_objs: list[Contact]):
    model_class = type(model_objs[0])

    if model_class == Contact:
        indexes = [obj.Sno for obj in model_objs]
        indexes.sort()
        return [model_objs.filter(Sno=sno).first() for sno in indexes]


# Create your views here.
@csrf_exempt
def contactApi(request, sno=0):
    if request.method == 'GET':
        if sno:
            contacts = Contact.objects.filter(Sno=sno)
        else:
            contacts = getAscinding(Contact.objects.all())
        contacts_serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(contacts_serializer.data, safe=False)

    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contacts_serializer = ContactSerializer(data=contact_data)
        if contacts_serializer.is_valid():
            # Sending Email
            send_mail(
                f"Message by - {contact_data['Name']}",  # Subject
                contact_data['Message'],  # Message
                contact_data['Email'],  # From Email
                [contact_data['Message'], ] # + [member.Email for member in Member.objects.filter(
                    # Membership='admin').all()]  # To Mail(s)
            )
            #
            # contacts_serializer.save()
            return JsonResponse("Sent Successfully", safe=False)
        return JsonResponse("Failed to Send", safe=False)

    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact = Contact.objects.get(
            Sno=contact_data['Sno'])
        contacts_serializer = ContactSerializer(
            contact, data=contact_data)
        if contacts_serializer.is_valid():
            contacts_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method == 'DELETE':
        contact = Contact.objects.get(sno=sno)
        contact.delete()
        return JsonResponse("Deleted Successfully", safe=False)
