from model.controladorP import Personas

class controladorN:
    def __init__(self):
        self.id = 0
    def getIncrementar(self)->int:
        self.id = self.id +1
        return self.id

    def aggregarNotaP(self,Personas:Personas):
        newDescrip = input("ingrese la descripcion de la nota: ").lstrip
        newNota = Nota(newDescrip)
        newNota.id = self.getIncrementar()
        Personas.notas.append(newNota)
        print("Nota agregada correctamente")
        wait()

    def listarNota(self,persona:Personas):
        if len(personas.notas)>0:
            for nota in persona.notas:
                nota.printInformation()
        else:
            print("No hay notas en el sistema")
        wait()
    
    def findId(self,id:int,persona:Personas)->Nota:
        if self.countNota(persona)>0:
            for nota in persona.notas:
                if int(nota.id) == id:
                    return nota
        return None

        def modificarNota(self,persona:Personas)->Nota:
            if self.countNota(persona)>0:
                idNot = input("ingrese la Id de la nota: ")
                while not(idNota.isnumeric()) or idNote==" ":
                    idNota = input("ID no valida, por favor intentelo nuevamente")
                    if idNota == "":
                        return
                    elif idNota.isnumeric():
                        notaFound = self.findId(int(idNota),persona)
                newDescrip = input ("ingrese la descripcion de la nota: ")
                if newDescrip == "":
                    newDescrip = notaFound.desNota
                if newDescrip == notaFound.desNota:
                    print("los datos son los mimos que antes")
                else:
                    notaFound.desNota = newDescrip
                    print("Nota modificada correctamente. ")
            else:
                print("No existen registro de notas")
            wait()
                        
