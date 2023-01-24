class Veiculo:
    def __init__(self, nome, tipo):
        self._nome = nome
        self._tipo = tipo

    def tipoVeiculo(self):
        print(self._tipo)


V2 = Veiculo('Fusca', 'Carro')
V2.tipoVeiculo()

moto = Veiculo('Honda', 'Terrestre')

barco = Veiculo('Barco pequeno', 'Marítimo')
