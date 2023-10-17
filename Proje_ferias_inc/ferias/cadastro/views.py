from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Férias, Departamento, Funcionário
from django.core import serializers
import json

def cadastro(request):
    if request.method == "GET":
        cadastro_list = Férias.objects.all()
        return render(request, 'cadastro.html', {'cadastro': cadastro_list})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        data_in = request.POST.get('data_in')
        dias = request.POST.get('dias')
        departamento = request.POST.get('departamento')

        
        departamento = Departamento(
            departamento = departamento
        )

        departamento.save()

        funcionario = Funcionário(
            nome = nome,
            matricula = matricula,
            departamento = departamento
        )

        funcionario.save()

        ferias = Férias(
            nome = nome,
            data_in = data_in,
            dias = dias
        )

        ferias.save() 

    return HttpResponse('Teste')

def att_cadastro(request):
    id_cadastro = request.POST.get('id_cadastro')

    cadastro = Férias.objects.filter(id=id_cadastro)

    cadastro_json = json.loads(serializers.serialize('json', cadastro))[0]['fields']
    data = {'cadastro': cadastro_json}
    return JsonResponse(data)