class TV:
    def __init__(self, volume, canal):
        self.__volume = volume
        self.__canal = canal

    def aumentarVol(self, aumentar):

        while aumentar < 100:
            if self.__volume < 100:
                self.__volume += aumentar
            if aumentar > 100:
                print('Impossível aumentar')
                print(f'O volume está em : {self.__volume}')
                