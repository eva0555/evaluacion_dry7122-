import json
with open('dispositivos.json', 'r') as file:
    dispositivos_data = json.load(file)

    for d in dispositivos_data.get('dispositivos', []):
        nombre = d.get('nombre', '<sin nombre>')
        ip     = d.get('ip', '<sin IP>')
        estado = d.get('estado', '<sin estado>')
        print(f"  • {nombre}")
        print(f"      IP:     {ip}")
        print(f"      Estado: {estado}")
        print()
