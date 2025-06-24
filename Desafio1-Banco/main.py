from dataclasses import dataclass
import sys


@dataclass
class Operacao():
    tipo: str 
    valor: float

def extrato():
    print("""
============================
      EXTRATO BANCARIO

          """)
    for _, chaves in extrato.itens():
        print(f"TIPO: {chaves["tipo"]}")
        print(f"VALOR: R${chaves["valor"]}")
    print(f"SALDO: R${saldo}")

def sacar(valor_saque: float) -> str:
    num_saque+=1
    saldo -= valor_saque
    operaction: Operacao = Operacao(tipo="SAQUE", valor=valor_saque)
    extrato.append(operaction)

def depositar(valor_deposito: float) -> str:
    saldo += valor_deposito
    operaction = Operacao(tipo="SAQUE", valor=valor_deposito)
    extrato.append(operaction)

def validacao(result: int, valor: int) -> bool:
    if result == 1:
            if valor > 500:
                print("O valor do saque foi invalido.")
                return False
            return True
    else:
        if valor < 0:
            print("O valor do deposito foi invalido.")
            return False
        return True


def main() -> int:
    while True:
        print("""
===========================
           Menu
1. Sacar
2. Depositar
3. Solicitar Extrato
4. Sair
                """)
        try:
            result: int = input("Selecione sua opção: ")
            match result:
                case 1:
                    if num_saque >= 3:
                        print("Seu limite de saques diarios foi excedido.")
                        continue
                    valor:float = input("Digite o valor do saque: ")
                    
                    if validacao(result, valor):
                        continue

                    sacar(valor)
                case 2:
                    valor:float = input("Digite o valor do deposito: ")

                    if validacao(result, valor):
                        continue

                    depositar(valor)
                case 3:
                    extrato()
                case 4:
                    sys.exit()

        except Exception as e:
            print("Houve um erro. O valor digitado é invalido.", e)
            return 0


if __name__ == "__main__":
    saldo: int
    extrato: list[Operacao]
    num_saque: int

    main()