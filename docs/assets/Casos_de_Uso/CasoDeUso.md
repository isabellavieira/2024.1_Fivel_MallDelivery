## Casos de Uso

### Criar Conta (Lojista)
- **Ator:** Lojista
- **Precondições:** O lojista não deve ter uma conta existente no sistema.
- **Fluxo Principal:**
  1. O lojista seleciona a opção “Criar Conta”.
  2. O lojista é solicitado a fornecer um endereço de e-mail e criar uma senha.
  3. O sistema verifica a unicidade do e-mail.
  4. O sistema envia um e-mail de verificação para o endereço fornecido.
  5. O lojista confirma a verificação através do e-mail recebido.
  6. O sistema cria a conta e informa o lojista do sucesso na criação.
- **Fluxo Alternativo:** Caso o e-mail já esteja em uso, o sistema informa o lojista e solicita outro e-mail.
- **Pós-condições:** O lojista possui uma conta ativa e pode logar no sistema.

### Inserir Dados da Loja
- **Ator:** Lojista
- **Precondições:** Lojista está logado e possui uma conta validada.
- **Fluxo Principal:**
  1. O lojista acessa os formulários de inserção de dados da loja.
  2. O lojista insere dados como nome da loja, endereço, telefone, descrição, entre outros.
  3. O sistema salva os dados inseridos de forma temporária, aguardando validação.
- **Pós-condições:** Dados da loja ficam pendentes para validação por um administrador.

### Validar Dados da Loja
- **Ator:** Administrador
- **Precondições:** Existem dados de lojas pendentes de validação.
- **Fluxo Principal:**
  1. O administrador acessa o painel de controle de validações pendentes.
  2. O administrador revisa os dados inseridos pelo lojista.
  3. O administrador aprova ou rejeita os dados.
  4. Se aprovados, o sistema atualiza o status dos dados para "validados".
  5. Se rejeitados, o sistema notifica o lojista para correção.
- **Pós-condições:** Dados da loja são validados e solidificados no sistema.

### Inserir Produto
- **Ator:** Lojista
- **Precondições:** Lojista está logado e tem loja validada.
- **Fluxo Principal:**
  1. O lojista acessa a seção de gestão de produtos.
  2. O lojista escolhe a opção de adicionar um novo produto.
  3. O lojista insere informações do produto, como nome, descrição, preço e fotos.
  4. O sistema salva as informações do produto.
- **Pós-condições:** Produto é adicionado ao perfil da loja no sistema.

### Aceitação dos Termos de Uso
- **Ator:** Lojista
- **Precondições:** O lojista está no processo de criar uma conta.
- **Fluxo Principal:**
  1. Durante o processo de criação da conta, após inserir os dados básicos (e-mail e senha) e antes de finalizar o cadastro, o lojista é apresentado com os Termos de Uso e a Política de Privacidade do sistema.
  2. O sistema exibe o documento dos Termos de Uso de forma clara e acessível, garantindo que o lojista possa ler o conteúdo sem dificuldades.
  3. O sistema requer que o lojista marque uma caixa de seleção indicando que leu e aceita os Termos de Uso e a Política de Privacidade.
  4. O lojista marca a caixa de seleção indicando sua aceitação.
  5. O sistema valida que a caixa de seleção foi marcada.
  6. O lojista pode então prosseguir para finalizar o processo de criação de conta.
  7. O sistema completa o cadastro e cria a conta do lojista.
- **Fluxo Alternativo:** Se o lojista não aceitar os Termos de Uso:
  1. O lojista não marca a caixa de seleção ou tenta prosseguir sem aceitar os termos.
  2. O sistema detecta que a caixa não foi marcada e impede a continuação do processo de cadastro.
  3. O sistema exibe uma mensagem explicando que a aceitação dos Termos de Uso é obrigatória para utilizar o serviço.
  4. O lojista é convidado a revisar e aceitar os Termos de Uso para continuar com o cadastro.
- **Pós-condições:** Se aceitos, o lojista tem sua conta criada com a confirmação de que concordou com os termos legais e políticas do sistema.
