from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Ticket,Product
from rest_framework import status
from .serializers import TicketSerializer,ProductSerializer

# Create your views here.


#View to get all products
@api_view(["GET"])
@csrf_exempt
def getAllproducts(request):
    products=Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'products': serializer.data}, safe=False, status=status.HTTP_200_OK)

#View to create a new Ticket
@api_view(["POST"])
@csrf_exempt
def addTicket(request):
    payload = json.loads(request.body)
    try:
        ticket = Ticket.objects.create(
            file_path=payload["file_path"],
        )
        serializer = TicketSerializer(ticket)
        return JsonResponse({'ticket': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

