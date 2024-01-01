import copy

if __name__ == "__main__":
    print("Este archivo no se puede utilizar tal cual, es solo el generador, debes importarlo en main.py")
    

class Generadordeescenarios():

    filaconparedes = list("####################")
    filaconlateralesdeparedes = list("#                  #")
    escenario = [  # 10x20
        list(filaconparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconlateralesdeparedes),
        list(filaconparedes)
    ]

    def generarescenario(self):
        return copy.deepcopy(self.escenario)