import random
from sc2bot.managers.interfaces import ProductionManager
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.ids.upgrade_id import UpgradeId


class StalkerRushProductionManager(ProductionManager):

    def __init__(self, bot, worker_manager, building_manager):
        super().__init__(bot, worker_manager, building_manager)
        self.next_iteration = 0
        print("Production manager ready")

    async def run(self):
        if self.bot.iteration >= self.next_iteration:
            # Buildings
            if self.bot.supply_left < self.bot.units(UnitTypeId.GATEWAY).amount * 2 + self.bot.units(UnitTypeId.WARPGATE).amount * 2 + self.bot.units(UnitTypeId.NEXUS).amount \
                    and not self.bot.already_pending(UnitTypeId.PYLON):
                await self.worker_manager.build(UnitTypeId.PYLON)
            
            elif self.bot.units(UnitTypeId.ASSIMILATOR).amount < self.bot.units(UnitTypeId.NEXUS).amount * 2:
                await self.worker_manager.build(UnitTypeId.ASSIMILATOR)
            
            elif not self.bot.units(UnitTypeId.CYBERNETICSCORE).exists \
                    and self.bot.can_afford(UnitTypeId.CYBERNETICSCORE) \
                    and (self.bot.units(UnitTypeId.WARPGATE).exists or self.bot.units(UnitTypeId.GATEWAY).exists) \
                    and self.bot.units(UnitTypeId.PYLON).ready.exists:
                await self.worker_manager.build(UnitTypeId.CYBERNETICSCORE)
            
            elif self.bot.can_afford(UnitTypeId.GATEWAY) \
                    and self.bot.units(UnitTypeId.GATEWAY).amount + self.bot.units(UnitTypeId.WARPGATE).amount < 4 \
                    and self.bot.units(UnitTypeId.PYLON).ready.exists:
                await self.worker_manager.build(UnitTypeId.GATEWAY)
            
            elif self.bot.can_afford(UnitTypeId.NEXUS):
                await self.worker_manager.build(UnitTypeId.NEXUS)

            elif not self.bot.units(UnitTypeId.TWILIGHTCOUNCIL).exists \
                    and self.bot.units(UnitTypeId.CYBERNETICSCORE).ready.exists \
                    and self.bot.can_afford(UnitTypeId.TWILIGHTCOUNCIL) \
                    and self.bot.units(UnitTypeId.PYLON).exists:
                await self.worker_manager.build(UnitTypeId.TWILIGHTCOUNCIL)

            # Units
            if self.bot.can_afford(UnitTypeId.STALKER) \
                    and await self.building_manager.can_train(UnitTypeId.STALKER):
                await self.building_manager.train(UnitTypeId.STALKER)

            if self.bot.units(UnitTypeId.NEXUS).idle.ready.exists \
                    and self.bot.units(UnitTypeId.PROBE).amount < 20 * self.bot.units(UnitTypeId.NEXUS).amount:
                await self.building_manager.train(UnitTypeId.PROBE)

            # Upgrades 
            if UpgradeId.BLINKTECH not in self.bot.state.upgrades \
                and self.bot.units(UnitTypeId.TWILIGHTCOUNCIL).ready.exists:
                await self.building_manager.research(UpgradeId.BLINKTECH)
            
            if UpgradeId.WARPGATERESEARCH not in self.bot.state.upgrades:
                await self.building_manager.research(UpgradeId.WARPGATERESEARCH)

            else:
                self.next_iteration += 1

            # Make sure to morph gateways into warpgates ASAP
            for gateway in self.bot.units(UnitTypeId.GATEWAY).ready:
                abilities = await self.bot.get_available_abilities(gateway)
                if AbilityId.MORPH_WARPGATE in abilities and self.bot.can_afford(AbilityId.MORPH_WARPGATE):
                    await self.bot.do(gateway(AbilityId.MORPH_WARPGATE))
