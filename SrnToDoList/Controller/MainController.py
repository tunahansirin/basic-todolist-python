from SrnToDoList.View.MainView import MainView

# Projede kullanılan ana sınıf.
class MainController:
    def __init__(self, pageController):
        self.pageController = pageController

    # Program başlandığında görünecek ana ekran yönlendirmesi
    def ShowMainView(self):
        MainView(self.pageController).MainMenu()