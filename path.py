import os
print("ruta a afegir al PATH?, ha de ser una subcarpeta del directori HOME de l'usuari actiu")
ruta = input()
path = "$HOME/" + ruta + ":" + os.environ['PATH']
fitxer = ".profile"
if os.access(fitxer, os.W_OK):
	with open(fitxer,"a") as f:
		f.write("PATH=" + path +'\n')
		f.close()
		print("PATH actualitzat!")
else:
	print("fitxer sense accés de lectura")
