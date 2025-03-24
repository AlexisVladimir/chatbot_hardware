import subprocess
import re

class HardwareInfo:
    def get_info(self, category):
        try:
            result = subprocess.run(['sudo', 'lshw', '-C', category], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            return None
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def check_lshw_installed():
        try:
            subprocess.run(['lshw', '-version'], capture_output=True, text=True)
            return True
        except FileNotFoundError:
            return False

    @staticmethod
    def get_help():
        try:
            result = subprocess.run(['lshw', '-help'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            return "No se pudo obtener la ayuda de lshw."
        except Exception as e:
            return f"Error al obtener ayuda: {str(e)}"

    @staticmethod
    def get_sensors_info():
        try:
            result = subprocess.run(['sensors'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            return "No se pudo obtener la información de sensors."
        except FileNotFoundError:
            return "El comando 'sensors' no está instalado. Instálalo con 'sudo apt install lm-sensors'."
        except Exception as e:
            return f"Error al obtener sensors: {str(e)}"

    @staticmethod
    def get_temperatures():
        output = HardwareInfo.get_sensors_info()
        if "No se pudo" in output or "Error" in output:
            return output
        temp_pattern = re.compile(r"(Core \d+|Package id \d+|[A-Za-z0-9]+):\s+\+(\d+\.\d+)°C")
        matches = temp_pattern.findall(output)
        if matches:
            return "\n".join([f"{name}: {temp}°C" for name, temp in matches])
        return "No se encontraron temperaturas en la salida de sensors."

    @staticmethod
    def get_memory_usage():
        try:
            result = subprocess.run(['free', '-h'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.splitlines()
                for line in lines:
                    if line.startswith("Mem:"):
                        parts = line.split()
                        table = (
                            "Uso de memoria:\n"
                            "+------------+---------+\n"
                            "| Categoría  | Valor   |\n"
                            "+------------+---------+\n"
                            f"| Total      | {parts[1]:<7} |\n"
                            f"| Usada      | {parts[2]:<7} |\n"
                            f"| Libre      | {parts[3]:<7} |\n"
                            f"| Compartida | {parts[4]:<7} |\n"
                            f"| Buff/Cache | {parts[5]:<7} |\n"
                            f"| Disponible | {parts[6]:<7} |\n"
                            "+------------+---------+"
                        )
                        return table
                return "No se pudo parsear el uso de memoria."
            return "No se pudo obtener el uso de memoria."
        except Exception as e:
            return f"Error al obtener uso de memoria: {str(e)}"

    @staticmethod
    def get_pci_devices():
        try:
            result = subprocess.run(['lspci'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.splitlines()
                if not lines:
                    return "No se encontraron dispositivos PCI."
                
                # Encabezado de la tabla
                table = "Dispositivos PCI:\n"
                table += "+----------+---------------------------------------------+\n"
                table += "| ID       | Descripción                                 |\n"
                table += "+----------+---------------------------------------------+\n"
                
                # Procesamos cada línea de lspci
                for line in lines:
                    parts = line.split(" ", 1)  # Separamos ID y descripción
                    if len(parts) == 2:
                        device_id, description = parts
                        # Ajustamos longitud para que quepa en la tabla
                        table += f"| {device_id:<8} | {description:<43} |\n"
                
                table += "+----------+---------------------------------------------+"
                return table
            return "No se pudo obtener la información de lspci."
        except FileNotFoundError:
            return "El comando 'lspci' no está instalado. Instálalo con 'sudo apt install pciutils'."
        except Exception as e:
            return f"Error al obtener dispositivos PCI: {str(e)}"