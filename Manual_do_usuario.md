# Manual de Usuário do Sistema de Cadastramento e Login de Lojas

## 1. Introdução
Bem-vindo ao Sistema de Cadastramento e Login de Lojas. Este manual fornecerá todas as informações necessárias para instalar, configurar e usar o sistema.

## 2. Instalação
### Requisitos do Sistema
- **Sistema Operacional**: Windows 10 ou superior
- **Python** instalado
- **Django** instalado

### Passos de Instalação
#### 1. Instalação do Python
Certifique-se de que o Python está instalado no seu sistema. Você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/downloads/).

#### 2. Instalação do Django
Depois de instalar o Python, você pode instalar o Django usando o pip, que é o gerenciador de pacotes do Python.
   ```bash
   pip install django
   ```

#### 3. Clone o Repositório
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```

#### 4. Navegue até o Diretório do Projeto
   ```bash
   cd Projeto_Cadastramento
   ```

#### 5. Crie um ambiente virtual e ative-o
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate
   ```

#### 6. Instale as dependências (lista de pacotes python)
   ```bash
   pip install -r requirements.txt
   ```

#### 7. Configure o Banco de dados
   ```bash
   python manage.py migrate
   ```

#### 8. Execute o Servidor de desenvolvimento
   ```bash
   python manage.py runserver
   ```

## 3. Uso do Sistema

#### 3.1 Tela Inicial
- A página inicial do sistema exibe produtos de todas as lojas cadastradas.

### 3.2 Registro e Login

#### Registro de Lojista
1. Navegue até a página de cadastro de lojista por meio do botão "Cadastrar".
2. Preencha o formulário com os detalhes do lojista e clique em "Enviar".
3. Navegue até a página de login de lojista por meio do botão "Login".

#### Login de Lojista
1. Insira o email cadastrado e a senha criada para o lojista.
2. Navegue para a página de cadastramento/login da lojapor meio do botão "Entrar".

#### Registro de Loja
1. Preencha o formulário com os detalhes da loja e clique em "Enviar".
2. Navegue para a página de login da loja por mio do botão "Login da sua loja".

#### Login de Loja
1. Insira o CNPJ da loja e a senha criada e clique em "Entrar".

### 3.3 Interface de Usuário

#### Gestão de Produtos
1. Após o login da loja ser realizado, clique em "Cadastrar Produtos".
2. Preencha o formulário com as informações e imagens desejadas, e clique em "Enviar".

## 4. Solução de Problemas

### Erro de Conexão
- Verifique se o banco de dados está configurado corretamente no arquivo `settings.py`.

## 5. Manutenção e Atualizações

### Como atualizar
1. Dar commit no repositório dentro do Github sempre que houver uma alteração.

## 6. Recursos Adicionas

- Email: contato@malldelivery.com.br
