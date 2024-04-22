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
        EDADMAYOR = request.POST.get('EDADMAYOR')
        FACTORES  = request.POST.get("FACTORES")
        AAS = request.POST.get('AAS')
        ANGINAGRAVE = request.POST.get('ANGINAGRAVE')
        ST = request.POST.get('ST')
        MARCADORPOSITIVO = request.POST.get('MARCADORPOSITIVO')
        CAD = request.POST.get('CAD') 
        
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
        
        timi_result = {
            'EDADMAYOR':EDADMAYOR,
            'FACTORES':FACTORES,
            'AAS':AAS,
            'ANGINAGRAVE':ANGINAGRAVE,
            'ST':ST,
            'MARCADORPOSITIVO':MARCADORPOSITIVO,
            'CAD':CAD,
        }
        
        respuesta = requests.post('http://54.145.45.183:8000/api/prediction/',json=datos_api)
        if respuesta.status_code == 200:
            
            resultado = respuesta.json()
            
            resultado = resultado['Nivel de riesgo']
            
            resultado= resultado * 2.17
            
            print(f'{resultado}')
            print(f"this is the values{timi_result.values()}")
            
            timi_result_valules = 0
            for x in timi_result.values():
                timi_result_valules += int(x)
                
            print(f"this is the values {timi_result_valules}") 
            
            context = {
                "resultado": resultado,
                'timi_result_valules':timi_result_valules
                }
            
            
            return render(request,'test.html',context)
        else :
            return render(request, 'error.html',{'error',respuesta.status_code})
            
        