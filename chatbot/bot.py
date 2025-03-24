from chatbot.interface import TerminalInterface
from hardware.lshw import HardwareInfo
from hardware.parser import parse_request, get_lshw_options, hardware_map

class Chatbot:
    def __init__(self):
        self.interface = TerminalInterface()
        self.hardware = HardwareInfo()
        self.options = get_lshw_options()
        print("Opciones cargadas al inicio:", self.options)

    def process_input(self, user_input):
        user_input_lower = user_input.lower().strip()
        
        if user_input_lower == "salir":
            return False, "¡Hasta luego!"
        elif user_input_lower == "opciones":
            if self.options:
                response = "Opciones disponibles de lshw:\n" + "\n".join(self.options)
                response += "\n\nComandos de hardware disponibles:\n"
                response += "\n".join([f"{key}: {value}" for key, value in hardware_map.items()])
                return True, response
            else:
                return True, "No se pudieron cargar las opciones de lshw."
        elif user_input_lower == "hola":
            return True, "¡Hola! ¿En qué puedo ayudarte hoy?"
        elif user_input_lower == "como estas":
            return True, "Muy bien, gracias por preguntar. ¿En qué puedo ayudarte hoy?"
        
        category = parse_request(user_input)
        if category:
            if category == "sensors":
                info = self.hardware.get_sensors_info()
                return True, f"Información completa de sensores:\n{info}"
            elif category == "temperature":
                info = self.hardware.get_temperatures()
                return True, f"Temperaturas:\n{info}"
            elif category == "memory_usage":
                info = self.hardware.get_memory_usage()
                return True, info
            elif category == "pci_devices":
                info = self.hardware.get_pci_devices()
                return True, info
            else:  # Para categorías de lshw
                info = self.hardware.get_info(category)
                if info:
                    return True, f"Información de {category}:\n{info}"
                return True, "No se pudo obtener la información."
        return True, "No entendí. Prueba con 'hola', 'cpu', 'ram', 'temperatura', 'uso memoria', 'lspci', etc."

    def run(self):
        self.interface.show_welcome()
        while True:
            user_input = self.interface.get_input()
            keep_running, response = self.process_input(user_input)
            self.interface.show_response(response)
            if not keep_running:
                break