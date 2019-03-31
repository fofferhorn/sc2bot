
"""
A modular StarCraft II bot.
"""

import time
import math
import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

import os

from absl import app
from absl import flags
import sys
from importlib import reload

FLAGS = flags.FLAGS

flags.DEFINE_string(name = 'model_name', default = None, help = 'The name of a trained neural network model to use as a production manager.')
flags.DEFINE_string(name = 'maxes_path', default = 'maxes.txt', help = 'The name of the files that contains the max values to be used for min-max normalization.')

FLAGS(sys.argv)

# from sc2bot.managers.terran_managers.army.simple_army_manager import SimpleArmyManager
# from sc2bot.managers.terran_managers.army.advanced_army_manager import AdvancedArmyManager
# from sc2bot.managers.terran_managers.building.simple_building_manager import SimpleBuildingManager
# from sc2bot.managers.terran_managers.production.marine_production_manager import MarineProductionManager
# from sc2bot.managers.terran_managers.production.reaper_marine_production_manager import ReaperMarineProductionManager
# from sc2bot.managers.terran_managers.production.orbital_production_manager import OrbitalProductionManager
# from sc2bot.managers.terran_managers.production.mlp_production_manager import MLPProductionManager
# from sc2bot.managers.terran_managers.production.mlp_model import Net
# from sc2bot.managers.terran_managers.scouting.simple_scouting_manager import SimpleScoutingManager
# from sc2bot.managers.terran_managers.assault.simple_assault_manager import SimpleAssaultManager
# from sc2bot.managers.terran_managers.assault.value_based_assault_manager import ValueBasedAssaultManager
# from sc2bot.managers.terran_managers.worker.simple_worker_manager import SimpleWorkerManager

import sc2bot.managers.protoss_managers.army.advanced_army_manager as advanced_army_manager
import sc2bot.managers.protoss_managers.assault.value_based_assault_manager as value_based_assault_manager
import sc2bot.managers.protoss_managers.building.simple_building_manager as simple_building_manager
import sc2bot.managers.protoss_managers.production.stalker_rush_production_manager as stalker_rush_production_manager
import sc2bot.managers.protoss_managers.production.ml_production_manager as ml_production_manager
import sc2bot.managers.protoss_managers.scouting.simple_scouting_manager as simple_scouting_manager
import sc2bot.managers.protoss_managers.worker.simple_worker_manager as simple_worker_manager

# class TerranBot(sc2.BotAI):

#     def __init__(self):
#         super().__init__()
#         self.iteration = 0
#         self.worker_manager = SimpleWorkerManager(self)
#         self.army_manager = AdvancedArmyManager(self)
#         self.assault_manager = ValueBasedAssaultManager(self, self.army_manager, self.worker_manager)
#         self.building_manager = SimpleBuildingManager(self, self.worker_manager)
#         # self.production_manager = MLPProductionManager(self, self.worker_manager, self.building_manager, "models_without_time/TvZ_3x256_no_frame_id_1552989984_state_dict")
#         # self.production_manager = MLPProductionManager(self, self.worker_manager, self.building_manager, "TvZ_3x256_features_2D_1552906112", features=[0.5, 0.5])
#         self.production_manager = MarineProductionManager(self, self.worker_manager, self.building_manager)
#         # self.production_manager = ReaperMarineProductionManager(self, self.worker_manager, self.building_manager)
#         # self.production_manager = OrbitalProductionManager(self, self.worker_manager, self.building_manager)
#         self.scouting_manager = SimpleScoutingManager(self, self.worker_manager, self.building_manager)
#         self.managers = [self.scouting_manager, self.production_manager, self.building_manager, self.assault_manager, self.army_manager, self.worker_manager]
#         self.enemy_units = {}
#         self.own_units = {}
#         print("Bot is ready")

#     async def on_step(self, iteration):
#         '''
#         Calls
#         :param iteration:
#         :return:
#         '''

#         #print("Step: ", self.state.observation.game_loop)

