"""FINISHED"""
import sys

version = sys.version_info[0]
if version == 2:
    from abc import ABCMeta, abstractmethod, abstractproperty
    superclass = object
elif version == 3:
    from abc import ABC, abstractmethod
    superclass = ABC
else:
    print('This version of Python is unsupported.')


def compatible_abstractproperty(function):
    if version == 2: return abstractproperty(function)
    elif version == 3: return property(abstractmethod(function))
    else: return function


class Path(superclass):
    if version == 2: __metaclass__ = ABCMeta

    @abstractmethod
    def increment(self, amount):
        raise NotImplementedError

    @compatible_abstractproperty
    def target(self):
        raise NotImplementedError

    @compatible_abstractproperty
    def independent_variable(self):
        raise NotImplementedError
