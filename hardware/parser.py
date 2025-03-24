from hardware.lshw import HardwareInfo

hardware_map = {
    "cpu": "processor",
    "procesador": "processor",
    "ram": "memory",
    "memoria": "memory",
    "disco": "disk",
    "almacenamiento": "disk",
    "tarjeta grafica": "display",
    "gpu": "display",
    "red": "network",
    "network": "network",
    "sensors": "sensors",
    "sensores": "sensors",
    "temperatura": "temperature",
    "temp": "temperature",
    "uso memoria": "memory_usage",
    "memoria usada": "memory_usage",
    "lspci": "pci_devices",
    "dispositivos pci": "pci_devices"
}

def parse_request(user_input):
    user_input = user_input.lower().strip()
    for key, category in hardware_map.items():
        if key in user_input:
            return category
    return None

def get_lshw_options():
    help_text = HardwareInfo.get_help()
    if not help_text or "No se pudo" in help_text:
        return ["Error: No se pudo obtener las opciones de lshw."]
    
    lines = help_text.splitlines()
    options = [line.strip() for line in lines if line.strip().startswith('-')]
    if not options:
        return ["No se encontraron opciones en la salida de 'lshw -help'."]
    return options