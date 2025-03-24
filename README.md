# Chatbot de Información de Hardware en Ubuntu

Este proyecto es un chatbot modular escrito en Python que permite obtener información del hardware de un sistema Ubuntu utilizando comandos como `lshw`, `sensors`, `free` y `lspci`. El chatbot interactúa con el usuario a través de la terminal y presenta la información en formatos organizados, como tablas o listas.

## Características
- **Información de hardware**: Consulta detalles de CPU, RAM, discos, tarjetas gráficas, red, etc., usando `lshw`.
- **Temperaturas**: Muestra las temperaturas de la CPU y otros componentes con `sensors`.
- **Uso de memoria**: Presenta el uso de RAM en una tabla clara con `free`.
- **Dispositivos PCI**: Lista dispositivos PCI (como GPU, red, USB) en una tabla con `lspci`.
- **Interacción amigable**: Responde a saludos como "hola" y ofrece una lista de comandos con "opciones".
- **Modularidad**: El código está organizado en módulos para facilitar su mantenimiento y expansión.

## Requisitos
- **Sistema operativo**: Ubuntu (o cualquier distribución Linux compatible).
- **Python**: Versión 3.6 o superior.
- **Dependencias del sistema**:
  - `lshw`: Para información general del hardware.
  - `lm-sensors`: Para temperaturas.
  - `pciutils`: Para dispositivos PCI (`lspci`).
  - `free`: Viene preinstalado en Ubuntu para uso de memoria.

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/chatbot-hardware-ubuntu.git
   cd chatbot-hardware-ubuntu
2. **Instala las dependencias del sistema**:
    ```bash
    sudo apt update
    sudo apt install lshw lm-sensors pciutils
    sudo sensors-detect