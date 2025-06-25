from prod1 import Product1
from concrete_builder import Builder

class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._builder = Product1()

    @property
    def product(self)->Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("PartA1")

    def produce_part_b(self):
        self._product.add("PartB1")

    def produce_part_c(self):
        self._product.add("PartC1")


