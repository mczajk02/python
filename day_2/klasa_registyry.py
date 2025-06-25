class ClassRegistry(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        cls.registry[name] = new_class
        return new_class

    @classmethod
    def get_registred_classes(cls):
        return cls.registry

    @classmethod
    def get_bases_classes(cls):
        return cls.__bases__


class BaseClass(metaclass=ClassRegistry):
    pass

class FirstClass(BaseClass):
    pass

class SecondClass(BaseClass):
    pass

class ThirdClass(BaseClass):
    pass

class EmptyClass(BaseClass):
    pass
class FourthClass(metaclass=ClassRegistry):
    pass

print(f"""Wynik działania metaklasy ClassRegistry:
    {ClassRegistry.get_registred_classes()}
""")

print(f"Przodkowie kasy:" , ClassRegistry.get_bases_classes())