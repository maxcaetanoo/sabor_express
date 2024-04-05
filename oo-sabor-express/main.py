from models.restaurant import Restaurant

restaurante_comedoria = Restaurant('Comedoria', 'Restaurante de massas')
restaurante_pan_pop = Restaurant('Pan Pop', 'Restaurante de sanduiches')
restaurante_sushi_sing = Restaurant('sushi sing', 'Restaurante de sushi')

restaurante_sushi_sing.alternate_status()

def main():
    Restaurant.restaurant_list()

if __name__ == '__main__':
    main()