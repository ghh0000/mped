# -*- coding:utf-8 -*-

from mpedBase import Base
from mpedClass import Class

class Instance(Base):
    """Instance of a user-defined class. """

    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, {})
