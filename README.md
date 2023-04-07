# V-Mail **DESCONTINUADO**
#### (pt-BR)
### Ferramenta para envio de e-mails com Django e SendGrid.

Link para acesso: https://correioelegante-raficfarah.herokuapp.com/
## Como desenvolver?
1. Clone o repositório;
2. Crie um virtualenv com Python 3.8.10;
3. Ative o virtualenv;
4. Instale as dependências;
5. Configure a instância com o .env;
6. Execute os testes.
```console
git clone https://github.com/raficfarah/v-mail.git
cd v-mail
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python3 manage.py test
```
## Como fazer o deploy
1. Crie uma instância do Heroku;
2. Envie as configurações para o Heroku;
3. Defina uma SECRET_KEY segura para a instância;
4. Defina DEBUG=FALSE;
5. Configure o serviço de email (pode ser Gmail ou SendGrid);
6. Envie o código para o Heroku.
```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py
heroku config:set DEBUG=FALSE
# configura o email
git push heroku master --force
```
#
#### (en)
###Tool for sending e-mails with Django and SendGrid.
Link to access: https://correioelegante-raficfarah.herokuapp.com/
## Usage
1. Clone the repository;
2. Create a virtualenv with Python3.8.10;
3. Activate the virtualenv;
4. Install the dependencies;
5. Configure the instance settings with .env;
6. Run the tests.
```console
git clone https://github.com/raficfarah/v-mail.git
cd v-mail
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python3 manage.py test
```
## How to deploy
1. Create an instance for Heroku;
2. Send the settings to Heroku/;
3. Set a secure SECRET_KEY for the instance;
4. Set DEBUG=FALSE;
5. Configure the e-mail sending service (can be Gmail or SendGrid);
6. Push the code to Heroku.
```console
heroku create myinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py
heroku config:set DEBUG=FALSE
# configure the e-mail service
git push heroku master --force
```
