from cog.command import Command


class FleetBase(Command):
    def __init__(self):
        super().__init__()

    def prepare(self):
        pass
