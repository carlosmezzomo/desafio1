Sistema Bancário em Python
Este projeto implementa um sistema bancário simples em Python com as operações de depósito, saque e extrato. Ele foi desenvolvido como parte de um desafio para criar uma aplicação de banco moderna e funcional. Atualmente, a aplicação atende a apenas um usuário, e não é necessário identificar o número de agência ou conta bancária.

Funcionalidades
1. Depósito
O usuário pode realizar depósitos de valores positivos.
Todos os depósitos são armazenados e exibidos no extrato.
2. Saque
Limite de 3 saques diários.
O valor máximo permitido por saque é de R$ 500,00.
O sistema verifica se há saldo suficiente para realizar o saque.
Saques realizados são exibidos no extrato.
3. Extrato
Exibe a lista completa de todas as transações (depósitos e saques).
No final, é mostrado o saldo atual da conta.
Caso não haja movimentações, o sistema exibe a mensagem: "Não foram realizadas movimentações."
