from django.shortcuts import render
from . models import*

# Create your views here.
def consulta (request):
    consultas ={
        'consultas':Musica.objects.all()
    }

    return render(request, 'consultas/consultas.html', consultas)

def apresentacao(request):
     if request.POST:
        nova_apresentacao= apresentacao()
        nova_apresentacao.data_de_apresentacao = request.POST.get('data')
        nova_apresentacao.nome = request.POST.get('data')
        nova_apresentacao.interprete = request.POST.get('data2')
        try:
              musica = Musica.objects.get(pk=request.POST.get('nome_da_musica'))
              nova_apresentacao.nome_da_musica= musica

        except Musica.DoesNotExist:
                print("Música não encontrada")
      
        except Exception as e:
                print("Erro de integridade:", e)
     apresentacao = {
         'musica':Musica.objects.all(),
        }
     
        
     return render(request,'apresentacao/apresentacao.html',apresentacao)

