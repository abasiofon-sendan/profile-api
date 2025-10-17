from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime,timezone

class ProfileView(APIView):
    def get(self, request):
        profile_data = {
            "email":"abasiofon135@gmail.com",
            "name":"Abasiofon Uduak Sendan",
            "stack":"Python/Django"
        }

        try:
            fact_response = requests.get("https://catfact.ninja/fact")
            fact_response.raise_for_status() 
            fact = fact_response.json().get("fact", "No fact found")

        except requests.RequestException as e:
            print(f"Error fetching cat fact: {e}")  
            fact = "Error retrieving cat fact"

        data={
            "status": "success",
            "user":profile_data,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "fact": fact

        }

        return Response(data, status=status.HTTP_200_OK, content_type="application/json") 
       


