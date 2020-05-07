from abc import ABC, abstractmethod
from models.grade_book_model import GradeBookModel
from views.console_view import ConsoleDateView


class AbstractApp(ABC):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

    @abstractmethod
    def run_app(self):
        pass

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, new_controller):
        self.__controller = new_controller


class ConsoleApp(AbstractApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.__model = GradeBookModel()
        self.__view = ConsoleDateView('ConsoleDateView', self.__model)
        self.__model.add_observer(self.__view)

        controller.model = self.__model
        controller.view = self.__view

    def run_app(self):
        while self.controller.get_user_input():
            pass