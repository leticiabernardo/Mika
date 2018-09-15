## Mika, sua assistente virtual

Este é um projeto inicial de um assistente virtual.<br><br>
No meu tempo livre, vou colocando mais comandos, funcionalidades e "inteligência".<br>
Em breve, escreverei uma documentação melhor sobre como instalar os pacotes para fazê-lo funcionar.<br>
Este projeto é livre, sendo assim, qualquer um pode modificá-lo e melhorá-lo como quiser.


---------------------------------
### Instalando o projeto

Antes de mais nada, você precisará do Python e do gerenciador de pacotes Pip instalados em sua máquina.<br>
Caso não tenha instalado o pip, rode os comandos abaixo:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py
```

Para checar se o Pip foi instalado corretamente, digite:
```
pip list
```

_O `pip list` exibe todos os pacotes já instalados._<br>
Agora com o pip instalado, instale o pacote virtualenv:
```
pip install virtualenv
```

Entre na pasta do projeto e crie sua máquina virtual.

#### Criando a máquina virtual com o virtualenv
Digite no seu terminal:
```
virtualenv venv
```
Caso queira copiar seus pacotes da sua máquina para a máquina virtual, utilize: 
`virtualenv venv -p C:/Python/Python36/python.exe`<br>
_Lembre-se de trocar o caminho pelo qual o Python está instalado em sua máquina._

Note que, é criado a pasta venv no diretório atual.
Para rodar o projeto, você precisará ativar a máquina e instalar todas as depedências do projeto, da seguinte forma:

###### Caso for Windows
```
.\venv\Scripts\activate
```

###### Caso for Linux
```
. venv/bin/activate
```

Com a mv ativada, instale os requisitos do projeto:
```
pip install -r requirements.txt
```

Instale o Espeak:
https://sourceforge.net/projects/espeak/files/latest/download?source=typ_redirect


Renomeie o `config-dist.py` para `config.py` e insira as chaves de APIs conforme as indicações no arquivo.
E, pronto.

---------------------------------
### Executando o projeto

Para executar o projeto, ative a venv e execute:
```
python run.py
```

---------------------------------
### Saindo do projeto
Para sair da virtual env, utilize o comando:
```
deactivate
```
