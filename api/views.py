import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

AI_URL = "http://localhost:9000/consult"

@api_view(["POST"])
def consult(request):

    text = request.data.get("text")

    r = requests.post(
        AI_URL,
        json={"text": text}
    )

    return Response(r.json())
