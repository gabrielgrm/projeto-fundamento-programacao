# projeto-fundamento-programacao
Manual do Usuário - Sistema de Rastreamento de Despesas Pessoais

**Para a utilização desse programa, é necessario a instalação do módulo TWILIO**, para esta rodando a aplicação de forma correta
Utilize o comando *pip3 install twilio*
Para saber mais sobre a instalação: https://www.twilio.com/pt-br/docs/libraries/python

Bem-vindo ao Sistema de Rastreamento de Despesas Pessoais! Este programa permite que você registre suas despesas, visualize suas despesas registradas, verifique seu saldo e exclua despesas indesejadas. Abaixo, você encontrará um guia passo a passo sobre como usar o programa.

1. Login:
   - Na tela inicial, você terá três opções:
     a) Digite '1' e pressione Enter para fazer login se já tiver uma conta registrada.
     b) Digite '2' e pressione Enter para se cadastrar e criar uma nova conta.
     c) Digite '3' e pressione Enter para sair do programa.

2. Fazer Login:
   - Se você selecionou a opção de login, você será solicitado a inserir seu nome de usuário (login) e senha.
   - Logo apos é solicitado um token enviado para o número de cadastro no registro.
   - Após inserir suas credenciais, o sistema verificará se as informações estão corretas.
   - Se o login for bem-sucedido, você será redirecionado para o menu principal.

3. Cadastro:
   - Se você selecionou a opção de cadastrar, você precisará preencher algumas informações para criar uma nova conta.
   - Primeiro, insira um nome de usuário (login) exclusivo.
   - Segundo, insira seu número de telefone. ex (+5581998781729)
   - Logo depois, escreva o token recebido via mensagem no seu celular.
   - Em seguida, defina uma senha para a sua conta e confirme-a.
   - Depois disso, você será solicitado a inserir seu salário mensal.
   - Após confirmar seu salário, sua conta será criada e você será redirecionado para o menu principal.

4. Menu Principal:
   - No menu principal, você tem as seguintes opções:
     a) Digite '1' e pressione Enter para registrar uma nova despesa.
     b) Digite '2' e pressione Enter para ver suas despesas registradas.
     c) Digite '3' e pressione Enter para verificar seu saldo.
     d) Digite '4' e pressione Enter para excluir uma despesa.
     e) Digite '5' e pressione Enter para fazer logout e sair do programa.

5. Registrar Despesa:
   - Ao selecionar essa opção, você será solicitado a fornecer informações sobre a despesa:
     a) Insira o nome da despesa.
     b) Insira o valor da despesa.
     c) Insira a categoria da despesa.
   - Após fornecer essas informações, a despesa será registrada e você será redirecionado de volta ao menu principal.

6. Ver Despesas:
   - Ao selecionar essa opção, você verá uma lista das suas despesas registradas.
   - Se desejar filtrar as despesas por categoria, insira o nome da categoria desejada. Se preferir ver todas as despesas, pressione Enter sem digitar nada.
   - Após visualizar as despesas, pressione Enter para voltar ao menu principal.

7. Ver Saldo:
   - Ao selecionar essa opção, você verá o saldo atual com base no seu salário e nas despesas registradas.
   - O saldo será exibido em reais (R$).
   - Pressione Enter para voltar ao menu principal.

8. Registar Ganhos:
   - Ao selecionar essa opção, você será solicitado a fornecer informaçoes sobre o seu ganho:
      a) Insira o valor do valor ganho.
   - Após forneceser essa informação, esse ganho será registrado e você será redirecionado de volta ao menu principal.

9. Excluir Despesa:
   - Ao selecionar essa opção, você verá uma lista das suas despesas registradas.
   - Insira o nome da despesa que deseja excluir.
   - A despesa será excluída e removida do sistema.
   - Pressione Enter para voltar ao menu principal.

10. Logout:
   - Ao selecionar essa opção, você fará logout da sua conta e retornará à tela de login.

Observação: O programa utiliza dois arquivos, 'dados.csv' para armazenar informações de login e 'gastos.csv' para armazenar informações sobre as despesas registradas. Certifique-se de que esses arquivos estejam no mesmo diretório do arquivo do programa.

Aproveite o Sistema de Rastreamento de Despesas Pessoais para manter o controle das suas finanças!
