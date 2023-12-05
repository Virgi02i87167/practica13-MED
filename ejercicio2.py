from collections import deque

class Banco:
    def __init__(self):
        self.cola_clientes = deque()

    def llegada_cliente(self, cliente):
        print(f"Cliente {cliente} ha llegado al banco.")
        self.cola_clientes.append(cliente)

    def atender_clientes(self):
        while self.cola_clientes:
            cliente_actual = self.cola_clientes.popleft()
            print(f"Atendiendo al cliente {cliente_actual}")

if __name__ == "__main__":
    banco = Banco()

    banco.llegada_cliente(1)
    banco.llegada_cliente(2)
    banco.llegada_cliente(3)
    banco.atender_clientes()
