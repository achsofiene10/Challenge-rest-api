from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Ticket,Product
from rest_framework import status
from .serializers import TicketSerializer,ProductSerializer
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
from datetime import datetime





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
    file = request.FILES['ticket']
    # datetime object containing current date and time
    now = datetime.now()
    dt_ticket = now.strftime("%d_%m_%Y_%H_%M_%S")
    try:
        path = default_storage.save(str(settings.BASE_DIR) + '/tickets/' +dt_ticket+'.pdf',
                                    ContentFile(file.read()))
        path_ticket=str(settings.BASE_DIR)+'/tickets/'+dt_ticket+'.pdf'
        ticket = Ticket.objects.create(
            file_path=path_ticket,
        )
        serializer = TicketSerializer(ticket)
        return JsonResponse({'ticket': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
