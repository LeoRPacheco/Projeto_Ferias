function exibir_form(tipo){
    add_cadastro = document.getElementById('adicionar-cadastro')
    att_cadastro = document.getElementById('att_cadastro')

    if(tipo == "1"){
        att_cadastro.style.display = "none"
        add_cadastro.style.display = "block"

    }else if(tipo == "2"){
        att_cadastro.style.display = "block"
        add_cadastro.style.display = "none"
    }
}

function dados_cadastro(){
    cadastro = document.getElementById('cadastro-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_cadastro = cadastro.value

    data = new FormData()
    data.append('id_cadastro', id_cadastro)

    fetch("/ferias/atualiza_cadastro/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data

    }).then(function(result){
        return result.json()

    }).then(function(data){
        
        document.getElementById('form-att-cadastro').style.display = 'block'

        nome = document.getElementById('nome')
        nome.value = data['nome']

        matricula = document.getElementById('matricula')
        matricula.value = data['matricula']

        data_in = document.getElementById('data_in')
        data_in.value = data['data_in']

        dias = document.getElementById('dias')
        dias.value = data['dias']
    })
}

function update_cadastro(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('matricula').value
    email = document.getElementById('data_in').value
    cpf = document.getElementById('dias').value

    fetch('/clientes/update_cliente/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if(data['status'] == '200'){
            nome = data['nome']
            sobrenome = data['sobrenome']
            email = data['email']
            cpf = data['cpf']
            console.log('Dados alterado com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }

    })

}