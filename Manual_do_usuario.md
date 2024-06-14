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

## 3. Uso do Sistema

### 3.1 Registro e Login

#### Registro de Lojista
1. Navegue até a página de cadastro de lojista: `/cadastro_lojista`.
2. Preencha o formulário com os detalhes do lojista e clique em "Registrar".

#### Login de Lojista
1. Navegue até a página de login de lojista: `/login_lojista`.
2. Insira o CNPJ do lojista e clique em "Entrar".

#### Registro de Loja
1. Navegue até a página de cadastro de loja: `/cadastro_loja`.
2. Preencha o formulário com os detalhes da loja e clique em "Registrar".

#### Login de Loja
1. Navegue até a página de login de loja: `/login_loja`.
2. Insira o CNPJ da loja e clique em "Entrar".

### 3.2 Interface de Usuário

#### Tela Inicial
- A página inicial do sistema exibe informações principais e opções de navegação.

#### Gestão de Produtos
1. Navegue até a página de cadastro de produtos: `/cadastro_produtos`.
2. Preencha o formulário com os detalhes do produto e clique em "Salvar".

### 3.3 Funcionalidades Específicas

#### Gestão de Lojas
- Acesse a aba "Lojas" para adicionar, editar ou remover lojas.

#### Gestão de Produtos
- Acesse a aba "Produtos" para adicionar, editar ou remover produtos.

## 4. Solução de Problemas

### 4.1 Problemas Comuns

#### Erro de Conexão
- Verifique se o banco de dados está configurado corretamente no arquivo `settings.py`.

### 4.2 FAQ

#### Como recuperar a senha?
- O sistema não utiliza senhas para login, apenas o CNPJ é necessário.

## 5. Exemplos e Capturas de Tela

(Inserir exemplos relevantes e capturas de tela da interface do usuário aqui)

## 6. Conclusão

Este manual deve fornecer todas as informações necessárias para instalação, configuração e uso adequado do Sistema de Cadastramento e Login de Lojas. Em caso de dúvidas adicionais, consulte a documentação do projeto ou entre em contato com o suporte técnico.



