import time
from colorama import Fore, Style

# WriterHelper, konsol ekranına çeşitli yazıları yazdırmak için kullanılan bir sınıftır.
class WriterHelper:

    # writerText metodu, konsol ekranına yazı yazdırmak için kullanılır.
    @staticmethod
    def writerText(text: str, prompt: bool = False, color: str = None):
        writerColor = Fore.WHITE
        
        if color == "success":
            writerColor = Fore.GREEN
        elif color == "error":
            writerColor = Fore.RED
        elif color == "warning":
            writerColor = Fore.YELLOW
        elif color == "info":
            writerColor = Fore.CYAN
        
        combinedText = ""
        for i in text:
            combinedText += i
            print(writerColor + combinedText + Style.RESET_ALL, end='\r', flush=True)
            time.sleep(0.01)
        
        if prompt:
            return input(writerColor + combinedText + Style.RESET_ALL + " ")
        else:
            print(writerColor + combinedText + Style.RESET_ALL)


    # writerTitle metodu, konsol ekranına başlık yazdırmak için kullanılır. WriterText metodu kullanılarak yazı yazdırılır.
    def writerTitle(self, title: str):
        self.writerText(Fore.LIGHTBLUE_EX + title + Style.RESET_ALL)
        self.writerText(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)
    
    # writerMenu metodu, konsol ekranına menü yazdırmak için kullanılır. WriterText metodu kullanılarak yazı yazdırılır.
    def writerMenu(self, menuDict: dict, title: str = None) -> None:
        if title:
            self.writerText(Fore.LIGHTBLUE_EX + title + Style.RESET_ALL)

        self.writerText(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)
        for key in menuDict:
            self.writerText(Fore.LIGHTBLUE_EX + f"{key} - {menuDict[key]}" + Style.RESET_ALL)
        self.writerText(Fore.LIGHTBLUE_EX + "------------------------------------" + Style.RESET_ALL)