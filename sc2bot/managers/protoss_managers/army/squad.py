from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
import math
from sc2.units import Units
from sc2.unit import Unit
from sc2.position import Point2, Point3
import random


class Squad:

    def __init__(self, bot, target, unit_types, order):
        self.bot = bot
        self.target = target
        self.order = order
        self.unit_types = unit_types
        self.units = None
        self.actions = []
        self.defensive_ramp = None
        self.defending_position = None

    async def run(self):
        if self.defensive_ramp is None or self.bot.iteration % 50 == 0 and self.bot.townhalls.exists:
            front_base = self.bot.townhalls.closest_to(self.bot.enemy_start_locations[0])
            distance_between_bases = front_base.distance_to(self.bot.enemy_start_locations[0])
            closest_distance_to_home = 100000
            for ramp in self.bot.game_info.map_ramps:
                distance_to_enemy = ramp.top_center.distance_to(self.bot.enemy_start_locations[0])
                distance_to_us = ramp.top_center.distance_to(front_base)
                distance_to_home = ramp.top_center.distance_to(self.bot.start_location)
                if distance_to_enemy < distance_between_bases:
                    if distance_to_home < closest_distance_to_home:
                        closest_distance_to_home = distance_to_home
                        self.defensive_ramp = ramp
                        dir_vector = ramp.bottom_center.direction_vector(ramp.top_center)
                        self.defending_position = ramp.top_center + dir_vector*4

        if len(self.actions) > 0:
            actions = [action for action in self.actions]
            self.actions = []
            await self.bot.do_actions(actions)
        else:
            if self.order == "attack":
                centroid = self.units.closest_to(self.units.center).position if self.units.amount > 0 else None
                for unit in self.units:
                    squad_size = self.units.amount + 2
                    distance = unit.distance_to(centroid)
                    # print("Squad size: ", squad_size, ", distance: ", distance)
                    if distance > squad_size/2:
                        #self.actions.append(unit.move(self.units.center))
                        if unit.type_id == UnitTypeId.SIEGETANKSIEGED:
                            self.actions.append(unit(AbilityId.UNSIEGE_UNSIEGE))
                        else:
                            self.actions.append(unit.move(centroid))
                    else:
                        self.unit_move(unit, self.target, self.order)
            elif self.order == "defend":
                for unit in self.units:
                    self.unit_move(unit, self.target, self.order)
            elif self.order == "harass":
                for unit in self.units:
                    self.harass_move(unit, self.target)

    def harass_move(self, unit, target):
        harassment_home = Point2((self.bot.start_location.y, self.bot.enemy_start_locations[0].x))
        harass_target = self.bot.known_enemy_structures.closest_to(harassment_home) if self.bot.known_enemy_structures.exists else self.bot.enemy_start_locations[0]

        if abs(unit.position.x - harassment_home.x) > 15:
            if unit.is_idle:
                self.actions.append(unit.move(harassment_home))
        elif unit.distance_to(target) > 25:
            if self.bot.iteration % 10 == 0:
                self.actions.append(unit.move(target))
        else:
            self.unit_move(unit, harass_target, order="harass", retreat_to=harassment_home, exclude_buildings=True)

    def unit_move(self, unit, target, order="attack", retreat_to=None, exclude_buildings=False):
        if retreat_to is None:
            retreat_to = self.bot.start_location

        if not exclude_buildings:
            closest_enemy_ground_unit = self.bot.known_enemy_units.not_flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).closest_to(
                unit) if self.bot.known_enemy_units.not_flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).exists else None
            closest_enemy_air_unit = self.bot.known_enemy_units.flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).closest_to(
                unit) if self.bot.known_enemy_units.flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).exists else None
            closest_enemy_unit = None
        else:
            closest_enemy_ground_unit = self.bot.known_enemy_units.not_structure.not_flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).closest_to(
                unit) if self.bot.known_enemy_units.not_flying.not_structure.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).exists else None
            closest_enemy_air_unit = self.bot.known_enemy_units.not_structure.flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).closest_to(
                unit) if self.bot.known_enemy_units.not_structure.flying.exclude_type(UnitTypeId.EGG).exclude_type(UnitTypeId.LARVA).exists else None
            closest_enemy_unit = None

        # Find closest enemy unit that the unit can attack
        if closest_enemy_ground_unit is not None and unit.can_attack_ground:
            closest_enemy_unit = closest_enemy_ground_unit
        if closest_enemy_air_unit is not None and unit.can_attack_air:
            if closest_enemy_unit is None or closest_enemy_air_unit.distance_to(unit.position) < closest_enemy_unit.distance_to(unit.position):
                closest_enemy_unit = closest_enemy_air_unit

        range_own = 0
        if closest_enemy_unit is not None:
            range_own = unit.ground_range if not closest_enemy_unit.is_flying else unit.air_range

        # TODO: Is the closest enemy closer to our base than us -> then get mad?
        # TODO: Define a more general defensive position, maybe even a list of them

        # Decide what to do
        if order == "attack" or (closest_enemy_unit is not None and closest_enemy_unit.distance_to(unit.position) < range_own):
            # Basic attack
            if closest_enemy_unit is not None:
                self._basic_attack(unit, closest_enemy_unit)
            else:
                self.actions.append(unit.move(target))

        elif order == "harass":
            if closest_enemy_unit is not None:
                if closest_enemy_ground_unit.ground_range >= unit.ground_range * 0.9:
                    self.actions.append(unit.move(retreat_to))
                else:
                    self._basic_attack(unit, closest_enemy_unit)
            elif self.bot.iteration % 200 == 0:
                self.actions.append(unit.move(target))

        elif order == "defend":
            if random.randint(0, len(self.units)) == 0:
                # Give some slack if kinda close
                if unit.distance_to(self.defending_position) <= 15 and self.bot.iteration % 20 != 0:
                    return

                # Otherwise hurry up
                if unit.distance_to(self.defending_position) > 5:
                    self.actions.append(unit.move(self.defending_position))

    def _basic_attack(self, unit, closest_enemy_unit):
        _range = unit.air_range if closest_enemy_unit.is_flying else unit.ground_range
        distance = closest_enemy_unit.distance_to(unit)
        if distance < _range * 0.8 and closest_enemy_unit.distance_to(self.bot.start_location) > unit.distance_to(self.bot.start_location):
            self.actions.append(unit.move(self.bot.start_location))
        elif not unit.is_attacking:
            self.actions.append(unit.attack(closest_enemy_unit))