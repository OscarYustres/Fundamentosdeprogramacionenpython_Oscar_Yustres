import requests
from datetime import datetime

_ENDPOINT = "https://api.binance.com"
nombre_archivo = "tx_prueba.txt"


class Usuario(object):
    def __init__(self, codigo):
     self.codigo = codigo

    def mostrarCodigo(self):
     return self.codigo 

class Criptomoneda(object):
     def __init__(self, nombre, cantidad):
      self.nombre = nombre
      self.cantidad = cantidad
      
     def indicarCantidad(self, cantidad):
      self.cantidad = cantidad

     def mostrarNombre(self):
      return self.nombre

     def mostrarCantidad(self):
      return self.cantidad

     def saldoMoneda(self, cotizacion):
         return self.cantidad*cotizacion

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
  data = requests.get(_url("/api/v3/ticker/price?symbol="+cripto)).json()
  precio = float(data["price"])
  return precio

def validMoneda(cripto):
   criptos = ["BTC","BCC","LTC","ETH"]
   if cripto in criptos:
     return True
   else:
      print("Monedas válidas (BTC,BCC,LTC,ETH)")
      return False

def validCodigo(codigo):
     if codigo == usuario.codigo:
         print("\n ¡TRANSACCIÓN FALLÍDA!, el código indicado es inválido")
         return False
     else:
         return True

def saldoInsuficiente(moneda, cantidad):
 aux = True
 if(moneda== "BTC"):
    if(bit.cantidad >= cantidad):
         return True
    else:
         aux = False
 if(moneda== "ETH"):
    if(ethe.cantidad >= cantidad):
         return True
    else:
         aux = False
 if(moneda== "BCC"):
    if(bcc.cantidad >= cantidad):
        return True
    else:
        aux = False                   
 if(moneda== "LTC"):
    if(ltc.cantidad >= cantidad):
        return True
    else:
        aux = False
 if(aux==False):
     print("  ¡Transaccion rechazada! Cantidad de"+ moneda+ " es insuficiente")
     return False            

def GuardarRegistro(moneda, operacion, codigo, cantidad, cantTotal):
    archivo = open(nombre_archivo,"a")
    dt = datetime.now()
    precio =  get_price(moneda+"USDT")
    archivo.write("\n"+"Fecha"+ ":" + dt.strftime("%A %d/%m/%Y %I:%M:%S%p") +",Moneda" +":"+str(moneda)
        +",Transacción" +":"+ operacion+",Código de usuario"+ ":"+ str(codigo) + ",Cantidad "+ ":"+ str(cantidad) 
            + ",Total de la operación en $"+":"+ str(precio*cantidad) +", Total acumulado en cuenta en $" + ":"+ str(precio*cantTotal))
    archivo.close()
    return

bit = Criptomoneda("BTC",2.5)
ethe = Criptomoneda("ETH",0.6734)
bcc = Criptomoneda("BCC",8.5)
ltc = Criptomoneda("LTC",7.36)
monedas = [bit,ethe,bcc,ltc]
usuario = Usuario(9210)   

