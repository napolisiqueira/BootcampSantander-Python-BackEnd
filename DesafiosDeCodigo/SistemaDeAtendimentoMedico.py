def ordenar_por_idade_desc(dicionario: dict) -> dict:
    return dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))


def classificar_pacientes(pacientes: list[tuple[str, int, str]]) -> list[str]:
    grupos = {"maxima": {}, "urgente": {}, "idosos": {}, "normal": {}}

    for nome, idade, status in pacientes:
        if status == "urgente" and idade >= 60:
            grupos["maxima"][nome] = idade
        elif status == "urgente":
            grupos["urgente"][nome] = idade
        elif idade >= 60:
            grupos["idosos"][nome] = idade
        else:
            grupos["normal"][nome] = idade

    for chave in grupos:
        grupos[chave] = ordenar_por_idade_desc(grupos[chave])

    fila = (
        list(grupos["maxima"].keys()) +
        list(grupos["urgente"].keys()) +
        list(grupos["idosos"].keys()) +
        list(grupos["normal"].keys())
    )

    return fila


# Entrada
n = int(input().strip())
pacientes = [tuple(input().strip().split(", ")) for _ in range(n)]
pacientes = [(nome, int(idade), status) for nome, idade, status in pacientes]

# Saída
fila = classificar_pacientes(pacientes)
print(f"Ordem de Atendimento: {', '.join(fila)}")
