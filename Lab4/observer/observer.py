#!/usr/bin/env python3
from abc import abstractmethod
from time import sleep
from progressbar import ProgressBar, Percentage, Bar


def main():
    subject = Observable()
    subject.add_observer(Progress())
    subject.add_observer(Logger())
    for i in range(1, 11):
        sleep(1)
        subject.notify(i)


class Observable:
    def __init__(self):
        self.__obs_list = []

    def add_observer(self, obs):
        self.__obs_list.append(obs)

    def notify(self, *args, **kwargs):
        for obs in self.__obs_list:
            obs.update(*args, **kwargs)


class Observer(object):
    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        pass


class Progress(Observer):
    def __init__(self):
        self.widgets = [Percentage(), Bar()]
        self.bar = ProgressBar(widgets=self.widgets, min_value=1, max_value=10).start()
        super().__init__()

    def update(self, progress):
        self.bar.update(progress)
        if progress == 10:
            self.bar.finish()


class Logger(Observer):
    def __init__(self):
        self.f = open("logfile.txt", "w")
        super().__init__()

    def update(self, progress):
        self.f.write("Current progress: {progress}\n".format(progress=progress))
        if progress == 10:
            self.f.close()


if '__main__' == __name__:
    main()