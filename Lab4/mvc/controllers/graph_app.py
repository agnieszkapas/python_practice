from .app import AbstractApp
from PyQt5.QtWidgets import QApplication
from models.grade_book_model import GradeBookModel
from views.graph_view import MainWindowView, GraphDateView, GraphActionButton


class GraphApp(AbstractApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.__app = QApplication([])

        model = GradeBookModel()
        date_view = GraphDateView('DateView', model)
        model.add_observer(date_view)
        action_view = GraphActionButton('ActionView')

        controller.model = model
        controller.view = action_view

        self.__win_view = MainWindowView()
        self.__win_view.add_component(date_view)
        self.__win_view.add_component(action_view)

    def run_app(self):
        self.__win_view.show()
        self.__app.exec_()