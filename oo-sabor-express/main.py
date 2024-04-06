from models.restaurant import Restaurant

restaurante_comedoria = Restaurant('Comedoria', 'Restaurante de massas')
restaurante_comedoria.recive_evaluations('Max', 10)
restaurante_comedoria.recive_evaluations('Mile', 8)
restaurante_comedoria.recive_evaluations('Gui', 5)

def main():
    Restaurant.restaurant_list()

if __name__ == '__main__':
    main()