# ☂️ Seletive
O projeto Seletive é uma ideia de aplicação desenvolvida para pessoas que procuram uma forma de organizar as vagas de emprego as quais tem interesse, a plataforma tem como objetivo facilitar essa ação.

![1](https://user-images.githubusercontent.com/78339857/201977468-4ce29c7a-49e0-4e9f-abea-f61d0ac5fc06.png)
![2](https://user-images.githubusercontent.com/78339857/201977492-137653d9-47c8-47c7-9e50-ac7d862cf527.png)
![3](https://user-images.githubusercontent.com/78339857/201977621-829e0c25-9183-4010-95c5-affbfc1911bc.png)
![4](https://user-images.githubusercontent.com/78339857/201977726-5c22c47c-a2a6-4ded-b873-906a060520e9.png)
![5](https://user-images.githubusercontent.com/78339857/201977804-465ae429-8db7-43df-b52d-67119f1e1c43.png)

<hr>

### 📑 Tecnologias usadas:
<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>CSS</td>
    <td>HTML</td>
    <td>Bootstrap</td>
  </tr>
</table>

<hr>

### 🔨 Como executar:

* Clone o repositório e vá para a sua pasta:
```
$ git clone https://github.com/RakelMacedo/Seletive.git

$ cd Seletive/
```
<br>

* Agora, vamos criar o nosso ambiente virtual e ativa-lo:
```bash
$ python3 -m venv venv

$ source venv/bin/activate
```

<br>

* Em seguida, vamos baixar nossas bibliotecas com:
```bash
$ pip install -r requirements.txt
```

<br>

* Vamos criar a estrutura no banco de dados:
``` 
$ python3 manage.py migrate
``` 

<br>

* Vamos criar um super usuario para poder ter acesso administrativo:
```bash
$ python3 manage.py createsuperuser
```
Preencha as informações com seus dados e não se esqueça do seu *usuário* e *senha*. 

<br>

* Agora vamos iniciar nosso servidor:
```bash
$ python3 manage.py runserver
```
<br>

  1. Acesse http://127.0.0.1:8000/admin/ para ir para a interface de administrador do Django, utilize seu usuário e senha para entrar. 
    Lá crie sua lista de Tecnologias, esta será disponibilizada para você selecionar quando for criar uma nova empresa, aparecerá como tecnologias
    usadas e tecnologias que você domina ou não. 

  2. Acesse http://127.0.0.1:8000/home/empresas para ir para a página principal. 


<br>

### ✅ Prontinho! Você esta pronto para utilizar Seletive. Faça bom uso e fique avontade =)
 
