from django.shortcuts import render
from django.views import View
import requests


# Create your views here.
class consume_api(View):
    def get(self,request):
        return render(request,'test.html')
    
    def post(self,request):
        EDAD = request.POST.get('EDAD') 
        SEXO = request.POST.get('SEXO') 
        DM2 = request.POST.get('DM2') 
        HAS = request.POST.get('HAS') 
        OBESIDAD = request.POST.get('OBESIDAD') 
        INFARTO_PREVIO = request.POST.get('INFARTO_PREVIO') 
        FALLA_RENAL = request.POST.get('FALLA_RENAL') 
        ALCOHOLISMO = request.POST.get('ALCOHOLISMO') 
        TABAQUISMO = request.POST.get('TABAQUISMO') 
        
        datos_api = {
            'EDAD':EDAD ,
            'SEXO': SEXO,
            'DM2':DM2 ,
            'HAS': HAS,
            'OBESIDAD':OBESIDAD ,
            'INFARTO_PREVIO':INFARTO_PREVIO ,
            'FALLA_RENAL':FALLA_RENAL ,
            'ALCOHOLISMO':ALCOHOLISMO ,
            'TABAQUISMO': TABAQUISMO
        }
        
        respuesta = requests.post('http://54.145.45.183:8000/api/prediction/',json=datos_api)
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            return render(request,'resultado.html',{"resultado":resultado})
        else :
            return render(request, 'error.html',{'error',respuesta.status_code})
            
        