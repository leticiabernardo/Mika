##Oran

----------------------------------
Ativando no Windows

Criando a maquina virtual
virtualenv venv
virtualenv venv -p C:/Python/Python36/python.exe

ativando
.\venv\Scripts\activate

---------------------------------
Ativando no linux
virtualenv venv

. venv/bin/activate


---------------------------------
Em ambos

listando bibliotecas instaladas
pip list

sudo dnf install python-pyaudio
sudo dnf install redhat-rpm-config
sudo yum install python-devel
sudo yum install libevent-devel
sudo easy_install gevent
sudo yum -y install gcc
ou
sudo apt-get install python-pyaudio

instalando os requisitos do projeto
pip install -r requirements.txt

executando o projeto
python run.py

sair do projeto
deactivate
