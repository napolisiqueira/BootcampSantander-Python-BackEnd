def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # TODO: Crie o processamento das reservas:
    
    confirmadas = []
    recusadas = []
    
    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos: 
    for i in reservas_solicitadas:
        if i in quartos_disponiveis:
          confirmadas.append(i)
        else:
          recusadas.append(i)

    

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(list(map(str, confirmadas))))
    print("Reservas recusadas:", " ".join(list(map(str, recusadas))))

# Chamada da função principal
processar_reservas()