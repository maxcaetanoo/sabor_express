from models.evaluation import Evaluation

# Classe restaurante criada para definir como serão os restaurantes.
class Restaurant():
    # lista que irá receber todos os restaurantes
    restaurant = []

    # Função construtora do objeto restaurante
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.title()#capitalize()
        self._active = False
        self._evaluation = []

        #Diferenças entre title e capitalize:
        #title() = todas as primeiras letras maiusculas ex: Casa Grande
        #capitalize() = apenas a primeira letra da primeira palavra maiuscula ex: Casa grande

        # Adcionando os objetos restaurante à nossa lista
        Restaurant.restaurant.append(self)
    
    # Função construtora de uma string do objeto
    def __str__(self):
        return f'{self._name}, {self._category}, {"Ativo" if self.active else "Inativo"}'
    
    # Função para listar todos os restaurantes
    @classmethod #Define o metodo que acessa a classe
    def restaurant_list(cls):
        print("-"*65)
        print(f"|{'Nome'.ljust(20)} | {'Categoria'.ljust(30)} | {'Status'.ljust(7)}|")
        print("-"*65)
        
        for index in cls.restaurant:
            print(f'|{index._name.ljust(20)} | {index._category.ljust(30)} | {index.active:^7}|')
        print("-"*65)
    
    #Metodo que define como será apresentada a propriedade 'active'
    @property
    def active(self):
        return '☑' if self._active else '☐'
    
    #Metodo para alternar o status de um objeto
    def alternate_status(self):
        self._active = not self._active
    
    #Metodo para receber avaliações
    def recive_evaluations(self, evaluator, assessment):
        evaluation = Evaluation(evaluator, assessment)
        self._evaluation.append(evaluation)

        
# #Objetos restaurantes sendo criados
# restaurante_comedoria = Restaurant('Comedoria', 'Restaurante de massas')
# restaurante_pan_pop = Restaurant('Pan Pop', 'Restaurante de sanduiches')
# restaurante_sushi_sing = Restaurant('sushi sing', 'Restaurante de sushi')

# #Existem duas formar de usar o metodo alternate_status, diretamente através do objeto ou através da classe
# restaurante_sushi_sing.alternate_status() #Objeto
# Restaurant.alternate_status(restaurante_pan_pop) #Classe

# Restaurant.restaurant_list()