def ajustes():
        menu_ajustes()
        opcao = int(input("->"))
        while opcao != 0:
                if opcao == 1:
                        global apronte
                        apronte = float(input("Apronte em litros (ex.: 25.0L): "))
                        #menu_ajustes()
                elif opcao == 2:
                        global rendimento
                        rendimento = float(input("Rendimento em % (ex.: 68.0%): "))
                        menu_ajustes()
                elif opcao == 3:
                        print("Apronte: %.2f" % apronte + "L")
                        print("Rendimento: %.2f" % rendimento + "%")
                        menu_ajustes()
                else:
                        print("Opcao errada")
                opcao = int(input("->"))

def menu_ajustes():
        print("AJUSTES")
        print("0-Sair")
        print("1-Ajustar Apronte")
        print("2-Ajustar Rendimento")
        print("3-Exibir")

def extrato():
        menu_extrato()
        opcao = int(input("->"))
        while opcao != 0:
                if opcao == 1:
                        global gu
                        gu = int(input("Gravidade em GU (ex.: 80): "))
                        menu_extrato()
                elif opcao == 2:
                        print("adicionar extrato")
                        menu_extrato()
                elif opcao == 3:
                        guT = gu * apronte
                        kilo = guT / 0.85 / rendimento
                        print("%.2f Kilos de Malte" % kilo)
                        menu_extrato()
                else:
                        print("Opvao errada")
                opcao = int(input("->"))

def menu_extrato():
        print("EXTRATO")
        print("0-Sair")
        print("1-Definir gravidade")
        print("2-Adicionar Extrato")
        print("3-Exibir")
        
