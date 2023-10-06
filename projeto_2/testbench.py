import math

class shapePoint:
  def __init__(self):
      self.x1 = input('Insira a coordenada X do ponto: ')
      self.y1 = input('Insira a coordenada Y do ponto: ')
      
      self.string = (f'- Forma geométrica: Ponto;\n- Localizado em: ({self.x1},{self.y1}).')
      
class shapeLine:
  def __init__(self):
      self.x0 = input('Insira a coordenada X do primeiro ponto da linha: ')
      self.y0 = input('Insira a coordenada Y do primeiro ponto da linha: ')
      self.x1 = input('Insira a coordenada X do segundo ponto da linha: ')
      self.y1 = input('Insira a coordenada Y do segundo ponto da linha: ')
      
      self.base = int(self.x1) - int(self.x0)
      self.altura = int(self.y1) - int(self.y0)
      self.raiz = math.sqrt(self.base**2+self.altura**2)
      
      self.string = (f'- Forma geométrica: Linha;\n- Localizada entre: ({self.x0},{self.y0}) e ({self.x1},{self.y1});\n- Comprimento da linha: {self.raiz} cm.')
      
class shapeSquare:
    def __init__(self):
      self.x1 = input('Insira a coordenada X do quadrado: ')
      self.y1 = input('Insira a coordenada Y do quadrado: ')
      
      self.lado = input('Insira qualquer lado do quadrado em cm: ')
      
      self.lado = int(self.lado)
      self.perimetro = 4*self.lado
      self.area = self.lado**2
      
      self.string = (f'- Forma geométrica: Quadrado;\n- Localizado em: ({self.x1},{self.y1});\n- Perímetro do quadrado: {self.perimetro} cm;\n- Área do quadrado: {self.area} cm.')

class shapeRectangle:
  def __init__(self):
    self.x1 = input('Insira a coordenada X do retângulo: ')
    self.y1 = input('Insira a coordenada Y do retângulo: ')
    self.altura = input('Insira a altura do retângulo em cm: ')
    self.largura = input('Insira a largura do retângulo em cm: ')
    
    self.perimetro = 2 * (int(self.altura) + int(self.largura))
    self.area = int(self.altura) * int(self.largura)
    
    self.string = (f'- Forma geométrica: Retângulo;\n- Localizado em: ({self.x1},{self.y1});\n- Perímetro do retângulo: {self.perimetro} cm;\n- Área do retângulo: {self.area} cm.')
    
class shapeCircle:
  def __init__(self):
    self.x1 = input('Insira a coordenada X do círculo: ')
    self.y1 = input('Insira a coordenada Y do círculo: ')
    self.raio = input('Insira o raio do círculo em cm: ')
    
    self.perimetro = 2 * 3.14 * int(self.raio)
    self.area = 3.14 * int(self.raio)**2
    
    self.string = (f'- Forma geométrica: Círculo;\n- Localizado em: ({self.x1},{self.y1});\n- Perímetro do círculo: {self.perimetro} cm;\n- Área do círculo: {self.area} cm.')

s1 = shapeCircle()
print(f'\n{s1.string}')
