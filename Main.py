from Controler import Controler
from Parser import Parser


def __Main__():
    m_parser = Parser()
    test = Controler(m_parser)
    test.launch()


__Main__()