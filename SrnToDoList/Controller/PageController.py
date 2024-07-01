from SrnToDoList.Controller.GraphicController import GraphicController
from SrnToDoList.Controller.HomeController import HomeController
from SrnToDoList.Controller.LogController import LogController
from SrnToDoList.Controller.LoginController import LoginController
from SrnToDoList.Controller.MainController import MainController
from SrnToDoList.Controller.ProfileController import ProfileController
from SrnToDoList.Controller.RegisterController import RegisterController
from SrnToDoList.Controller.TaskController import TaskController
from SrnToDoList.Controller.TaskListController import TaskListController
from SrnToDoList.Helper.SessionHelper import SessionHelper

# PageController sınıfından diğer controller sınıflarına erişim sağlar.
# Ek olarak de bir sessionID ve sessionHelper nesnesi oluşturur.
# Burada sessionID ve sessionHelper nesneleri, kullanıcı oturum bilgilerini tutar.
class PageController:
    def __init__(self):
        self.sessionID = None
        self.sessionHelper = SessionHelper()
        self.homeController = HomeController(self)
        self.loginController = LoginController(self)
        self.registerController = RegisterController(self)
        self.mainController = MainController(self)
        self.taskListController = TaskListController(self)
        self.taskController = TaskController(self)
        self.profileController = ProfileController(self)
        self.logController = LogController(self)
        self.graphicController = GraphicController(self)