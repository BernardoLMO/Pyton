from restaurante import Restaurante

restaurante_catatau = Restaurante('catatau', 'Gourmet')
restaurante_mexicano = Restaurante('aiaiai', 'Mexicano')
restaurante_gonas = Restaurante('EoGonasFi', 'Japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()