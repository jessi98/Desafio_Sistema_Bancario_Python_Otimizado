# Sistema Bancário Simples - Etapa 2

Este projeto implementa um sistema bancário simples com funcionalidades básicas, focado em modularização e inclusão de novos recursos.

---

## Funcionalidades

- **Menu interativo** com as seguintes opções:
  - [1] Depositar
  - [2] Sacar
  - [3] Extrato
  - [4] Nova Conta
  - [5] Listar Contas
  - [6] Novo Usuário
  - [0] Sair

- **Depósito e saque** com validação de valores, limite por saque e limite diário de saques.
- **Extrato** exibindo o histórico das movimentações e saldo atual.
- **Cadastro de usuários** com dados pessoais (nome, CPF, data de nascimento, endereço).
- **Criação de contas bancárias** vinculadas aos usuários cadastrados.
- **Listagem de contas** cadastradas com detalhes (agência, número da conta e titular).

---

## Estrutura do Código

- Uso de funções para organizar cada operação, como `deposito()`, `saque()`, `criar_usuario()`, `criar_cc()`, entre outras.
- Função `menu()` para exibir o menu e receber a escolha do usuário.
- Função `filtrar_usuarios()` para buscar usuários pelo CPF e evitar duplicidade.
- Uso de listas para armazenar múltiplos usuários e contas em memória.
- Função principal `main()` controla o fluxo do programa e mantém as variáveis de estado.
