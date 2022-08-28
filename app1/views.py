from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.http import Http404
import random
from datetime import datetime



from app1.models import Users, Incidents
from app1.serializers import userSerializers, incidentSerializers

class userList(APIView):
    # In this Class we will send all the Users from the database and will create new users as well

    def get(self, request, format=None):
        users = Users.objects.all()
        serializerUsers = userSerializers(users, many=True)
        return Response(serializerUsers.data)

    def post(self, request, format=None):
        serializer = userSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class userDetails(APIView):

    def get_objects(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_objects(pk)
        serializer = userSerializers(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_objects(pk)
        serializer = userSerializers(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_objects(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

############################################################################################################

class incidentListUser(APIView):

    def get(self, request, pk, format=None):
        incidents = Incidents.objects.filter(reportName=pk)
        serialize = incidentSerializers(incidents, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

        

###########################################################################################################


class incidentList(APIView):
    
    def get(self, request, format=None):
        incidents = Incidents.objects.all()
        serializerIncidents = incidentSerializers(incidents, many=True)
        return Response(serializerIncidents.data)

    def post(self, request, format=None):
        incidentDATA = request.data
        print(incidentDATA)
        randomID = "RMG"+str(random.randint(10000,99999))+str(datetime.now().year)
        incidentDATA["incidentID"] = randomID
        serialize = incidentSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    

class incidentDetails(APIView):

    def get_object(self, data):
        try:
            return Incidents.objects.get(pk=data)
        except Incidents.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        id = request.data["incidentID"]
        incident = self.get_object(id)
        serialize = incidentSerializers(incident)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def put(self,request, format=None):
        id = request.data["incidentID"]
        req_data = request.data
        # del req_data["id"]
        print(id)
        print(req_data)
        incident = self.get_object(id)

        # incident=Incidents.objects.filter(incidentID=id)
        # print(incident.values)
        serialize = incidentSerializers(incident, data=req_data)
        # print(serialize.data)
        print("SAVYA SACHI")

        if serialize.is_valid():
            print("SARANSH BALYAN")
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        id = request.data["incidentID"]
        incident = self.get_object(id)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)