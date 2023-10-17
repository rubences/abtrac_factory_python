from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """ La interfaz Abstract Factory declara un conjunto de métodos que devuelven
     diferentes productos abstractos. Estos productos se llaman familia y son
     relacionados por un tema o concepto de alto nivel. Los productos de una familia suelen ser
     capaces de colaborar entre sí. Una familia de productos puede tener varios
     variantes, pero los productos de una variante son incompatibles con los productos de
     otro.
     """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

    @abstractmethod
    def create_product_c(self) -> AbstractProductC:
        pass

    @abstractmethod
    def create_product_d(self) -> AbstractProductD:
        pass


class ConcreteFactory1(AbstractFactory):
    """
     Las Fábricas de Hormigón producen una familia de productos que pertenecen a un solo
     variante. La fábrica garantiza que los productos resultantes son compatibles. Nota
     que las firmas de los métodos de Concrete Factory devuelven un resumen
     producto, mientras que dentro del método se instancia un producto concreto.
     """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

    def create_product_c(self) -> AbstractProductC:
        return ConcreteProductC1()
    
    def create_product_d(self) -> AbstractProductD:
        return ConcreteProductD1()


class ConcreteFactory2(AbstractFactory):
    """
    Cada fábrica de hormigón tiene una variante de producto correspondiente.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
    
    def create_product_c(self) -> AbstractProductC:
        return ConcreteProductC2()
    
    def create_product_d(self) -> AbstractProductD:
        return ConcreteProductD2()



class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
         pass


    """
    Concrete Products are created by corresponding Concrete Factories.
    """


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
Aquí está la interfaz base de otro producto. Todos los productos pueden interactuar
     entre sí, pero la interacción adecuada sólo es posible entre productos de
     la misma variante concreta.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
El Producto B es capaz de hacer lo suyo...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"

class AbstractProductC(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_c(self) -> str:
        pass


class ConcreteProductC1(AbstractProductC):
    def useful_function_c(self) -> str:
        return "The result of the product C1."

class ConcreteProductC2(AbstractProductC):
    def useful_function_c(self) -> str:
        return "The result of the product C2."

class AbstractProductD(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_d(self) -> str:
        pass

class ConcreteProductD1(AbstractProductD):
    def useful_function_d(self) -> str:
        return "The result of the product D1."

class ConcreteProductD2(AbstractProductD):
    def useful_function_d(self) -> str:
        return "The result of the product D2."


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    product_c = factory.create_product_c()
    product_d = factory.create_product_d()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")
    print(f"{product_c.useful_function_c()}")
    print(f"{product_d.useful_function_d()}")




if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())