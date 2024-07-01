from SrnToDoList.View.HomeView import HomeView

# Ana ekran ile ilgili islemlerin yapildigi sınıf.
class HomeController:
    def __init__(self, pageController):
        self.pageController = pageController
        
    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Ana ekranı gösteren metot.
    def ShowHomeView(self):
        HomeView(self.pageController).HomeMenu()
