from sc2bot.managers.interfaces import ProductionManager
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId
from sc2.ids.upgrade_id import UpgradeId
import sc2bot.constants as c

import math
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import normalize
from tensorflow.keras import metrics, optimizers, layers, losses, models, utils
from tensorflow.keras import backend as K

import numpy as np

def top_3_categorical_accuracy(y_true, y_pred):
    return metrics.top_k_categorical_accuracy(y_true, y_pred, k=3)

def top_1_categorical_accuracy(y_true, y_pred):
    return metrics.top_k_categorical_accuracy(y_true, y_pred, k=1)

class MLProductionManager(ProductionManager):
    def __init__(self, bot, worker_manager, building_manager, model_name, request_frequency):
        super().__init__(bot, worker_manager, building_manager)
        self.next_iteration = 0
        self.model = models.load_model(model_name, {"top_1_categorical_accuracy": top_1_categorical_accuracy, "top_3_categorical_accuracy": top_3_categorical_accuracy})
        self.observation = None

        print("Production manager ready")


    async def run(self):
        print('________________________________________________________________________________')

        state = self.bot.state

        self.observation = state.observation

        input_data = self.prepare_input()

        print('--------------------------------------------------------------------------------')

        prediction = self.model.predict(input_data, verbose = 0)

        await self.carry_out_prediction(prediction[0])

        print('________________________________________________________________________________')
        

    def prepare_input(self):
        resources = self.get_resources()
        upgrades = self.get_upgrades()
        in_progress = self.get_units_in_progress()
        friendly_unit_list = self.get_friendly_unit_list()
        enemy_unit_list = self.get_enemy_unit_list()

        input_data = []
        input_data.append(self.observation.game_loop)   # 1
        input_data += resources                         # 9
        input_data += upgrades                          # 26
        input_data += in_progress                       # 70
        input_data += friendly_unit_list                # 44
        input_data += enemy_unit_list                   # 44

        print('Time step (step/seconds): ' + str(self.observation.game_loop) + '/' + str(self.observation.game_loop/22.4))
        print('Resources (minerals, vespene, food(cap, used, army, workers), idle_workers, army_count, warp_gates): ' + str(resources[0]) + ', ' + str(resources[1]) + ', (' + str(resources[2]) + ', ' + str(resources[3]) + ', ' + str(resources[4]) + ', ' + str(resources[5]) + '), ' + str(resources[6]) + ', ' + str(resources[7]) + ', ' + str(resources[8]))
        print('In progress: ' + str(self.in_progress_dic(in_progress)))
        print('Upgrades: ' + str(self.upgrades_dic(upgrades)))
        print('Friendly buildings: ' + str(self.buildings_dic(friendly_unit_list)))
        print('Friendly units: ' + str(self.units_dic(friendly_unit_list)))
        print('Enemy buildings: ' + str(self.buildings_dic(enemy_unit_list)))
        print('Enemy units: ' + str(self.units_dic(enemy_unit_list)))

        input_data = keras.normalize(input_data, axis=-1, order=2)
        # input_data = min_max_norm(input_data, self.maxes)

        return np.array([input_data])


    def in_progress_dic(self, in_progress):
        in_progress_dic = {}
        for i in range(len(in_progress)):
            amount = in_progress[i]
            if amount > 0:
                in_progress_name = c.protoss_in_progress_to_name_mapper.get(i)
                in_progress_dic[in_progress_name] = amount
        return in_progress_dic


    def buildings_dic(self, units):
        units_dic = {}
        for i in range(16):
            amount = units[i]
            if amount > 0:
                unit_name = c.protoss_unit_to_name_mapper.get(i)
                units_dic[unit_name] = amount
        return units_dic


    def units_dic(self, units):
        buidlings_dic = {}
        for i in range(16, len(units)):
            amount = units[i]
            if amount > 0:
                buidling_name = c.protoss_unit_to_name_mapper.get(i)
                buidlings_dic[buidling_name] = amount
        return buidlings_dic


    def upgrades_dic(self, upgrades):
        upgrades_dic = {}
        for i in range(len(upgrades)):
            amount = upgrades[i]
            if amount > 0:
                upgrade_name = c.protoss_upgrade_to_name_mapper.get(i)
                upgrades_dic[upgrade_name] = amount
        return upgrades_dic


    def get_resources(self):
        resources = [
            self.observation.player_common.minerals,
            self.observation.player_common.vespene,
            self.observation.player_common.food_cap,
            self.observation.player_common.food_used,
            self.observation.player_common.food_army,
            self.observation.player_common.food_workers,
            self.observation.player_common.idle_worker_count,
            self.observation.player_common.army_count,
            self.observation.player_common.warp_gate_count
        ]

        return resources
    

    def get_units_in_progress(self):
        # Number of each building, unit and upgrade in progress
        in_progress_list = [0] * (44 + 26)

        for unit in self.observation.raw_data.units:
            if unit.alliance == 1:
                # Something is being built/something in the map. E.g. a building being built.
                if unit.build_progress < 1:
                    protoss_unit = c.protoss_in_progress_unit_mapper.get(unit.unit_type)
                    in_progress_list[protoss_unit] += 1

                # Something is being built/something by something else. E.g. a building training a unit.
                if unit.orders is not None:
                    for order in unit.orders:
                        # The unit being built by e.g. a building.
                        in_progress_entity = c.protoss_in_progress_ability_to_unit_mapper.get(order.ability_id) 
            
                        if in_progress_entity is not None:
                            in_progress_list[in_progress_entity] += 1

        return in_progress_list


    def get_friendly_unit_list(self):
        # Amount of units for each protoss unit
        unit_list = [0] * 44

        for unit in self.observation.raw_data.units:
            if unit.alliance == 1 and unit.build_progress == 1.0:
                protoss_unit = c.protoss_unit_mapper.get(unit.unit_type)
                if protoss_unit is not None:
                    unit_list[protoss_unit] += 1

        return unit_list


    def get_enemy_unit_list(self):
        # Amount of units for each protoss unit
        unit_list = [0] * 44

        for unit in self.observation.raw_data.units:
            if unit.alliance == 4:
                unit_index = c.protoss_unit_mapper.get(unit.unit_type)
                if unit_index is not None:
                    unit_list[unit_index] += 1

        return unit_list


    def get_upgrades(self):
        upgrades = [0] * 26

        for upgrade_id in self.observation.raw_data.player.upgrade_ids:
            protoss_upgrade = c.protoss_upgrade_mapper.get(upgrade_id)
            if protoss_upgrade is not None:
                upgrades[protoss_upgrade] += 1
        
        return upgrades


    async def carry_out_prediction(self, prediction):
        prediction_action = np.argmax(prediction)

        # random = np.random.random_sample()

        # # Take a random action from the predictions based on the likelyhood in the output.
        # _sum = 0.0
        # for i in range(len(prediction)):
        #     if _sum <= random <= _sum + prediction[i]:
        #         print('Randomly chose action: ' + str(i))
        #         prediction_action = i
        #         break
        #     _sum += prediction[i]

        macro_action = None

        # It's a special case with the 5 different level upgrades
        if prediction_action == 27:
            if UpgradeId.PROTOSSAIRARMORSLEVEL3 in self.bot.state.upgrades:
                return
            elif UpgradeId.PROTOSSAIRARMORSLEVEL2 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSAIRARMORSLEVEL3
            elif UpgradeId.PROTOSSAIRARMORSLEVEL1 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSAIRARMORSLEVEL2
            else:
                macro_action = UpgradeId.PROTOSSAIRARMORSLEVEL1
        elif prediction_action == 28:
            if UpgradeId.PROTOSSAIRWEAPONSLEVEL3 in self.bot.state.upgrades:
                return
            elif UpgradeId.PROTOSSAIRWEAPONSLEVEL2 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSAIRWEAPONSLEVEL3
            elif UpgradeId.PROTOSSAIRWEAPONSLEVEL1 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSAIRWEAPONSLEVEL2
            else: 
                macro_action = UpgradeId.PROTOSSAIRWEAPONSLEVEL1
        elif prediction_action == 29:
            if UpgradeId.PROTOSSGROUNDARMORSLEVEL3 in self.bot.state.upgrades:
                return
            elif UpgradeId.PROTOSSGROUNDARMORSLEVEL2 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSGROUNDARMORSLEVEL3
            elif UpgradeId.PROTOSSGROUNDARMORSLEVEL1 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSGROUNDARMORSLEVEL2
            else:
                macro_action = UpgradeId.PROTOSSGROUNDARMORSLEVEL1
        elif prediction_action == 30:
            if UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3 in self.bot.state.upgrades:
                return
            elif UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3
            elif UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2
            else:
                macro_action = UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1
        elif prediction_action == 31:
            if UpgradeId.PROTOSSSHIELDSLEVEL3 in self.bot.state.upgrades:
                return
            elif UpgradeId.PROTOSSSHIELDSLEVEL2 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSSHIELDSLEVEL3
            elif UpgradeId.PROTOSSSHIELDSLEVEL1 in self.bot.state.upgrades:
                macro_action = UpgradeId.PROTOSSSHIELDSLEVEL2
            else:
                macro_action = UpgradeId.PROTOSSSHIELDSLEVEL1
        else:
            macro_action = c.protoss_output_to_action_mapper.get(prediction_action)

        macro_action_type = c.action_to_type_mapper.get(macro_action)

        print('Action predicted: ' + str(macro_action) + ' of type: ' + macro_action_type)

        if macro_action_type == 'upgrade' \
                and macro_action not in self.bot.state.upgrades \
                and self.bot.can_afford(macro_action):
            await self.building_manager.research(macro_action)
            return
        elif macro_action_type == 'build' \
                and self.bot.can_afford(macro_action):
            await self.worker_manager.build(macro_action)
            return
        elif macro_action_type == 'train' \
                and await self.building_manager.can_train(macro_action) \
                and self.bot.can_afford(macro_action):
            await self.building_manager.train(macro_action)
            return
        elif macro_action_type == 'ability':
            return
        else:
            return