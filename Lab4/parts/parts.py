#!/usr/bin/env python3


def main():
    board1 = ComputerPart("mini_board", 500)
    board2 = ComputerPart("advanced_board", 1000)
    video1 = ComputerPart("video_accelerator", 700)
    video2 = ComputerPart("better_accelerator", 900)
    sound1 = ComputerPart("midi_sound_card", 400)
    disk1 = ComputerPart("ssd", 500)
    disk2 = ComputerPart("hdd", 300)
    mouse1 = ComputerPart("blue_tooth_mouse", 50)
    keyboard1 = ComputerPart("blue_tooth_keyboard", 100)
    keyboard2 = ComputerPart("keyboard_with_touch_pad", 200)
    usb1 = ComputerPart("blue_tooth_dongle", 50)

    set1 = ComputerSet("gamer_set")
    set1.add_component(board2)
    set1.add_component(sound1)
    set1.add_component(video1)

    # on the second thought...
    set1.remove_component(video1)
    set1.add_component(video2)

    set1.add_component(disk1)
    set1.add_component(keyboard2)

    set2 = ComputerSet("office_set")
    set2.add_component(board1)
    set2.add_component(disk2)

    set3 = ComputerSet("peripheral_set")
    set3.add_component(mouse1)
    set3.add_component(keyboard1)
    set3.add_component(usb1)

    set2.add_component(set3)

    assert set1.get_price() == 3000
    assert set2.get_price() == 1000

    print(set1.get_price())
    print(set2.get_price())


class Component:
    def __init__(self, name, price):
        super().__init__()
        self.__name = name
        self.__price = price

    def add_price(self, price):
        self.__price += price

    def del_price(self, price):
        self.__price -= price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


class ComputerPart(Component):
    def __init__(self, name, price):
        super().__init__(name, price)


class ComputerSet(Component):
    def __init__(self, name):
        super().__init__(name, 0)
        self.__component_dict = dict()

    def add_component(self, component: Component):
        self.__component_dict[component.get_name()] = component
        super().add_price(component.get_price())

    def remove_component(self, component: Component):
        if component.get_name() in self.__component_dict:
            self.del_price(self.__component_dict[component.get_name()].get_price())
            del self.__component_dict[component.get_name()]


if __name__ == '__main__':
    main()