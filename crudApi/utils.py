import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
from rest_framework.response import Response


def movieList(num):

    try:
        url = 'https://demo.credy.in/api/v1/maya/movies/'
        if num is not None:
            url += num
        flag = False
        a=0
        while(flag==False):
            a+=1
            print(a)
            response = requests.get(url, auth=HTTPBasicAuth(settings.ID, settings.PASSWORD))
            if response.status_code == 200:
                print("hey")
                flag = True
                return Response(response.json())
    except requests.exceptions.ConnectionError:
        return Response({
            'error': 'Something went wrong'
        })

