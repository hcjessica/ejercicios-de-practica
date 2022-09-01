def encenderVela(statusEncendido):
  if(statusEncendido == 0):
    print("No hacer nada");
  else:
    print("Buscar fósforo");
    print("Encender vela");


#encenderVela(1);

def cuentaRegresiva(cantidadSegundos):
  while(cantidadSegundos > 0):
    print("numero: " + str(cantidadSegundos))
    cantidadSegundos-=1
    
#cuentaRegresiva(5)

def entrarTienda(statusPuerta):
  if(statusPuerta == 0):
    print("Abrir puerta");
  else:
    print("Entrar defrente a la tienda");


#entrarTienda(0);

def compraZapato(opcion, talla):
  talla_sandalias = {30,35,38,40};
  talla_zapatillas = {40,39,38,36};
  statusDisponible = 0;
  
  if (opcion == "sandalias"):
    print("Se eligió sandalias");
    for ts in talla_sandalias:
      if(ts == talla):
        statusDisponible = 1;
        break;
  elif(opcion == "zapatillas"):
    print("Se eligió zapatillas");
    for tz in talla_zapatillas:
      if(tz == talla):
        statusDisponible = 1;
        break;

  if(statusDisponible) == 1:
    print("Talla disponible");
  else:
    print("Talla no disponible");

#compraZapato("zapatillas", 42)

def validarMayorEdad(edad):
  if(edad >= 18):
    print("Mayor de edad");
  else:
    print("Es menor de edad");

#validarMayorEdad(17);
    
    
