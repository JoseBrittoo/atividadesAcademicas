Demo
![image](https://github.com/JoseBrittoo/atividadesAcademicas/assets/95869529/fe479312-7a24-41b3-a3ed-1c2df521621b)

## Clonando e configurando o projeto
```
git clone https://github.com/JoseBrittoo/atividadesAcademicas.git
```

Depois de clonado ainda é necessário se fazer mais alguns ajustes para que possamos rodar este projeto na sua máquina. Primeiramente vamos criar um ambiente virtual.
```
python -m venv venv 
```
Após finalizado a instalação e configuração inicial do ambiente virtual acima, podemos ativá-lo com o comando.
```
venv\Scripts\activate
```
Proximo passo é instalar as dependencias do nosso projeto. É simples, basta executar o comando abaixo no seu terminal.
```
pip install -r requirements.txt
```
Para criar as migrações que precisam ser feitas no nosso banco execute os comandos abaixo no seu terminal
```
python manage.py makemigrations
python manage.py migrate
```
Depois de feitos os passos anteriores devemos agora startar nosso servidor local antes de acessar a nossa aplicação.
```
python manage.py runserver
```
Após o start deve aparecer algo assim: 'http://127.0.0.1:8000/' dê Ctrl+clique, que irá para um página no seu navegador, depois que carregar adicione 'http://127.0.0.1:8000/accounts/fcadastro/'

## 🛠️Ferramentas utlizadas
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
