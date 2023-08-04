'''
celular1_marca = "samsumg"
celular2_marca = "apple"
celular3_marca = 'huawei'

celular1_modelo = "galaxy s10"
celular2_modelo = "iphone 11"
celular3_modelo = 'p30 pro'

celular1_camaraF = '12mpx'
celular2_camaraF = '19mpx'
celular3_camaraF = '24mpx'

celular1_camaraT = '120mpx'
celular2_camaraT = '25mpx'
celular3_camaraT = '45mpx'


celulares = []
'''

# usando la clases POO ⭐


class Celular:
    def __init__(self, marca, modelo, camaraF, camaraT):
        self.marca = marca
        self.modelo = modelo
        self.camaraF = camaraF
        self.camaraT = camaraT
        print('se creo un celular nuevo')

    def llamar(self):
        print('llamando desde', self.modelo)

    def cortar(self):
        print('cortando desde', self.modelo)


celuar1 = Celular('samsumg', 'galaxy s10', '12mpx', '120mpx')
celuar2 = Celular('apple', 'iphone 11', '19mpx', '25mpx')
celuar3 = Celular('huawei', 'p30 pro', '24mpx', '45mpx')
print(celuar1.modelo)
print(celuar2.modelo)
print(celuar3.modelo)
print(celuar1.llamar())
