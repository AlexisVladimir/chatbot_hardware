from chatbot.bot import Chatbot
from hardware.lshw import HardwareInfo

def main():
    if not HardwareInfo.check_lshw_installed():
        print("Por favor, instala lshw primero con: sudo apt install lshw")
        return
    bot = Chatbot()
    bot.run()

if __name__ == "__main__":
    main()