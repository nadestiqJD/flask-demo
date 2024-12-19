from viewmodels.IViewmodel import IViewmodel


class EmailViewmodel(IViewmodel):
    def __init__(self, receivers):
        self.Receivers = receivers
    Receivers = []