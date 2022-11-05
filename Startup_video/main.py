#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORTS
import os, sys, random, subprocess

title ="───────────────────────────────────────────────────────────────────\n"
title+="█▀█ ▄▀█ █▄ █ █▀▄ █▀█ █▀▄▀█   █▀ ▀█▀ ▄▀█ █▀█ ▀█▀   █ █ █ █▀▄ █▀▀ █▀█\n"
title+="█▀▄ █▀█ █ ▀█ █▄▀ █▄█ █ ▀ █   ▄█  █  █▀█ █▀▄  █    ▀▄▀ █ █▄▀ ██▄ █▄█\n"
title+="───────────────────────────────────────────────────────────────────\n"

# PATHS
if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"VID")):
	DIN=os.path.join(os.path.dirname(os.path.abspath(__file__)),"VID")
else:
	sys.exit("❌ No se ha encontrado el directorio VID, donde estará el video o videos a establecer.")
DOUT=r"/home/deck/.steam/root/config/uioverrides/movies"
FOUT=os.path.join(DOUT, "deck_startup.webm")

def first_time():
	if not os.path.isdir(DOUT):
		try:
			subprocess.getoutput("mkdir -p /home/deck/.steam/root/config/uioverrides/movies")
			print(f"✅ Se ha creado la ruta correctamente.\n * Este mensaje solo sale si el directorio no existe.\n · {DOUT}\n")
		except:
			sys.exit("❌ Error al crear el directorio.\n· {DOUT}")
def randomice(FILES):
	# RANDOM FILE
	while True:
		vid=random.choice(FILES)
		if os.path.splitext(vid)[1]==".webm":
			return vid
def set_video(vid):
	# COPY VIDEO
	try:
		print(os.path.join(DIN,vid),FOUT)
		process=subprocess.getoutput(f"cp {os.path.join(DIN,vid)} {FOUT}")
		print(process)
		print(f"✅ Video de arranque cambiado.\n · {vid}")
	except e:
		print("❌ Error al mover el nuevo video.")
def del_video():
	msg="───────────────────────────────────────────────────────────────────\n"
	msg+="Se va a elimiar el video de arranque.\n"
	msg+="Esta opción no deshabilita el servicio.\n"
	msg+="Si lo tenías activo recuerda usar también la opción (4).\n"
	msg+="───────────────────────────────────────────────────────────────────\n"
	print(msg)
	
	subprocess.getoutput(f'rm {os.path.join(DOUT,"deck_startup.webm")}')
	subprocess.getoutput(f"rmdir {DOUT}")
	subprocess.getoutput(f"rmdir /home/deck/.steam/root/config/uioverrides/")
	
	print("✅ Se ha eliminado el video de arraque.")
def endes_service(opt):
	if opt==True:
		msg="───────────────────────────────────────────────────────────────────\n"
		msg+="Esta opción establece el script en el inicio del sistema,\n"
		msg+="para que cada vez que se reinice la Steam Deck, aparezca un \n"
		msg+="video aleatorio de la carpeta VID.\n\n"
		msg+="Pedirá permisos de administrador.\n"
		msg+="───────────────────────────────────────────────────────────────────\n"
		print(msg)

		# SURE?
		if input("(0) Para cancelar.\n")=="0":
			return	
			
		file_out='[Unit]\n'
		file_out+='Description=Random video start\n'
		file_out+='After=network.target\n'
		file_out+='\n'
		file_out+='[Service]\n'
		file_out+=f'ExecStart=python {__file__} -r\n'
		file_out+='Type=oneshot\n'
		file_out+='RemainAfterExit=true\n'
		file_out+='\n'
		file_out+='[Install]\n'
		file_out+='WantedBy=default.target\n'

		textfile=open("random_video_start.service", "w")
		textfile.write(file_out)
		textfile.close()

		subprocess.getoutput("sudo mv random_video_start.service /etc/systemd/system/")
		subprocess.getoutput("sudo chmod 0644 /etc/systemd/system/random_video_start.service")
		subprocess.getoutput("sudo systemctl daemon-reload")
		subprocess.getoutput("sudo systemctl enable random_video_start.service")

		print("✅ Se ha establecido en el arranque del sistema.\n")
		return
	else:
		msg="───────────────────────────────────────────────────────────────────\n"
		msg+="¿Quieres continuar deshabilitando el servicio?\n"
		msg+="(0) Para cancelar.\n"
		msg+="───────────────────────────────────────────────────────────────────\n"
		print(msg)

		if input("Pulsa 0 para cancelar.")=="0":
			return

		print(subprocess.getoutput("sudo systemctl disable random_video_start.service"))
		print(subprocess.getoutput("sudo rm /etc/systemd/system/random_video_start.service"))

		print("✅ Servicio deshabilitado.\n")
		return

def main():
	FILES=os.listdir(DIN)

	while True:
		## MENU
		msg=title
		msg+=" 1. Establece o cambia el video aleatorio.\n"
		msg+=" 2. Borrar el video.\n"
		msg+=" 3. Habilitar el video aleatorio en cada reinicio.\n"
		msg+=" 4. Deshabilitar el video aleatorio en cada reinicio.\n"
		msg+="\n"
		msg+="(0) Salir\n"
		print(msg)

		## OPCIONES
		opt=input("Opción: ")
		if opt=="0":
			sys.exit("== EXIT ==")
		elif opt=="1":
			first_time()
			vid=randomice(FILES)
			set_video(vid)
		elif opt=="2":
			del_video()
		elif opt=="3":
			endes_service(True)
		elif opt=="4":
			endes_service(False)

		else:
			print("❌ Opción no reconocida")

		input("\n...Presiona una tecla para continuar...")
		subprocess.run(['clear'])

if __name__=='__main__':
	# SIN PARÁMETRO (menú)
	if len(sys.argv)==1:
		main()
	# PARÁMETROS
	elif "-h" in sys.argv:
		msg=title
		msg+="Utilidad que nos facilita configurar un video de arranque del modo gaaming en nuestra Steam Deck.\n"
		msg+="\n"
		msg+=" -h · Muestra este apartado.\n"
		msg+=" -r · Establece un video aleatorio (Sin menú).\n"
		print(msg)
	elif "-r" in sys.argv:
		FILES=os.listdir(DIN)
		vid=randomice(FILES)
		set_video(vid)
	else:
		sys.exit("❌ Parámetros aun no soportados.")



	#	main()