from sc2bot.managers.interfaces import ArmyManager
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units
from sc2bot.managers.protoss_managers.army.squad import Squad
from sc2.ids.ability_id import AbilityId
import math
from sc2.units import Units


class AdvancedArmyManager(ArmyManager):

    def __init__(self, bot):
        super().__init__(bot)
        self.squads = []

    async def run(self):

        assert len(self.squads) <= 5

        # Create squads
        for squad in self.squads:
            units = []
            if squad.unit_types is None:
                for unit in self.bot.units.not_structure.exclude_type(UnitTypeId.PROBE):
                    units.append(unit)
            else:
                for unit in self.bot.units.not_structure.exclude_type(UnitTypeId.PROBE):
                    if unit.type_id in squad.unit_types:
                        units.append(unit)
            squad.units = Units(units, self.bot.game_data())

        # Control squads:
        for squad in self.squads:
            await squad.run()

    async def harass(self, target, unit_types):
        new_squad = Squad(self.bot, target, unit_types, order="harass")
        for i in range(len(self.squads)):
            squad = self.squads[i]
            if (set(squad.unit_types) if squad.unit_types is not None else set()) == (set(unit_types) if unit_types is not None else set()):
                if squad.order == "harass" and squad.target == target:
                    return
                self.squads[i] = new_squad
        self.squads.append(new_squad)

    async def attack(self, target, unit_types=None):
        squad = Squad(self.bot, target, unit_types, order="attack")
        if unit_types is None:
            self.squads = [squad for squad in self.squads if squad.order == "harass"]
        self.squads.append(squad)

    async def defend(self, target, unit_types=None):
        new_squad = Squad(self.bot, target, unit_types, order="defend")
        if unit_types is None:
            self.squads = [squad for squad in self.squads if squad.order == "harass"]
        self.squads.append(new_squad)

