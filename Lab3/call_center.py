#!/usr/bin/env python
import random


def main():
    employee = Employee('Caller')
    employee.set_random_status()
    employee.set_message('Good Morning')
    manager = Employee('Manager')
    manager.set_random_status()
    director = Employee('Director')
    employee.dispatch_call(employee).dispatch_call(manager).dispatch_call(director)


class Employee:
    def __init__(self, position: str):
        self.is_busy = False
        self.position = position
        self.message = None

    def set_message(self, message: str):
        self.message = message

    def dispatch_call(self, employee: 'Employee'):
        if employee.is_busy:
            employee.message = self.message
            print("Call passed to {}".format(employee.position))
            return employee
        else:
            print("Call handled by {}".format(employee.position))
            print("Message: {}".format(self.message))
            exit()

    def set_random_status(self):
        self.is_busy = random.choice([True, False])


if __name__ == "__main__":
    main()