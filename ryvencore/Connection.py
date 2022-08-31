"""
deprecated and now unused
"""

from .Base import Base, Event

from .InfoMsgs import InfoMsgs


class Connection(Base):
    """
    The base class for both types of connections. All data is transmitted through a connection from an output
    port to some connected input port.
    """

    def __init__(self, params):
        Base.__init__(self)

        self.activated = Event(object)  # TODO: connections are not activated anymore

        self.out, self.inp, self.flow = params

    # def activate(self, data=None):
    #     """Causes forward propagation of information"""
    #
    #     self.activated.emit(data)


class ExecConnection(Connection):
    pass

    # def activate(self, data=None):
    #     """Causes an update in the input port"""
    #     InfoMsgs.write('exec connection activated')
    #     super().activate()
    #
    #     self.inp.update()


class DataConnection(Connection):

    def __init__(self, params):
        super().__init__(params)

        self.data = None

    # def get_val(self):
    #     """Gets the value of the output port -- only used in exec mode flows"""
    #     InfoMsgs.write('data connection getting value')
    #
    #     return self.out.get_val()

    # def activate(self, data=None):
    #     """Passes data to the input port and causes update"""
    #     InfoMsgs.write('data connection activated')
    #     super().activate(data)
    #
    #     # propagate data forward
    #     self.inp.update(data)
