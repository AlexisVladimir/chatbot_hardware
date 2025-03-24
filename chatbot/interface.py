
class TerminalInterface:
    def show_welcome(self):
        print("¡Hola! Soy Vladimir un chatbot para ver informacion del hardware de tu PC en Ubuntu.")
        print("Pregunta por: cpu, ram, disco, tarjeta grafica, red, etc.")
        print("Escribe 'opciones' para ver los comandos de lshw disponibles.")
        print("Escribe 'salir' para terminar.\n")

    def get_input(self):
        return input("¿Qué quieres saber? > ")

    def show_response(self, response):
        print(response)
        print("-" * 50)