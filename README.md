# kt-docker-compose

Objetivo:
Mostrar a possibilidade de declarar vários contêineres em um arquivo, possibilitando:
1) Criar, excluir, parar, iniciar e reiniciar todos os contêineres de uma só vez apenas com um comando.
2) Permitir que os contêineres comuniquem entre si usando como hostname o nome do serviço.
3) Permitir que os contêineres exponham no ip externo apenas as portas dos serviços que precisam ser acessados de fora. 
4) Permitir que várias instâncias do mesmo contêiner sejam criadas e passem a operar dinamicamente, a princípio, otimizando o uso das threads do servidor e ao mesmo tempo, possibilitando o desenvolvimento local, de sistemas arquitetados para rodar em clusters, como o Docker Swarm e o Kubernetes


## Linux:
#### Instalar o docker-compose no linux.
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

## Windows:
#### Editar o arquivo hosts no Windows
Abrir o cmd.exe com permissões de administrador

notepad \Windows\System32\drivers\etc\hosts

##### Adicionar a linha:

127.0.0.1 web.localhost


#### Fazer tunel da máquina do docker para o localhost caso o docker não rode local:
putty -load "Default Settings" HOSTNAME -l USERNAME -L 80:localhost:80


##### Acessar o Swagger pela url e bater algumas vezes no endpoint
http://web.localhost/swagger/spec.html
##### Modificar o número de instâncias do microerviço:
docker-compose up -d --scale web=5

##### Agora bater mais vezes no endpoint

#### Quem preferir, pode usar o curl ao invés do Swagger:

curl --header 'Host: web.localhost' 'http://web.localhost/v1/system/info' 
