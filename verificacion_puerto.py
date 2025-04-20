puerto = int(input("Introduce número de puerto: "))
if 0 <= puerto <= 1023:
    tipo = "Bien conocido"
elif 1024 <= puerto <= 49151:
    tipo = "Registrado"
elif 49152 <= puerto <= 65535:
    tipo = "Dinámico/privado"
else:
    tipo = None

if tipo:
    print(f"Puerto {puerto}: {tipo}")
else:
    print("No corresponde a un puerto válido")