#         for unit in self.known_enemy_units | self.known_enemy_structures:
#             self.enemy_units[unit.tag] = unit

#         self.iteration += 1
#         # print("-- Production Manager")
#         await self.production_manager.execute()
#         # print("-- Scouting Manager")
#         await self.scouting_manager.execute()
#         # print("-- Assault Manager")
#         await self.assault_manager.execute()
#         # print("-- Army Manager")
#         await self.army_manager.execute()
#         # print("-- Worker Manager")
#         await self.worker_manager.execute()
#         # print("-- Building Manager")
#         await self.building_manager.execute()

#     def game_data(self):
#         return self._game_data

#     def client(self):
#         return self._client

#     async def get_next_expansion(self):
#         """Find next expansion location."""

#         closest = None
#         distance = math.inf
#         for el in self.expansion_locations:
#             def is_near_to_expansion(t):
#                 return t.position.distance_to(el) < self.EXPANSION_GAP_THRESHOLD

#             if any(map(is_near_to_expansion, self.townhalls)):
#                 # already taken
#                 continue

#             startp = self._game_info.player_start_location
#             d = startp.distance_to(el)
#             if d is None:
#                 continue

#             if d < distance:
#                 distance = d
#                 closest = el

#         return closest

#     async def on_unit_destroyed(self, unit_tag):
#         if unit_tag in self.own_units:
#             del self.own_units[unit_tag]
#         if unit_tag in self.enemy_units:
#             del self.enemy_units[unit_tag]
#         for manager in self.managers:
#             await manager.on_unit_destroyed(unit_tag)

#     async def on_unit_created(self, unit):
#         self.own_units[unit.tag] = unit
#         for manager in self.managers:
#             await manager.on_unit_created(unit)

#     async def on_building_construction_started(self, unit):
#         self.own_units[unit.tag] = unit
#         for manager in self.managers:
#             await manager.on_building_construction_started(unit)

#     async def on_building_construction_complete(self, unit):
#         for manager in self.managers:
#             await manager.on_building_construction_complete(unit)


class ProtossBot(sc2.BotAI):
    def __init__(self, model_name = None):
        super().__init__()
        self.iteration = 0
        self.worker_manager = simple_worker_manager.SimpleWorkerManager(self)
        self.army_manager = advanced_army_manager.AdvancedArmyManager(self)
        self.assault_manager = value_based_assault_manager.ValueBasedAssaultManager(self, self.army_manager, self.worker_manager)
        self.building_manager = simple_building_manager.SimpleBuildingManager(self, self.worker_manager)
        self.scouting_manager = simple_scouting_manager.SimpleScoutingManager(self, self.worker_manager, self.building_manager)

        if model_name is None:
            self.production_manager = stalker_rush_production_manager.StalkerRushProductionManager(self, self.worker_manager, self.building_manager)
        else:
            self.production_manager = ml_production_manager.MLProductionManager(
                self, 
                self.worker_manager, 
                self.building_manager, 
                model_name, 
                44
            )

        self.managers = [self.scouting_manager, self.production_manager, self.building_manager, self.assault_manager, self.army_manager, self.worker_manager]
        self.enemy_units = {}
        self.own_units = {}
        print("Bot is ready")


    async def on_step(self, iteration):
        '''
        Calls
        :param iteration:
        :return:
        '''

        #print("Step: ", self.state.observation.game_loop)

        for unit in self.known_enemy_units | self.known_enemy_structures:
            self.enemy_units[unit.tag] = unit

        self.iteration += 1
        # print("-- Production Manager")
        await self.production_manager.execute()
        # print("-- Scouting Manager")
        await self.scouting_manager.execute()
        # print("-- Assault Manager")
        await self.assault_manager.execute()
        # print("-- Army Manager")
        await self.army_manager.execute()
        # print("-- Worker Manager")
        await self.worker_manager.execute()
        # print("-- Building Manager")
        await self.building_manager.execute()


    def game_data(self):
        return self._game_data

    def client(self):
        return self._client

    
    async def get_next_expansion(self):
        closest = None
        distance = math.inf
        for el in self.expansion_locations:
            def is_near_to_expansion(t):
                return t.position.distance_to(el) < self.EXPANSION_GAP_THRESHOLD

            if any(map(is_near_to_expansion, self.townhalls)):
                # already taken
                continue

            startp = self._game_info.player_start_location
            d = startp.distance_to(el)
            if d is None:
                continue

            if d < distance:
                distance = d
                closest = el

        return closest


    async def on_unit_destroyed(self, unit_tag):
        if unit_tag in self.own_units:
            del self.own_units[unit_tag]
        if unit_tag in self.enemy_units:
            del self.enemy_units[unit_tag]
        for manager in self.managers:
            await manager.on_unit_destroyed(unit_tag)


    async def on_unit_created(self, unit):
        self.own_units[unit.tag] = unit
        for manager in self.managers:
            await manager.on_unit_created(unit)


    async def on_building_construction_started(self, unit):
        self.own_units[unit.tag] = unit
        for manager in self.managers:
            await manager.on_building_construction_started(unit)


    async def on_building_construction_complete(self, unit):
        for manager in self.managers:
            await manager.on_building_construction_complete(unit)


