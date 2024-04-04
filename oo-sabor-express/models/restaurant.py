# Classe restaurante criada para definir como serão os restaurantes.
class Restaurant():
    # lista que irá receber todos os restaurantes
    restaurant = []

    # Função construtora do objeto restaurante
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

        # Adcionando os objetos restaurante à nossa lista
        Restaurant.restaurant.append(self)
    
    # Função construtora de uma string do objeto
    def __str__(self):
        return f'{self.name}, {self.category}, {"Ativo" if self.active else "Inativo"}'
    
    # Função para listar todos os restaurantes
    def restaurant_list():
        print("-"*53)
        print(f"{'Nome':<10} | {'Categoria':^30} | {'Status'}")
        print("-"*53)
        
        for index in Restaurant.restaurant:
            print(f'{index.name:<10} | {index.category:^30} | {'Ativo' if index.active else 'Inativo'}')
        

restaurante_comedoria = Restaurant('Comedoria', 'Comida italiana')

restaurante_pan_pop = Restaurant('Pan Pop', 'Restaurante de sanduiches')

Restaurant.restaurant_list()