while True:
 print("*************////////////////////////////////***************")
 print("             Disfruta de tu billetera virtual")
 print("____________________________________________________________")
 print("Tú código de Usuario es: " + str(usuario.mostrarCodigo()))
 print("Menú de opciones:")
 print(("1. Recibir Cantidad \n"
       "2. Transferir monto\n"
       "3. Mostrar balance de una moneda\n"
       "4. Mostrar balance general\n"
       "5. Mostrar histórico de transacciones\n"
       "6. Salir del programa"))
 seleccion = int(input("Seleccione una opción para continuar: "))

 if(seleccion==1):
     moneda = input("   Ingrese la moneda a recibir: ")
     while not validMoneda(moneda):
             moneda = input("   ingrese la moneda a recibir: ")
     cantidad = float(input("   Ingrese la cantidad a recibir de "+ moneda+ ":"))
     codigo = int(input("  Ingrese el codigo del emisor: "))
     while not validCodigo(codigo):
       codigo = int(input("   Ingrese el codigo del emisor: "))
     if(moneda=="BTC"):
            bit.indicarCantidad(bit.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad, bit.mostrarCantidad())
     elif(moneda=="ETH"):
            ethe.indicarCantidad(ethe.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,ethe.mostrarCantidad())
     elif(moneda=="BCC"):
            bcc.indicarCantidad(bcc.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,bcc.mostrarCantidad())
     elif(moneda=="LTC"):
            ltc.indicarCantidad(ltc.cantidad + cantidad)
            GuardarRegistro(moneda,"Recibido",codigo, cantidad,ltc.mostrarCantidad())
     print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue añadido correctamente a su billetera")                   
 
 elif(seleccion==2):
     moneda = input("Ingrese la moneda a transferir: ")
     while not validMoneda(moneda):
         moneda = input("Ingrese la moneda a transferir: ")
     cantidad = float(input(" Ingrese la cantidad a transferir de "+ moneda+ ":"))
     while not saldoInsuficiente(moneda, cantidad):
         cantidad = float(input(" Ingrese la cantidad a transferir de "+ moneda+ ":"))
     codigo = int(input("  Ingrese el codigo del emisor: "))
     while not validCodigo(codigo):
       codigo = int(input("   Ingrese el codigo del emisor: "))
     if(moneda=="BTC"):
            bit.indicarCantidad(bit.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad, bit.mostrarCantidad())
     elif(moneda=="ETH"):
            ethe.indicarCantidad(ethe.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad,ethe.mostrarCantidad())
     elif(moneda=="BCC"):
            bcc.indicarCantidad(bcc.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad,bcc.mostrarCantidad())
     elif(moneda=="LTC"):
            ltc.indicarCantidad(ltc.cantidad - cantidad)
            GuardarRegistro(moneda,"Enviado",codigo, cantidad,ltc.mostrarCantidad())
     print("\n       ¡TRANSACCIÓN EXITOSA!, monto fue descontado correctamente de su billetera")   

 elif(seleccion==3):
        moneda = input("    Ingrese la moneda a consultar: ")
        while not validMoneda(moneda):
            moneda = input("    Ingrese la moneda a consultar: ")
        precio = get_price(moneda+"USDT")
        if(moneda=="BTC"):
            print("Moneda: " + moneda + " Cantidad: "+ str(bit.mostrarCantidad()) +" Saldo disponible: $."+ str(bit.saldoMoneda(precio)))
        elif(moneda=="ETH"):
             print("Moneda: " + moneda + " Cantidad: "+str(ethe.mostrarCantidad()) +" Saldo disponible: $."+str(ethe.saldoMoneda(precio)))
        elif(moneda=="BCC"):
             print("Moneda: " + moneda + " Cantidad: "+str(bcc.mostrarCantidad()) + " Saldo disponible: $."+str(bcc.saldoMoneda(precio)))
        elif(moneda=="LTC"):
             print("Moneda: " + moneda + " Cantidad: "+ str(ltc.mostrarCantidad()) +" Saldo disponible: $."+str(ltc.saldoMoneda(precio)))

 elif(seleccion==4):
        moneda = ""
        totalUSD = 0
        for moneda in monedas:
            precio = get_price(moneda.mostrarNombre()+"USDT")
            totalUSD += moneda.saldoMoneda(precio)
            print("Moneda: " + moneda.mostrarNombre() + " Cantidad: "+ str(moneda.mostrarCantidad()) +" Saldo disponible: $."+ str(moneda.saldoMoneda(precio)) +"\n")
        print("El monto acumulado total de todas las criptomonedas es $." + str(totalUSD))            
 
 elif(seleccion==5):
        archivo = open(nombre_archivo,"r")
        texto = archivo.read()
        archivo.close()
        lineas = texto.splitlines()
        print(texto)
 elif(seleccion==6):
   print("\n  Gracias por usar tu billetera virtual.") 
   break
 else:
    print("\nPor favor, selecciona una opción válida")