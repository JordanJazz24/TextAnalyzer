import re
from identifier import Symbol, Function
from dataStruct import SymbolTable


class TextAnalyzer:
    def __init__(self):
        self.table = SymbolTable.SymbolTable()
        self.types = ['void', 'int', 'float', 'string']


    # Métodos relacionados con la creación de la table de símbolos
    def create_table(self):
        contador = 0
        cuerpo = ""
        booleana = bool(0)
        contador2 = 0

        with open("code/codigo.txt", "r") as f:
            for linea in f:
                if self.isFunction(linea) is True:
                     nombre = linea.split(' ')[1].strip()
                     contador = contador + 1
                     cuerpo = ""
                     for linea2 in f:
                         if linea2 != ' ':
                            x = re.search('\\{',linea2)
                            y = re.search('\\}',linea2)
                            if(x):
                                z = re.search(nombre,linea2)
                                if (z):
                                    contador = contador + 1
                                    contador2 = contador2 + 1
                                else:
                                    if(self.bodyFunction(linea) == True):
                                        x1 = 3
                                        while x1 < linea.count(" ") - 1:
                                            if  linea.split(' ')[x1].strip() != ',':
                                                tipoV = linea.split(' ')[x1].strip()
                                            if  linea.split(' ')[x1+1].strip() != ',':
                                                nombreV = linea.split(' ')[x1+1].strip()
                                            variable = Symbol.Symbol(tipoV, nombreV, None, "local", self.getLine(linea2))
                                            self.table.add_symbol(nombreV, variable)
                                            x1 = x1 + 3

                                    cuerpo = cuerpo + linea2
                                    contador = contador+1
                                    contador2 = contador2 + 1

                                    for i in range(len(self.types)):
                                        if linea2.split(' ')[0].strip() == self.types[i]:
                                            tipo3 = linea2.split(' ')[0].strip()
                                            nombre3 = linea2.split(' ')[1].strip()
                                            if tipo3 == "int":
                                                valor13 = linea2.split('=')[1].strip()
                                                valor3 = valor13.replace(';','')

                                            variable = Symbol.Symbol(tipo3, nombre3, valor3, "local", self.getLine(linea2))
                                            self.table.add_symbol(nombre3, variable)
                            else:
                                if(y):
                                    contador = contador-1
                                    if(contador == 0):
                                        break
                                    cuerpo = cuerpo + linea2
                                    contador2 = contador2 + 1

                                    for i in range(len(self.types)):
                                        if linea2.split(' ')[0].strip() == self.types[i]:
                                            tipo3 = linea2.split(' ')[0].strip()
                                            nombre3 = linea2.split(' ')[1].strip()
                                            valor13 = linea2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')

                                            variable = Symbol.Symbol(tipo3, nombre3, valor3, "local", self.getLine(linea2))
                                            self.table.add_symbol(nombre3, variable)

                                else:
                                    cuerpo = cuerpo + linea2
                                    contador2 = contador2 + 1

                                    for i in range(len(self.types)):
                                        if linea2.split(' ')[0].strip() == self.types[i]:
                                            tipo3 = linea2.split(' ')[0].strip()
                                            nombre3 = linea2.split(' ')[1].strip()
                                            valor13 = linea2.split('=')[1].strip()
                                            valor3 = valor13.replace(';','')

                                            variable = Symbol.Symbol(tipo3, nombre3, valor3, "local", self.getLine(linea2))
                                            self.table.add_symbol(nombre3, variable)



                     funcion = Function.Function(linea.split(' ')[0].strip(), nombre, cuerpo, self.getLine(linea2))
                     self.table.add_symbol(nombre, funcion)

                else:
                    if(contador2 == 0):
                        if linea.count(" ") == 2:
                             nombre = linea.split(' ')[0].strip()
                             valor1 = linea.split('=')[1].strip()
                             valor = valor1.replace(';','')

                             variable = Symbol.Symbol(None, nombre, valor, "global", self.getLine(linea))
                             self.table.add_symbol(nombre, variable)
                        else:
                            tipo = linea.split(' ')[0].strip()
                            nombre = linea.split(' ')[1].strip()
                            valor1 = linea.split('=')[1].strip()
                            valor = valor1.replace(';','')

                            variable = Symbol.Symbol(tipo, nombre, valor, "global", self.getLine(linea))
                            self.table.add_symbol(nombre, variable)
                    elif linea.count(" ") == 3:
                        tipo = linea.split(' ')[0].strip()
                        nombre = linea.split(' ')[1].strip()
                        valor1 = linea.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        variable = Symbol.Symbol(tipo, nombre, valor, "global", self.getLine(linea))
                        self.table.add_symbol(nombre, variable)
                    elif linea.count(" ") == 2:
                        nombre = linea.split(' ')[0].strip()
                        valor1 = linea.split('=')[1].strip()
                        valor = valor1.replace(';','')

                        variable = Symbol.Symbol(None, nombre, valor, "global", self.getLine(linea))
                        self.table.add_symbol(nombre, variable)
    def isFunction(self, linea):
        y = re.search('\\(', linea)
        if (y):
            return True
        else:
            return False
    def bodyFunction(self, linea):
        x = re.search('\\(' '\\)', linea)

        if x:
            return False
        return True
    def getLine(self, lineaAbuscar):
        contador = 1
        with open("code/codigo.txt", "r") as f:
            for linea in f:
                if linea == lineaAbuscar:
                    return contador
                contador = contador + 1

    #------------------------------------------------------

    # Métodos relacionados con la impresión y busqueda de la table de símbolos

    def buscar(self,num):
        return self.table.find_Symbol(num)

    def printCode(self):
        with open("code/codigo.txt", "r") as file:
            for line_number, line in enumerate(file, start=1):
                print(line_number, line, end='')
        print()

    def inTable(self, variable):
        if self.table.find_Symbol(variable) != None:
            return True
        return False

    #------------------------------------------------------

    # Métodos relacionados con la validación de tipos y error
    def isFloat(self, variable):
        try:
             float(variable)
             return True
        except:
             return False

    def dataType(self, tipo):
        switch = {
            "int": int,
            "string": str,
            "float": float,
            "void": None}
        return switch.get(tipo, None)

    def isWhileIf(self, linea):
        x = re.search('if',linea)
        y = re.search('while',linea)

        if x or y:
            return True
        return False

    def isInt(self, variable):
        try:
            int(variable)
            return True
        except:
            return False

    import re

    def bodyError(self):
        with open("code/codigo.txt", "r") as f:
            for line1 in f:
                if self.isFunction(line1) and not self.isWhileIf(line1):
                    name = line1.split(' ')[1].strip()
                    body = self.table.find_Symbol(name).get_body()

                    counter = body.count('\n')

                    for linea2 in f:
                        if linea2 != ' ':
                            tipo = self.table.find_Symbol(name).get_return_type()
                            x = re.search('return', body)

                            if x and tipo == "void" and not counter:
                                print(f"Error – Linea {self.getLine(linea2)}: 'return' no valido en funciones void")
                                counter += 1

                            if linea2.split(' ')[0].strip() == "return":
                                nombreV1 = linea2.split(' ')[1].strip().replace(';', '')
                                if self.inTable(nombreV1):
                                    tipoV = self.table.find_Symbol(nombreV1).get_type()

                                    if tipoV is None:
                                        print(
                                            f"Error – Linea {self.getLine(linea2) + counter}: La variable {self.table.find_Symbol(nombreV1).get_name()} no está declarada")
                                    elif tipoV != tipo:
                                        print(
                                            f"Error – Linea {self.getLine(linea2)}: Valor de retorno no coincide con la declaracion de la funcion")
                                else:
                                    if not (self.isInt(nombreV1) or self.isFloat(nombreV1)):
                                        if tipo != "string":
                                            print(
                                                f"Error – Linea {self.getLine(linea2)}: Valor de retorno no coincide con la declaracion de la funcion")

                                    if self.isInt(nombreV1) or self.isFloat(nombreV1):
                                        if tipo not in ["int", "float"]:
                                            print(
                                                f"Error – Linea {self.getLine(linea2)}: Valor de retorno no coincide con la declaracion de la funcion")

                            if linea2.count(" ") == 2:
                                conta = 0
                                nombreV2 = linea2.split(' ')[0].strip()
                                valor12 = linea2.split('=')[1].strip().replace(';', '')
                                if self.isInt(valor12) and not conta:
                                    if self.table.find_Symbol(nombreV2).get_type() != "int":
                                        print(
                                            f"Error – Linea {self.getLine(linea2)}: Error asignacion en la variable: '{self.table.find_Symbol(nombreV2).get_name()}")
                                        conta += 1

                                if self.isFloat(valor12) and self.table.find_Symbol(
                                        nombreV2).get_scope() == "local" and not conta:
                                    if self.table.find_Symbol(nombreV2).get_type() != "float":
                                        print(
                                            f"Error – Linea {self.getLine(linea2)}: Error asignacion en la variable: {self.table.find_Symbol(nombreV2).get_name()}")
                                        conta += 1

                                if not (self.isFloat(valor12) or self.isInt(valor12)):
                                    if self.table.find_Symbol(nombreV2).get_type() != "string":
                                        print(
                                            f"Error – Linea {self.getLine(linea2)}: Error asignacion en la variable: {self.table.find_Symbol(nombreV2).get_name()}")
                                conta = 0

                            nombreParametro = ""
                            if self.isWhileIf(linea2):
                                nombreParametro = linea2.split(' ')[2].strip()
                                if not self.table.find_Symbol(nombreParametro):
                                    print(
                                        f"Error – Linea {self.getLine(linea2)}: La variable {nombreParametro} no está declarada")

    def errorAsignacion(self):
        with open("code/codigo.txt", "r") as f:
            for linea in f:
                if self.isFunction(linea) and not self.isWhileIf(linea):
                    self.checkReturnType(linea)
                else:
                    if linea.count(" ") == 3:
                        self.checkVariableAssignment(linea)
                    elif linea.count(" ") == 2:
                        self.checkVariableDeclaration(linea)

    def checkReturnType(self, linea):
        nombre = linea.split(' ')[1].strip()
        type_match_count = sum(1 for t in self.types if self.table.find_Symbol(nombre).get_return_type() != t)

        if type_match_count == len(self.types):
            print(
                f"Error – Linea {self.getLine(linea)}: Tipo de dato {self.table.find_Symbol(nombre).get_type()} no valido")

    def checkVariableAssignment(self, linea):
        nombre = linea.split(' ')[1].strip()
        type_match_count = sum(1 for t in self.types if self.table.find_Symbol(nombre).get_type() != t)

        if type_match_count == len(self.types):
            if self.table.find_Symbol(nombre).get_type() is not None:
                print(
                    f"Error – Linea {self.getLine(linea)}: Tipo de dato {self.table.find_Symbol(nombre).get_type()} no valido")
            else:
                print(
                    f"Error – Linea {self.getLine(linea)}: La variable {self.table.find_Symbol(nombre).get_name()} no está declarada")

        self.checkValueAssignment(linea, nombre)

    def checkVariableDeclaration(self, linea):
        nombre = linea.split(' ')[0].strip()
        type_match_count = sum(1 for t in self.types if self.table.find_Symbol(nombre).get_type() != t)

        if type_match_count == len(self.types):
            if self.table.find_Symbol(nombre).get_type() is not None:
                print(
                    f"Error – Linea {self.getLine(linea)}: Tipo de dato {self.table.find_Symbol(nombre).get_type()} no valido")
            else:
                print(
                    f"Error – Linea {self.getLine(linea)}: La variable {self.table.find_Symbol(nombre).get_name()} no está declarada")

    def checkValueAssignment(self, linea, nombre):
        if self.table.find_Symbol(nombre).get_value().isdigit():
            self.checkNumericAssignment(linea, nombre)
        else:
            self.checkNonNumericAssignment(linea, nombre)

    def checkNumericAssignment(self, linea, nombre):
        if self.dataType(self.table.find_Symbol(nombre).get_type()) not in [int, float]:
            print(
                f"Error – Linea {self.getLine(linea)}: Error asignacion en la variable: {self.table.find_Symbol(nombre).get_name()}")

    def checkNonNumericAssignment(self, linea, nombre):
        if self.isFloat(self.table.find_Symbol(nombre).get_value()) or self.isInt(
                self.table.find_Symbol(nombre).get_value()):
            if self.dataType(self.table.find_Symbol(nombre).get_type()) not in ["int", "float"]:
                print(
                    f"Error – Linea {self.getLine(linea)}: Error asignacion en la variable: {self.table.find_Symbol(nombre).get_name()}")
        elif self.inTable(self.table.find_Symbol(nombre).get_value()):
            assigned_type = self.table.find_Symbol(self.table.find_Symbol(nombre).get_value()).get_type()
            if assigned_type != self.table.find_Symbol(nombre).get_type() and self.dataType(
                    self.table.find_Symbol(nombre).get_type()) != str:
                print(
                    f"Error – Linea {self.getLine(linea)}: Error asignacion en la variable: {self.table.find_Symbol(nombre).get_name()}")
        elif self.dataType(self.table.find_Symbol(nombre).get_type()) != str:
            print(
                f"Error – Linea {self.getLine(linea)}: Error asignacion en la variable: {self.table.find_Symbol(nombre).get_name()}")

    def run (self):
        self.printCode()
        self.create_table()
        self.errorAsignacion()
        self.bodyError()



if __name__ == '__main__':
    TextAnalyzer().run()

