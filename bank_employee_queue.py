# Simulação de Fila de Atendimento Bancário - Bank Employee Queue

# Estrutura de clientes na fila
fila = ["Cliente A - Minuta de Demanda", "Cliente B - Depósito em dinheiro", "Cliente C - Retirada de dinheiro", "Cliente D - Depósito em cheque"]

# Simulação de abertura do banco
banco_aberto = True

while banco_aberto:
    if not fila:
        print("Fila vazia. Aguardando novos clientes...")
        # Simulação de encerramento do dia (pra evitar loop infinito aqui)
        banco_aberto = False
    else:
        cliente = fila.pop(0)
        print(f"Atendendo: {cliente}")

        if "Minuta de Demanda" in cliente:
            print("Direcionado para o Contador A.")
        elif "Depósito em dinheiro" in cliente:
            print("Direcionado para o Contador B.")
        elif "Retirada de dinheiro" in cliente:
            print("Direcionado para o Contador C.")
        elif "Depósito em cheque" in cliente:
            print("Direcionado para o Contador D.")
        else:
            print("Serviço não identificado.")

print("Banco fechado. Atendimento encerrado.")
