'''
Para essa segunda versão do sistema bancário (v2), vamos otimizar e aplicar novas implementações:

- criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária;
- criar um decorador de log e estabelecer um limite de 10 transações diárias para a conta, aplicado para todas as funções de transações;
- se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia;
- o decorador de log deve registrar e mostre no extrato, a data e hora de cada transação. 

A função saque deve receber os argumentos apenas por nome (keyword only), por exemplo: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

A função extrato deve receber os argumentos por posição e por nome (positional and keyword). Argumentos posicionais: saldo, argumentos nomeados: extrato.

Os usuários criados (clientes) devem ser armazenados em uma lista, composto por nome, data de nascimento, CPF e endereço. O endereço deve ser uma string e não devemos cadastrar dois usuários com o mesmo CPF e deve ser somente números.

A conta corrente deve ser composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário

Fique a vontade para adicionar mais funções, como por exemplo: listar contas.
'''




