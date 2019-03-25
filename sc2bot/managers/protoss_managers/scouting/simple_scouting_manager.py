from sc2bot.managers.interfaces import ScoutingManager
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
import math


class SimpleScoutingManager(ScoutingManager):

    def __init__(self, bot, worker_manager, building_manager):
        super().__init__(bot, worker_manager, building_manager)

    async def run(self):
        # Worker scouting?
        if self.bot.iteration % 50 == 0 and self.bot.known_enemy_structures.amount == 0 and self.bot.units(UnitTypeId.PYLON):
            target = self.bot.known_enemy_structures.random_or(self.bot.enemy_start_locations[0]).position
            # print("ScoutingManager: scouting ", target)
            await self.worker_manager.scout(target)

