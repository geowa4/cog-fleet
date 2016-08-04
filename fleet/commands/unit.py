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
        try:
            filter_string = self.request.options.get('filter', '')
        except:
            filter_string = ''
        for unit in self.get_all_units():
            if filter_string in unit.get('name'):
                unit.pop('options', None)
                results.append(unit)
        self.response.content(results).send()

    def get_all_units(self):
        units = []
        fleet_response = util.api_get('units')
        units.extend(fleet_response.get('units', []))
        while fleet_response.get('nextPageToken', None) is not None:
            fleet_response = util.api_get(
                'units?nextPageToken={}'.format(
                    fleet_response.get('nextPageToken')
                )
            )
            units.extend(fleet_response.get('units', []))
        self.amend_state_onto_units(units)
        return units

    def amend_state_onto_units(self, units):
        for unit in units:
            if unit.get('machineID') is None:
                state = {}
            else:
                state = util.api_get(
                    'state?machineID={}&unitName={}'.format(
                        unit.get('machineID'), unit.get('name')
                    )
                ).get('states', [{}])[0]
            unit['systemdSubState'] = state.get('systemdSubState', '')
            unit['systemdLoadState'] = state.get('systemdLoadState', '')
            unit['systemdActiveState'] = state.get('systemdActiveState', '')

    def parse_subcommand_(self):
        if self.request.args is None:
            return self.list
        if self.request.args[0] == "list":
            return self.list
        self.fail("Unknown subcommand: '%s'" % self.request.args[0])
