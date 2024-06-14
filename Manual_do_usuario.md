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
   source .venv\Scripts\activate
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

