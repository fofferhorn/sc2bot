from sc2bot.managers.interfaces import AssaultManager
from sc2.ids.unit_typeid import UnitTypeId
from sc2.units import Units


class ValueBasedAssaultManager(AssaultManager):

    def __init__(self, bot, army_manager, worker_manager):
        super().__init__(bot, army_manager, worker_manager)

    async def run(self):

        if self.bot.iteration % 2 == 0:

            # Target
            opp_base = self.bot.known_enemy_structures.random_or(self.bot.enemy_start_locations[0]).position
            opp_threats = self.bot.known_enemy_structures.prefer_close_to(self.bot.enemy_start_locations[0])
            own_base = self.bot.start_location
            target = opp_threats[0] if len(opp_threats) > 0 else opp_base

            # Should attack
            own_ground_to_ground, own_ground_to_air, own_air_to_air, own_air_to_ground = self.army_value(self.bot.units())
            opp_ground_to_ground, opp_ground_to_air, opp_air_to_air, opp_air_to_ground = self.army_value(Units(self.bot.enemy_units.values(), self.bot.game_data()), include_buildings=True)

            own_ground_to_ground = own_ground_to_ground * 0.9
            own_ground_to_air = own_ground_to_air * 0.9
            own_air_to_air = own_air_to_air * 0.9
            own_air_to_ground = own_air_to_ground * 0.9

            #print("Own army value: ", own_ground_to_ground + own_ground_to_air + own_air_to_air + own_air_to_ground)
            #print("Opp army value: ", opp_ground_to_ground + opp_ground_to_air + opp_air_to_air + opp_air_to_ground)

            if own_air_to_air + own_air_to_ground + own_ground_to_air + own_ground_to_ground > opp_air_to_air + opp_air_to_ground + opp_ground_to_air + opp_ground_to_ground:
                #print("AssaultManager: Attacking with all units", target)
                await self.army_manager.attack(target, None)
            elif own_air_to_ground > opp_ground_to_air and own_air_to_air > opp_air_to_air:
                #print("AssaultManager: Attacking with flying units", target)
                await self.army_manager.attack(target, [unit.type_id for unit in self.bot.units.flying()])
            elif own_ground_to_ground > opp_ground_to_ground and own_ground_to_air > opp_air_to_ground:
                #print("AssaultManager: Attacking with ground units", target)
                await self.army_manager.attack(target, [unit.type_id for unit in self.bot.units() if not unit.is_flying])
            else:
                #print("AssaultManager: defending with everything", target)
                await self.army_manager.defend(own_base, None)

    def army_value(self, units, include_buildings=False):
        air_to_air = 0
        air_to_ground = 0
        ground_to_ground = 0
        ground_to_air = 0
        for unit in units:
            if unit.type_id not in [UnitTypeId.SCV, UnitTypeId.MULE]:
                if include_buildings == unit.is_structure or not unit.is_structure:
                    #cost = self.bot.game_data().calculate_ability_cost(u.creation_ability)
                    ##cost = cost.minerals + cost.gas
                    if unit.can_attack_ground:
                        value = unit.health * unit.air_dps
                        if unit.is_flying:
                            air_to_ground += value
                        else:
                            ground_to_ground += value
                    if unit.can_attack_air:
                        value = unit.health * unit.ground_dps
                        if unit.is_flying:
                            air_to_air += value
                        else:
                            ground_to_air += value

        return ground_to_ground, ground_to_air, air_to_air, air_to_ground
