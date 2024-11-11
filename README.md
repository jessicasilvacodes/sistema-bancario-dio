## "Criando um Sistema Bancário com Python"

### Desafio do bootcamp "NTT DATA - Engenharia de Dados com Python" da [DIO (Digital Innovation One)](https://web.dio.me/home)

Contexto:

Um grande banco deseja modernizar suas operações e desenvolver seu novo sistema na linguagem Python.

Para a *primeira versão do sistema (v1)*, devemos implementar as seguintes operações: depósito, saque e extrato.

Nas operações de depósito, deve ser possível depositar valores positivos. A v1 do projeto trabalha apenas com 1 usuário, dessa forma, por enquanto, não precisaremos nos preocupar com identificador pessoal, número de agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque. Caso o usuário não tenha dinheiro em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

As operações de extrato devem listar todos os depósitos e saques realizados na conta. No fim da listagem, deve ser exibido o saldo atual. Os valores devem ser exibidos no formato: R$xxxx.xx

Para essa *segunda versão do sistema bancário (v2)*, vamos otimizar e aplicar duas novas funções, uma para cadastrar usuário (cliente) e outra para cadastrar conta bancária, devemos criar um decorador de log e estabelecer um limite de 10 transações diárias para a conta, aplicado para todas as funções de transações, e se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.

O decorador de log também deve registrar e mostrar no extrato, a data e hora de cada transação.

A função saque deve receber os argumentos apenas por nome (keyword only), por exemplo: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

A função extrato deve receber os argumentos por posição e por nome (positional and keyword). Argumentos posicionais: saldo, argumentos nomeados: extrato.

Os usuários criados (clientes) devem ser armazenados em uma lista, composto por nome, data de nascimento, CPF e endereço. O endereço deve ser uma string e não devemos cadastrar dois usuários com o mesmo CPF e deve ser somente números.

A conta corrente deve ser composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário

Já na *terceira versão do sistema bancário (v3)*, devemos iniciar a modelagem do sistema em POO (Programação Orientada a Objetos), e serão adicionadas classes para os clientes e para as operações básicas, depósitos e saques.

O sistema será atualizado para armazenar os dados de clientes e contas bancárias em objetos, ao invés de dicionários.

...
em andamento...
...


Desafio realizado por [Jessica Silva](https://www.linkedin.com/in/sdsjessica/), em 2024.

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jessicasilvacodes)
