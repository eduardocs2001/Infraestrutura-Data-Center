from re import A


class base:

    def __init__(self, tempo, valor_kwh):
        self.watts = 1
        self.kw = 1000
        self.horas = tempo
        self.valor = float(valor_kwh)
        self.energia = {}


    def gasto_energia(self):
        while True:
            aparelho = input('Aparelho: ')
            marca = input('Marca: ')
            modelo= input('Modelo: ')
            potencia = float(input('Potencia: '))
            print('--------------------------GASTO DE ENERGIA------------------------')
            potencia = float(potencia)
            e = potencia * self.horas
            valor = e * self.valor
            print(f'Formula: E(kwh) = KW * TEMPO(horas de uso)\nConta: E = {potencia}kw * {self.horas}h = {e}\nResultado: Teremos um custo de R${valor} para manter ativo operando interuptamente pelo periodo de {self.horas}h\n')
            print('------------------------------------------------------------------')
            self.energia[aparelho] = {'Marca' : marca, 'Modelo' : modelo, 'Potencia' : potencia, 'Gasto (Kwh)' : e, 'Gasto (R$)' : valor}
            de = input('Deseja realizar mai um calculo (s)im (n)ão? ')
            if de == 'n':
                for x in self.energia:
                    print(f'\n{x}:')
                    for y in self.energia[x]:
                        print(f"    {y} = {self.energia[x][y]}")

                break
            else:
                pass


calculo = base(720, 0.30)
calculo.gasto_energia()
