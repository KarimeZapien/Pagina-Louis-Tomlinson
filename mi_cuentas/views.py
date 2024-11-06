
from django.shortcuts import render

def index(request):
    return render(request, 'mi_cuentas/index.html')  # Asegúrate de que la plantilla existe