def main(argv):
    replay_name = f"replays/sc2bot_{int(time.time())}.sc2replay"
    # # Multiple difficulties for enemy bots available https://github.com/Blizzard/s2client-api/blob/ce2b3c5ac5d0c85ede96cef38ee7ee55714eeb2f/include/sc2api/sc2_gametypes.h#L30
    # sc2.run_game(sc2.maps.get("(2)CatalystLE"),
    #              players=[Bot(Race.Protoss, ProtossBot(FLAGS.model_name)), Computer(Race.Protoss, Difficulty.Medium)],
    #              save_replay_as=replay_name,
    #              realtime=False)

    player_config = [Bot(Race.Protoss, ProtossBot(FLAGS.model_name)), Computer(Race.Protoss, Difficulty.Medium)]

    gen = sc2.main._host_game_iter(
        sc2.maps.get("(2)CatalystLE"),
        player_config,
        save_replay_as=replay_name,
        realtime=False
    )

    games_played = 1

    while True:
        print('--------------------------------------')
        print('Starting game number ' + str(games_played))
        print('--------------------------------------')

        r = next(gen)

        reload(advanced_army_manager)
        reload(value_based_assault_manager)
        reload(simple_building_manager)
        reload(stalker_rush_production_manager)
        reload(ml_production_manager)
        reload(simple_scouting_manager)
        reload(simple_worker_manager)
        player_config[0].ai = ProtossBot(FLAGS.model_name)
        gen.send(player_config)

        games_played += 1

    # # Multiple difficulties for enemy bots available https://github.com/Blizzard/s2client-api/blob/ce2b3c5ac5d0c85ede96cef38ee7ee55714eeb2f/include/sc2api/sc2_gametypes.h#L30
    # player_config = [Bot(Race.Protoss, ProtossBot(FLAGS.model_name)), Computer(Race.Protoss, Difficulty.Medium)]

    # for i in range(1,101):
    #     print('--------------------------------------')
    #     print('Starting game number ' + str(i))
    #     print('--------------------------------------')

    #     replay_name = f"sc2bot_{int(time.time())}.sc2replay"
    #     sc2.run_game(sc2.maps.get("(2)CatalystLE"),
    #                 players=player_config,
    #                 save_replay_as=replay_name,
    #                 realtime=False)

    #     reload(AdvancedArmyManager)
    #     reload(ValueBasedAssaultManager)
    #     reload(SimpleBuildingManager)
    #     reload(StalkerRushProductionManager)
    #     reload(MLProductionManager)
    #     reload(SimpleScoutingManager)
    #     reload(SimpleWorkerManager)
    #     player_config[0].ai = ProtossBot(FLAGS.model_name)


if __name__ == '__main__':
    app.run(main)
