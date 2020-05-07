#!/usr/bin/env python3
from controllers.grade_book_controller import GradeBookController
from controllers.graphic_date_controller import GraphicDateController
from controllers.app import ConsoleApp
from controllers.graph_app import GraphApp


def main_win():
    controller = GraphicDateController()
    app = GraphApp(controller)
    app.run_app()


def main_console():
    controller = GradeBookController()
    app = ConsoleApp(controller)
    app.run_app()


if '__main__' == __name__:
    main_console()