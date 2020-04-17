#!/usr/bin/env python


def main():
    print("Base production line:")
    product1 = Product("product1")
    Production.finish_production_process(Production.prepare_production_process(product1)).print_stages()
    print("Extended production line:")
    product2 = Product("product2")
    ExtendedProduction.finish_production_process(
        ExtendedProduction.new_stage(ExtendedProduction.prepare_production_process(product2))).print_stages()


class Product:
    def __init__(self, name: str):
        self.name = name
        self.current_stage = ''
        self.stages = []

    def print_stages(self):
        for stage in self.stages:
            print(stage)


class Production:
    @staticmethod
    def prepare_production_process(product: Product):
        product.current_stage = "preparation"
        product.stages.append(product.current_stage)
        return product

    @staticmethod
    def finish_production_process(product: Product):
        product.current_stage = "termination"
        product.stages.append(product.current_stage)
        return product


class ExtendedProduction(Production):
    @staticmethod
    def new_stage(product: Product):
        product.current_stage = "extension"
        product.stages.append(product.current_stage)
        return product


if __name__ == '__main__':
    main()