from SrnToDoList.Helper.GraphicsHelper import GraphicsHelper
from SrnToDoList.View.GraphicView import GraphicView

# Grafiklerle ilgili işlemlerin yapıldığı sınıf.
class GraphicController:
    def __init__(self, pageController):
        self.pageController = pageController

    # -> Sınıf içerisinde kullanılan görüntü yönlendirme metotları

    # Grafik menüsünü gösteren metot.
    def ShowGraphicMenu(self):
        GraphicView(self.pageController).GraphicMenu()