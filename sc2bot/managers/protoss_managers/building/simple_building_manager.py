from sc2bot.managers.interfaces import BuildingManager
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.ids.upgrade_id import UpgradeId
from random import choice


class SimpleBuildingManager(BuildingManager):

    def __init__(self, bot, worker_manager):
        super().__init__(bot, worker_manager)

        self.trained_at = {
            UnitTypeId.PROBE: [UnitTypeId.NEXUS],
            UnitTypeId.ZEALOT: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE],
            UnitTypeId.ADEPT: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE],
            UnitTypeId.STALKER: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE],
            UnitTypeId.SENTRY: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE],
            UnitTypeId.HIGHTEMPLAR: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE],
            UnitTypeId.DARKTEMPLAR: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE],
            UnitTypeId.IMMORTAL: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.OBSERVER: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.WARPPRISM: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.DISRUPTOR: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.COLOSSUS: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.PHOENIX: [UnitTypeId.STARGATE],
            UnitTypeId.ORACLE: [UnitTypeId.STARGATE],
            UnitTypeId.VOIDRAY: [UnitTypeId.STARGATE],
            UnitTypeId.TEMPEST: [UnitTypeId.STARGATE],
            UnitTypeId.CARRIER: [UnitTypeId.STARGATE],
            UnitTypeId.MOTHERSHIP: [UnitTypeId.NEXUS],
            UnitTypeId.INTERCEPTOR: [UnitTypeId.CARRIER],
            UnitTypeId.ARCHON: [UnitTypeId.HIGHTEMPLAR, UnitTypeId.DARKTEMPLAR]
        }

        self.researched_at = {
            UpgradeId.ADEPTPIERCINGATTACK: UnitTypeId.TWILIGHTCOUNCIL, 
            UpgradeId.BLINKTECH: UnitTypeId.TWILIGHTCOUNCIL,
            UpgradeId.CHARGE: UnitTypeId.TWILIGHTCOUNCIL,
            UpgradeId.EXTENDEDTHERMALLANCE: UnitTypeId.ROBOTICSBAY,
            UpgradeId.OBSERVERGRAVITICBOOSTER: UnitTypeId.ROBOTICSBAY,
            UpgradeId.GRAVITICDRIVE: UnitTypeId.ROBOTICSBAY,
            UpgradeId.CARRIERLAUNCHSPEEDUPGRADE: UnitTypeId.FLEETBEACON,
            UpgradeId.ANIONPULSECRYSTALS: UnitTypeId.FLEETBEACON,
            UpgradeId.PROTOSSAIRARMORSLEVEL1: UnitTypeId.CYBERNETICSCORE,
            UpgradeId.PROTOSSAIRARMORSLEVEL2: UnitTypeId.CYBERNETICSCORE,
            UpgradeId.PROTOSSAIRARMORSLEVEL3: UnitTypeId.CYBERNETICSCORE,
            UpgradeId.PROTOSSAIRWEAPONSLEVEL1: UnitTypeId.CYBERNETICSCORE,
            UpgradeId.PROTOSSAIRWEAPONSLEVEL2: UnitTypeId.CYBERNETICSCORE,
            UpgradeId.PROTOSSAIRWEAPONSLEVEL3: UnitTypeId.CYBERNETICSCORE,
            UpgradeId.PROTOSSGROUNDARMORSLEVEL1: UnitTypeId.FORGE,
            UpgradeId.PROTOSSGROUNDARMORSLEVEL2: UnitTypeId.FORGE,
            UpgradeId.PROTOSSGROUNDARMORSLEVEL3: UnitTypeId.FORGE,
            UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1: UnitTypeId.FORGE,
            UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2: UnitTypeId.FORGE,
            UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3: UnitTypeId.FORGE,
            UpgradeId.PROTOSSSHIELDSLEVEL1: UnitTypeId.FORGE,
            UpgradeId.PROTOSSSHIELDSLEVEL2: UnitTypeId.FORGE,
            UpgradeId.PROTOSSSHIELDSLEVEL3: UnitTypeId.FORGE,
            UpgradeId.PSISTORMTECH: UnitTypeId.TEMPLARARCHIVE,
            UpgradeId.DARKTEMPLARBLINKUPGRADE: UnitTypeId.DARKSHRINE,
            UpgradeId.WARPGATERESEARCH: UnitTypeId.CYBERNETICSCORE,
        }

        self.requirements = {
            UnitTypeId.GATEWAY: [UnitTypeId.NEXUS, UnitTypeId.PYLON],
            UnitTypeId.FORGE: [UnitTypeId.NEXUS, UnitTypeId.PYLON],
            UnitTypeId.PHOTONCANNON: [UnitTypeId.FORGE, UnitTypeId.PYLON],
            UnitTypeId.SHIELDBATTERY: [UnitTypeId.CYBERNETICSCORE, UnitTypeId.PYLON],
            UnitTypeId.CYBERNETICSCORE: [UnitTypeId.GATEWAY, UnitTypeId.WARPGATE, UnitTypeId.PYLON],
            UnitTypeId.TWILIGHTCOUNCIL: [UnitTypeId.CYBERNETICSCORE, UnitTypeId.PYLON],
            UnitTypeId.STARGATE: [UnitTypeId.CYBERNETICSCORE, UnitTypeId.PYLON],
            UnitTypeId.ROBOTICSFACILITY: [UnitTypeId.CYBERNETICSCORE, UnitTypeId.PYLON],
            UnitTypeId.TEMPLARARCHIVE: [UnitTypeId.TWILIGHTCOUNCIL, UnitTypeId.PYLON],
            UnitTypeId.DARKSHRINE: [UnitTypeId.TWILIGHTCOUNCIL, UnitTypeId.PYLON],
            UnitTypeId.FLEETBEACON: [UnitTypeId.STARGATE, UnitTypeId.PYLON],
            UnitTypeId.ROBOTICSBAY: [UnitTypeId.ROBOTICSFACILITY, UnitTypeId.PYLON]
        }

        self.unit_requirements = {
            UnitTypeId.PROBE: [UnitTypeId.NEXUS],
            UnitTypeId.ZEALOT: [UnitTypeId.GATEWAY],
            UnitTypeId.ADEPT: [UnitTypeId.GATEWAY, UnitTypeId.CYBERNETICSCORE],
            UnitTypeId.STALKER: [UnitTypeId.GATEWAY, UnitTypeId.CYBERNETICSCORE],
            UnitTypeId.SENTRY: [UnitTypeId.GATEWAY, UnitTypeId.CYBERNETICSCORE],
            UnitTypeId.HIGHTEMPLAR: [UnitTypeId.GATEWAY, UnitTypeId.TEMPLARARCHIVE],
            UnitTypeId.DARKTEMPLAR: [UnitTypeId.GATEWAY, UnitTypeId.DARKSHRINE],
            UnitTypeId.IMMORTAL: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.OBSERVER: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.WARPPRISM: [UnitTypeId.ROBOTICSFACILITY],
            UnitTypeId.DISRUPTOR: [UnitTypeId.ROBOTICSFACILITY, UnitTypeId.ROBOTICSBAY],
            UnitTypeId.COLOSSUS: [UnitTypeId.ROBOTICSFACILITY, UnitTypeId.ROBOTICSBAY],
            UnitTypeId.PHOENIX: [UnitTypeId.STARGATE],
            UnitTypeId.ORACLE: [UnitTypeId.STARGATE],
            UnitTypeId.VOIDRAY: [UnitTypeId.STARGATE],
            UnitTypeId.TEMPEST: [UnitTypeId.STARGATE, UnitTypeId.FLEETBEACON],
            UnitTypeId.CARRIER: [UnitTypeId.STARGATE, UnitTypeId.FLEETBEACON],
            UnitTypeId.MOTHERSHIP: [UnitTypeId.NEXUS, UnitTypeId.FLEETBEACON],
            UnitTypeId.INTERCEPTOR: [UnitTypeId.CARRIER],
            UnitTypeId.ARCHON: [UnitTypeId.HIGHTEMPLAR, UnitTypeId.DARKTEMPLAR]
        }

    async def run(self):
        pass

    async def train(self, unit, max_queue=1):
        print("BuildingManager: training ", unit)
        if self.bot.can_afford(unit):
            trainers = self.trained_at[unit]

            if UnitTypeId.WARPGATE in trainers and self.bot.units(UnitTypeId.WARPGATE).ready.exists:
                print('Training ' + str(unit) + ' using Warpgate')
                for warpgate in self.bot.units(UnitTypeId.WARPGATE):
                    abilities = await self.bot.get_available_abilities(warpgate)
                    if AbilityId.WARPGATETRAIN_ZEALOT in abilities:
                        pos = choice(self.bot.units(UnitTypeId.PYLON)).position.to2.random_on_distance(4)
                        placement = await self.bot.find_placement(AbilityId.WARPGATETRAIN_STALKER, pos, placement_step=1)
                        if placement is None:
                            print('can\'t place unit')
                            return 
                        self.actions.append(warpgate.warp_in(UnitTypeId.STALKER, placement))

            for trainer in trainers:
                buildings = sorted(self.bot.units(trainer).ready, key=lambda x: len(x.orders))
                for building in buildings:
                    
                    # Free spot in queue
                    if len(building.orders) >= max_queue:
                        continue

                    self.actions.append(building.train(unit))
                    return

    async def research(self, upgrade):
        buildings = self.bot.units(self.researched_at[upgrade]).ready
        for i in range(len(buildings)):
            building = buildings[i]
            if len(building.orders) == 0 or i == len(buildings) - 1:
                print("BuildingManager: researching ", upgrade)
                self.actions.append(building.research(upgrade))
                return

    async def can_train(self, unit_type, must_be_ready=True, must_afford=True, max_queue=1):
        # Requirements not satisfied
        if not self.unit_requirements_satisfied(unit_type):
            print('Requirements not satisfied for ' + str(unit_type))
            return False

        # Can't afford
        if must_afford and not self.bot.can_afford(unit_type):
            print('Not enough resources for ' + str(unit_type))
            return False

        # Can an archon be morphed?
        if unit_type == UnitTypeId.ARCHON:
            return self.can_morph(UnitTypeId.ARCHON)

        # Can interceptors be built?
        if unit_type == UnitTypeId.INTERCEPTOR:
            return self.bot.units(UnitTypeId.CARRIER).exists

        trainers = self.trained_at[unit_type]

        # Can it be trained using a warpgate?
        if UnitTypeId.WARPGATE in trainers and self.bot.units(UnitTypeId.WARPGATE).ready.exists:
            if not must_be_ready:
                return True

            if self.bot.units(UnitTypeId.WARPGATE).exists and self.bot.units(UnitTypeId.WARPGATE).ready.exists:
                for warpgate in self.bot.units(UnitTypeId.WARPGATE):
                    abilities = await self.bot.get_available_abilities(warpgate)
                    if AbilityId.WARPGATETRAIN_ZEALOT in abilities:
                        return True

        for trainer in trainers:
            if self.bot.units(trainer).exists:
                if not must_be_ready:
                    return True
                
                if self.bot.units(trainer).ready.exists:
                    for building in self.bot.units(trainer).ready:
                        # Free spot in queue
                        if len(building.orders) >= max_queue:
                            continue
                        else:
                            return True
        
        return False

    def unit_requirements_satisfied(self, unit_type):
        if unit_type in self.unit_requirements:
            for requirement in self.unit_requirements[unit_type]:
                # Special case with warpgate and gateway
                if requirement == UnitTypeId.GATEWAY \
                        and not (
                        (self.bot.units(UnitTypeId.GATEWAY).exists and self.bot.units(UnitTypeId.GATEWAY).ready.exists) \
                        or 
                        (self.bot.units(UnitTypeId.WARPGATE).exists and self.bot.units(UnitTypeId.WARPGATE).ready.exists)
                        ):
                    return False
                else:
                    continue
                
                if not self.bot.units(requirement).exists \
                        and not self.bot.units(requirement).ready.exists:
                    return False

            return True
        else:
            return True

    def can_upgrade(self, upgrade_type, must_be_ready=True, must_afford=True):
        return False

    def can_morph(self, morph):
        if morph == self.bot.units(UnitTypeId.ARCHON) and (len(self.bot.units(UnitTypeId.HIGHTEMPLAR)) >= 2 or len(self.bot.units(UnitTypeId.DARKTEMPLAR)) >= 2):
            return True
        return False

    def can_add_on(self, add_on, must_afford=True):
        return False

    def is_legal_training_action(self, unit_type):
        if unit_type == UnitTypeId.NUKE:
            return False
        return self.can_train(unit_type, must_be_ready=False, must_afford=False)

    def is_legal_upgrade_action(self, upgrade_type):
        return self.can_upgrade(upgrade_type, must_be_ready=False, must_afford=False)

    def is_legal_build_action(self, build_type):
        if build_type == UnitTypeId.ASSIMILATOR and self.bot.units(UnitTypeId.ASSIMILATOR).amount >= self.bot.units(UnitTypeId.NEXUS).amount * 2:
            return self.worker_manager.is_building(UnitTypeId.NEXUS)
        if build_type not in self.requirements:
            return True
        for requirement in self.requirements[build_type]:
            if self.bot.units(requirement).amount == 0 and not self.worker_manager.is_building(requirement):
                return False
        return True
