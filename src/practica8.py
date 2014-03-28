#!/usr/bin/python

import sys
import moduloerror

argumentos = sys.argv[1:]

#Si se introducen los argumentos ocurre esto

if (len(argumentos) == 8):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float (argumentos[i]))
    nombre_fichero = argumentos[7]
 
 
else:
  n = int (raw_input ());
  print "Introduzca el numero de aproximaciones:"
  aproximaciones = int (raw_input ());
  print "Introduzca 5 umbrales de error:"
  umbral = []
  for i in range (5):
   print "Introduzca el umbral", i, ":"
   umbral.append(float (raw_input ()));
  print "Introduzca el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input ();
  
if(n>0): 
  fichero=open(nombre_fichero,"w")
  fichero.write ("Nº de intervalos: %d\n" % (aproximaciones))
 for i in range (5):
   porcentaje = moduloerror.error (n, aproximaciones, umbral[i])
   fichero.write ("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje, umbral[i]))
 fichero.close ()
else:
  print "El valor de los intervalos debe ser mayor que 0"

  

