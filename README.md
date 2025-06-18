# Bank Employee - Customer Queue Simulation 

Projeto simples que simula o fluxo de atendimento em um banco, onde clientes entram na fila e são atendidos de acordo com o tipo de serviço solicitado.

---

## Cenário do problema:

- O banco abre às 6h da manhã.
- Inicialmente, a fila está vazia.
- Durante o expediente, os clientes entram na fila com um dos seguintes tipos de pedidos:

1. Depósito em dinheiro
2. Retirada de dinheiro
3. Depósito em cheque
4. Minuta de Demanda (Demand Draft)

---

## Lógica aplicada:

1. Verificar se o banco está aberto.
2. Enquanto o banco estiver aberto:
   - Se a fila estiver vazia, aguardar novos clientes.
   - Se houver clientes, processar cada um conforme o tipo de solicitação.
3. Direcionar o cliente para o contador correto:
   - **Minuta de Demanda → Contador A**
   - **Depósito em dinheiro → Contador B**
   - **Retirada de dinheiro → Contador C**
   - **Depósito em cheque → Contador D**
4. Após finalizar a fila, o banco fecha.

---

## Exemplo de execução:

**Fila inicial:**

- Cliente A - Minuta de Demanda
- Cliente B - Depósito em dinheiro
- Cliente C - Retirada de dinheiro
- Cliente D - Depósito em cheque

**Saída esperada:**

Atendendo: Cliente A - Minuta de Demanda
Direcionado para o Contador A.

Atendendo: Cliente B - Depósito em dinheiro
Direcionado para o Contador B.

Atendendo: Cliente C - Retirada de dinheiro
Direcionado para o Contador C.

Atendendo: Cliente D - Depósito em cheque
Direcionado para o Contador D.

Banco fechado. Atendimento encerrado.

---

## Motivação:

Esse projeto foi desenvolvido como parte dos meus estudos de **Lógica de Programação**, dentro do curso **Coding Essentials – Logic Building for Beginners (Udemy)**.

Meu objetivo foi treinar:

- Uso de **filas**
- Estruturas de repetição (`while`)
- Estruturas condicionais (`if...else`)

---

## Tecnologias usadas:

- Python 3.x

---

## Sobre mim:

Sou André Ricardo, estudante em transição de carreira para a área de Tecnologia da Informação.  
Atualmente focado em aprender **lógica de programação**, **Python**, **Inteligência Artificial** e também explorando hobbies como **montagem de hardware**.

