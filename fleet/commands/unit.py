from fleet.commands.base import FleetBase
import fleet.util as util


class Unit(FleetBase):
    def __init__(self):
        super().__init__()

    def run(self):
        handler = self.parse_subcommand_()
        handler()

    def list(self):
        results = []
        for unit in util.api_get('units'):
            results.append(unit)
        self.response.content(results).send()

    def parse_subcommand_(self):
        if self.request.args is None:
            return self.list
        if self.request.args[0] == "list":
            return self.list
        self.fail("Unknown subcommand: '%s'" % self.request.args[0])
