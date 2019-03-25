from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId

# Mapping of unit_id to index in list.
protoss_unit_mapper = {
    # Buildings
    61: 0,     # Assimilator
    72: 1,     # CyberneticsCore
    69: 2,     # DarkShrine
    64: 3,     # FleetBeacon
    63: 4,     # Forge
    62: 5,     # Gateway
    59: 6,     # Nexus
    66: 7,     # PhotonCannon
    60: 8,     # Pylon
    70: 9,     # RoboticsBay
    71: 10,    # RoboticsFacility
    1910: 11,  # ShieldBattery
    67: 12,    # Stargate
    68: 13,    # TemplarArchive
    65: 14,    # TwilightCouncil
    133: 15,   # WarpGate

    # Units
    84: 16,     # Probe
    73: 17,     # Zealot
    77: 18,     # Sentry
    311: 19,    # Adept
    74: 20,     # Stalker
    75: 21,     # HighTemplar
    76: 22,     # DarkTemplar
    141: 23,    # Archon
    4: 24,      # Colossus
    694: 25,    # Disruptor
    82: 26,     # Observer
    83: 27,     # Immortal
    81: 28,     # WarpPrism
    78: 29,     # Phoenix
    495: 30,    # Oracle
    80: 31,     # VoidRay
    496: 32,    # Tempest
    79: 33,     # Carrier
    85: 34,     # Interceptor
    10: 35,     # Mothership
    488: 36,    # MothershipCore

    # Abilities
    801: 37,    # AdeptPhaseShift
    135: 38,    # ForceField
    1911: 39,   # ObserverSurveillanceMode
    733: 40,    # DisruptorPhased
    136: 41,    # WarpPrismPhasing
    894: 42,    # PylonOvercharged
    732: 43     # StasisTrap
}

# Mapping of upgrades (ability_ids) to indexes in list
protoss_upgrade_mapper = {
    1: 0,       # CARRIERLAUNCHSPEEDUPGRADE
    39: 1,      # PROTOSSGROUNDWEAPONSLEVEL1
    40: 2,      # PROTOSSGROUNDWEAPONSLEVEL2
    41: 3,      # PROTOSSGROUNDWEAPONSLEVEL3
    42: 4,      # PROTOSSGROUNDARMORSLEVEL1
    43: 5,      # PROTOSSGROUNDARMORSLEVEL2
    44: 6,      # PROTOSSGROUNDARMORSLEVEL3
    45: 7,      # PROTOSSSHIELDSLEVEL1
    46: 8,      # PROTOSSSHIELDSLEVEL2
    47: 9,      # PROTOSSSHIELDSLEVEL3
    48: 10,     # OBSERVERGRAVITICBOOSTER
    49: 11,     # GRAVITICDRIVE
    50: 12,     # EXTENDEDTHERMALLANCE
    52: 13,     # PSISTORMTECH
    78: 14,     # PROTOSSAIRWEAPONSLEVEL1
    79: 15,     # PROTOSSAIRWEAPONSLEVEL2
    80: 16,     # PROTOSSAIRWEAPONSLEVEL3
    81: 17,     # PROTOSSAIRARMORSLEVEL1
    82: 18,     # PROTOSSAIRARMORSLEVEL2
    83: 19,     # PROTOSSAIRARMORSLEVEL3
    84: 20,     # WARPGATERESEARCH
    86: 21,     # CHARGE
    87: 22,     # BLINKTECH
    99: 23,     # PHOENIXRANGEUPGRADE
    130: 24,    # ADEPTPIERCINGATTACK
    141: 25     # DARKTEMPLARBLINKUPGRADE
}

protoss_in_progress_unit_mapper = {
    # Buildings
    61: 0,     # Assimilator
    72: 1,     # CyberneticsCore
    69: 2,     # DarkShrine
    64: 3,     # FleetBeacon
    63: 4,     # Forge
    62: 5,     # Gateway
    59: 6,     # Nexus
    66: 7,     # PhotonCannon
    60: 8,     # Pylon
    70: 9,     # RoboticsBay
    71: 10,    # RoboticsFacility
    1910: 11,  # ShieldBattery
    67: 12,    # Stargate
    68: 13,    # TemplarArchive
    65: 14,    # TwilightCouncil
    133: 15,   # WarpGate

    # Units
    84: 16,     # Probe
    73: 17,     # Zealot
    77: 18,     # Sentry
    311: 19,    # Adept
    74: 20,     # Stalker
    75: 21,     # HighTemplar
    76: 22,     # DarkTemplar
    141: 23,    # Archon
    4: 24,      # Colossus
    694: 25,    # Disruptor
    82: 26,     # Observer
    83: 27,     # Immortal
    81: 28,     # WarpPrism
    78: 29,     # Phoenix
    495: 30,    # Oracle
    80: 31,     # VoidRay
    496: 32,    # Tempest
    79: 33,     # Carrier
    85: 34,     # Interceptor
    10: 35,     # Mothership
    488: 36,    # MothershipCore

    # Abilities
    801: 37,    # AdeptPhaseShift
    135: 38,    # ForceField
    1911: 39,   # ObserverSurveillanceMode
    733: 40,    # DisruptorPhased
    136: 41,    # WarpPrismPhasing
    894: 42,    # PylonOvercharged
    732: 43     # StasisTrap
}

protoss_in_progress_upgrade_mapper = {
    0: 44,      # CARRIERLAUNCHSPEEDUPGRADE
    1: 45,     # PROTOSSGROUNDWEAPONSLEVEL1
    2: 46,     # PROTOSSGROUNDWEAPONSLEVEL2
    3: 47,     # PROTOSSGROUNDWEAPONSLEVEL3
    4: 48,     # PROTOSSGROUNDARMORSLEVEL1
    5: 49,     # PROTOSSGROUNDARMORSLEVEL2
    6: 50,     # PROTOSSGROUNDARMORSLEVEL3
    7: 51,     # PROTOSSSHIELDSLEVEL1
    8: 52,     # PROTOSSSHIELDSLEVEL2
    9: 53,     # PROTOSSSHIELDSLEVEL3
    10: 54,     # OBSERVERGRAVITICBOOSTER
    11: 55,     # GRAVITICDRIVE
    12: 56,     # EXTENDEDTHERMALLANCE
    13: 57,     # PSISTORMTECH
    14: 58,     # PROTOSSAIRWEAPONSLEVEL1
    15: 59,     # PROTOSSAIRWEAPONSLEVEL2
    16: 60,     # PROTOSSAIRWEAPONSLEVEL3
    17: 61,     # PROTOSSAIRARMORSLEVEL1
    18: 62,     # PROTOSSAIRARMORSLEVEL2
    19: 63,     # PROTOSSAIRARMORSLEVEL3
    20: 64,     # WARPGATERESEARCH
    21: 65,     # CHARGE
    22: 66,     # BLINKTECH
    23: 67,     # PHOENIXRANGEUPGRADE
    24: 68,    # ADEPTPIERCINGATTACK
    25: 69     # DARKTEMPLARBLINKUPGRADE
}

protoss_in_progress_to_name_mapper = {
    # Buildings
    0: 'Assimilator',
    1: 'CyberneticsCore',
    2: 'DarkShrine',
    3: 'FleetBeacon',
    4: 'Forge',
    5: 'Gateway',
    6: 'Nexus',
    7: 'PhotonCannon',
    8: 'Pylon',
    9: 'RoboticsBay',
    10: 'RoboticsFacility',
    11: 'ShieldBattery',
    12: 'Stargate',
    13: 'TemplarArchive',
    14: 'TwilightCouncil',
    15: 'WarpGate',

    # Units
    16: 'Probe',
    17: 'Zealot',
    18: 'Sentry',
    19: 'Adept',
    20: 'Stalker',
    21: 'HighTemplar',
    22: 'DarkTemplar',
    23: 'Archon',
    24: 'Colossus',
    25: 'Disruptor',
    26: 'Observer',
    27: 'Immortal',
    28: 'WarpPrism',
    29: 'Phoenix',
    30: 'Oracle',
    31: 'VoidRay',
    32: 'Tempest',
    33: 'Carrier',
    34: 'Interceptor',
    35: 'Mothership',
    36: 'MothershipCore',

    # Abilities
    37: 'AdeptPhaseShift',
    38: 'ForceField',
    39: 'ObserverSurveillanceMode',
    40: 'DisruptorPhased',
    41: 'WarpPrismPhasing',
    42: 'PylonOvercharged',
    43: 'StasisTrap',

    # Upgrades
    44: 'CARRIERLAUNCHSPEEDUPGRADE',
    45: 'PROTOSSGROUNDWEAPONSLEVEL1',
    46: 'PROTOSSGROUNDWEAPONSLEVEL2',
    47: 'PROTOSSGROUNDWEAPONSLEVEL3',
    48: 'PROTOSSGROUNDARMORSLEVEL1',
    49: 'PROTOSSGROUNDARMORSLEVEL2',
    50: 'PROTOSSGROUNDARMORSLEVEL3',
    51: 'PROTOSSSHIELDSLEVEL1',
    52: 'PROTOSSSHIELDSLEVEL2',
    53: 'PROTOSSSHIELDSLEVEL3',
    54: 'OBSERVERGRAVITICBOOSTER',
    55: 'GRAVITICDRIVE',
    56: 'EXTENDEDTHERMALLANCE',
    57: 'PSISTORMTECH',
    58: 'PROTOSSAIRWEAPONSLEVEL1',
    59: 'PROTOSSAIRWEAPONSLEVEL2',
    60: 'PROTOSSAIRWEAPONSLEVEL3',
    61: 'PROTOSSAIRARMORSLEVEL1',
    62: 'PROTOSSAIRARMORSLEVEL2',
    63: 'PROTOSSAIRARMORSLEVEL3',
    64: 'WARPGATERESEARCH',
    65: 'CHARGE',
    66: 'BLINKTECH',
    67: 'PHOENIXRANGEUPGRADE',
    68: 'ADEPTPIERCINGATTACK',
    69: 'DARKTEMPLARBLINKUPGRADE'
}

# Mapping of ability_ids to the buildings/units/upgrades they will turn into. 
protoss_in_progress_ability_to_unit_mapper = {
    # Build
    882: protoss_in_progress_unit_mapper.get(61),    # BUILD_ASSIMILATOR
    894: protoss_in_progress_unit_mapper.get(72),    # BUILD_CYBERNETICSCORE
    891: protoss_in_progress_unit_mapper.get(69),    # BUILD_DARKSHRINE
    885: protoss_in_progress_unit_mapper.get(64),    # BUILD_FLEETBEACON
    884: protoss_in_progress_unit_mapper.get(63),    # BUILD_FORGE
    883: protoss_in_progress_unit_mapper.get(62),    # BUILD_GATEWAY
    1042: protoss_in_progress_unit_mapper.get(85),   # BUILD_INTERCEPTORS
    880: protoss_in_progress_unit_mapper.get(59),    # BUILD_NEXUS
    887: protoss_in_progress_unit_mapper.get(66),    # BUILD_PHOTONCANNON
    881: protoss_in_progress_unit_mapper.get(60),    # BUILD_PYLON
    892: protoss_in_progress_unit_mapper.get(70),   # BUILD_ROBOTICSBAY
    893: protoss_in_progress_unit_mapper.get(71),   # BUILD_ROBOTICSFACILITY
    895: protoss_in_progress_unit_mapper.get(1910),   # BUILD_SHIELDBATTERY
    889: protoss_in_progress_unit_mapper.get(67),   # BUILD_STARGATE
    890: protoss_in_progress_unit_mapper.get(68),   # BUILD_TEMPLARARCHIVE
    886: protoss_in_progress_unit_mapper.get(65),   # BUILD_TWILIGHTCOUNCIL

    # Morph
    1766: protoss_in_progress_unit_mapper.get(141),  # MORPH_ARCHON
    1520: protoss_in_progress_unit_mapper.get(62),  # MORPH_GATEWAY
    1847: protoss_in_progress_unit_mapper.get(10),  # MORPH_MOTHERSHIP
    1518: protoss_in_progress_unit_mapper.get(133),  # MORPH_WARPGATE

    # Research
    1594: protoss_in_progress_upgrade_mapper.get(130),  # RESEARCH_ADEPTRESONATINGGLAIVES
    1593: protoss_in_progress_upgrade_mapper.get(87),  # RESEARCH_BLINK
    1592: protoss_in_progress_upgrade_mapper.get(86),  # RESEARCH_CHARGE
    1097: protoss_in_progress_upgrade_mapper.get(50),  # RESEARCH_EXTENDEDTHERMALLANCE
    1093: protoss_in_progress_upgrade_mapper.get(48),  # RESEARCH_GRAVITICBOOSTER
    1094: protoss_in_progress_upgrade_mapper.get(49),  # RESEARCH_GRAVITICDRIVE
    44: protoss_in_progress_upgrade_mapper.get(1),    # RESEARCH_INTERCEPTORGRAVITONCATAPULT
    46: protoss_in_progress_upgrade_mapper.get(99),    # RESEARCH_PHOENIXANIONPULSECRYSTALS
    1565: protoss_in_progress_upgrade_mapper.get(81),  # RESEARCH_PROTOSSAIRARMORLEVEL1
    1566: protoss_in_progress_upgrade_mapper.get(82),  # RESEARCH_PROTOSSAIRARMORLEVEL2
    1567: protoss_in_progress_upgrade_mapper.get(83),  # RESEARCH_PROTOSSAIRARMORLEVEL3
    1562: protoss_in_progress_upgrade_mapper.get(78),  # RESEARCH_PROTOSSAIRWEAPONSLEVEL1
    1563: protoss_in_progress_upgrade_mapper.get(79),  # RESEARCH_PROTOSSAIRWEAPONSLEVEL2
    1564: protoss_in_progress_upgrade_mapper.get(80),  # RESEARCH_PROTOSSAIRWEAPONSLEVEL3
    1065: protoss_in_progress_upgrade_mapper.get(42),  # RESEARCH_PROTOSSGROUNDARMORLEVEL1
    1066: protoss_in_progress_upgrade_mapper.get(43),  # RESEARCH_PROTOSSGROUNDARMORLEVEL2
    1067: protoss_in_progress_upgrade_mapper.get(44),  # RESEARCH_PROTOSSGROUNDARMORLEVEL3
    1062: protoss_in_progress_upgrade_mapper.get(39),  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1
    1063: protoss_in_progress_upgrade_mapper.get(40),  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2
    1064: protoss_in_progress_upgrade_mapper.get(41),  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3
    1068: protoss_in_progress_upgrade_mapper.get(45),  # RESEARCH_PROTOSSSHIELDSLEVEL1
    1069: protoss_in_progress_upgrade_mapper.get(46),  # RESEARCH_PROTOSSSHIELDSLEVEL2
    1070: protoss_in_progress_upgrade_mapper.get(47),  # RESEARCH_PROTOSSSHIELDSLEVEL3
    1126: protoss_in_progress_upgrade_mapper.get(52),  # RESEARCH_PSISTORM
    2720: protoss_in_progress_upgrade_mapper.get(141),  # RESEARCH_SHADOWSTRIKE
    1568: protoss_in_progress_upgrade_mapper.get(84),  # RESEARCH_WARPGATE

    # Train
    922: protoss_in_progress_unit_mapper.get(311),   # TRAIN_ADEPT
    948: protoss_in_progress_unit_mapper.get(79),   # TRAIN_CARRIER
    978: protoss_in_progress_unit_mapper.get(4),   # TRAIN_COLOSSUS
    920: protoss_in_progress_unit_mapper.get(76),   # TRAIN_DARKTEMPLAR
    994: protoss_in_progress_unit_mapper.get(694),   # TRAIN_DISRUPTOR
    919: protoss_in_progress_unit_mapper.get(75),   # TRAIN_HIGHTEMPLAR
    979: protoss_in_progress_unit_mapper.get(83),   # TRAIN_IMMORTAL
    110: protoss_in_progress_unit_mapper.get(10),   # TRAIN_MOTHERSHIP
    1853: protoss_in_progress_unit_mapper.get(488),  # TRAIN_MOTHERSHIPCORE
    977: protoss_in_progress_unit_mapper.get(82),   # TRAIN_OBSERVER
    954: protoss_in_progress_unit_mapper.get(495),   # TRAIN_ORACLE
    946: protoss_in_progress_unit_mapper.get(78),   # TRAIN_PHOENIX
    1006: protoss_in_progress_unit_mapper.get(84),  # TRAIN_PROBE
    921: protoss_in_progress_unit_mapper.get(77),   # TRAIN_SENTRY
    917: protoss_in_progress_unit_mapper.get(74),   # TRAIN_STALKER
    955: protoss_in_progress_unit_mapper.get(496),   # TRAIN_TEMPEST
    950: protoss_in_progress_unit_mapper.get(80),   # TRAIN_VOIDRAY
    976: protoss_in_progress_unit_mapper.get(81),   # TRAIN_WARPPRISM
    916: protoss_in_progress_unit_mapper.get(73),   # TRAIN_ZEALOT

    # TrainWarp
    1419: protoss_in_progress_unit_mapper.get(311),  # TRAINWARP_ADEPT
    1417: protoss_in_progress_unit_mapper.get(76),  # TRAINWARP_DARKTEMPLAR
    1416: protoss_in_progress_unit_mapper.get(75),  # TRAINWARP_HIGHTEMPLAR
    1418: protoss_in_progress_unit_mapper.get(77),  # TRAINWARP_SENTRY
    1414: protoss_in_progress_unit_mapper.get(74),  # TRAINWARP_STALKER
    1413: protoss_in_progress_unit_mapper.get(73),  # TRAINWARP_ZEALOT
}

# Mapping of macro abiliti_ids to the buildings/units/upgrades they will turn into. 
protoss_ability_to_unit_mapper = {
    # Build
    882: 0,    # BUILD_ASSIMILATOR
    894: 1,    # BUILD_CYBERNETICSCORE
    891: 2,    # BUILD_DARKSHRINE
    885: 3,    # BUILD_FLEETBEACON
    884: 4,    # BUILD_FORGE
    883: 5,    # BUILD_GATEWAY
    1042: 6,   # BUILD_INTERCEPTORS
    880: 7,    # BUILD_NEXUS
    887: 8,    # BUILD_PHOTONCANNON
    881: 9,    # BUILD_PYLON
    892: 10,   # BUILD_ROBOTICSBAY
    893: 11,   # BUILD_ROBOTICSFACILITY
    895: 12,   # BUILD_SHIELDBATTERY
    889: 13,   # BUILD_STARGATE
    890: 14,   # BUILD_TEMPLARARCHIVE
    886: 15,   # BUILD_TWILIGHTCOUNCIL

    # Morph
    1766: 16,  # MORPH_ARCHON
    1520: 5,  # MORPH_GATEWAY
    1847: 17,  # MORPH_MOTHERSHIP
    1518: 18,  # MORPH_WARPGATE

    # Research
    1594: 19,  # RESEARCH_ADEPTRESONATINGGLAIVES
    1593: 20,  # RESEARCH_BLINK
    1592: 21,  # RESEARCH_CHARGE
    1097: 22,  # RESEARCH_EXTENDEDTHERMALLANCE
    1093: 23,  # RESEARCH_GRAVITICBOOSTER
    1094: 24,  # RESEARCH_GRAVITICDRIVE
    44: 25,    # RESEARCH_INTERCEPTORGRAVITONCATAPULT
    46: 26,    # RESEARCH_PHOENIXANIONPULSECRYSTALS
    1565: 27,  # RESEARCH_PROTOSSAIRARMORLEVEL1
    1566: 27,  # RESEARCH_PROTOSSAIRARMORLEVEL2
    1567: 27,  # RESEARCH_PROTOSSAIRARMORLEVEL3
    1562: 28,  # RESEARCH_PROTOSSAIRWEAPONSLEVEL1
    1563: 28,  # RESEARCH_PROTOSSAIRWEAPONSLEVEL2
    1564: 28,  # RESEARCH_PROTOSSAIRWEAPONSLEVEL3
    1065: 29,  # RESEARCH_PROTOSSGROUNDARMORLEVEL1
    1066: 29,  # RESEARCH_PROTOSSGROUNDARMORLEVEL2
    1067: 29,  # RESEARCH_PROTOSSGROUNDARMORLEVEL3
    1062: 30,  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1
    1063: 30,  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2
    1064: 30,  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3
    1068: 31,  # RESEARCH_PROTOSSSHIELDSLEVEL1
    1069: 31,  # RESEARCH_PROTOSSSHIELDSLEVEL2
    1070: 31,  # RESEARCH_PROTOSSSHIELDSLEVEL3
    1126: 32,  # RESEARCH_PSISTORM
    2720: 33,  # RESEARCH_SHADOWSTRIKE
    1568: 34,  # RESEARCH_WARPGATE

    # Train
    922: 35,   # TRAIN_ADEPT
    948: 36,   # TRAIN_CARRIER
    978: 37,   # TRAIN_COLOSSUS
    920: 38,   # TRAIN_DARKTEMPLAR
    994: 39,   # TRAIN_DISRUPTOR
    919: 40,   # TRAIN_HIGHTEMPLAR
    979: 41,   # TRAIN_IMMORTAL
    110: 42,   # TRAIN_MOTHERSHIP
    1853: 43,  # TRAIN_MOTHERSHIPCORE
    977: 44,   # TRAIN_OBSERVER
    954: 45,   # TRAIN_ORACLE
    946: 46,   # TRAIN_PHOENIX
    1006: 47,  # TRAIN_PROBE
    921: 48,   # TRAIN_SENTRY
    917: 49,   # TRAIN_STALKER
    955: 50,   # TRAIN_TEMPEST
    950: 51,   # TRAIN_VOIDRAY
    976: 52,   # TRAIN_WARPPRISM
    916: 53,   # TRAIN_ZEALOT

    # TrainWarp
    1419: 35,  # TRAINWARP_ADEPT
    1417: 38,  # TRAINWARP_DARKTEMPLAR
    1416: 40,  # TRAINWARP_HIGHTEMPLAR
    1418: 48,  # TRAINWARP_SENTRY
    1414: 49,  # TRAINWARP_STALKER
    1413: 53,  # TRAINWARP_ZEALOT
}

# The names of the different macro actions a player can take. 
protoss_macro_actions = [
    # Build
    'ASSIMILATOR',
    'CYBERNETICSCORE',
    'DARKSHRINE',
    'FLEETBEACON',
    'FORGE',
    'GATEWAY',
    'INTERCEPTORS',
    'NEXUS',
    'PHOTONCANNON',
    'PYLON',
    'ROBOTICSBAY',
    'ROBOTICSFACILITY',
    'SHIELDBATTERY',
    'STARGATE',
    'TEMPLARARCHIVE',
    'TWILIGHTCOUNCIL',

    # Morph
    'ARCHON',
    'MOTHERSHIP',
    'WARPGATE',

    # Research
    'ADEPTRESONATINGGLAIVES',
    'BLINK',
    'CHARGE',
    'EXTENDEDTHERMALLANCE',
    'GRAVITICBOOSTER',
    'GRAVITICDRIVE',
    'INTERCEPTORGRAVITONCATAPULT',
    'PHOENIXANIONPULSECRYSTALS',
    'PROTOSSAIRARMOR',
    'PROTOSSAIRWEAPONS',
    'PROTOSSGROUNDARMOR',
    'PROTOSSGROUNDWEAPONS',
    'PROTOSSSHIELDS',
    'PSISTORM',
    'SHADOWSTRIKE',
    'RESEARCHWARPGATE',

    # Train
    'ADEPT',
    'CARRIER',
    'COLOSSUS',
    'DARKTEMPLAR',
    'DISRUPTOR',
    'HIGHTEMPLAR',
    'IMMORTAL',
    'MOTHERSHIP',
    'MOTHERSHIPCORE',
    'OBSERVER',
    'ORACLE',
    'PHOENIX',
    'PROBE',
    'SENTRY',
    'STALKER',
    'TEMPEST',
    'VOIDRAY',
    'WARPPRISM',
    'ZEALOT'
]

# Mapping of unit_id to index in list.
protoss_unit_to_name_mapper = {
    # Buildings
    0: 'Assimilator',
    1: 'CyberneticsCore',
    2: 'DarkShrine',
    3: 'FleetBeacon',
    4: 'Forge',
    5: 'Gateway',
    6: 'Nexus',
    7: 'PhotonCannon',
    8: 'Pylon',
    9: 'RoboticsBay',
    10: 'RoboticsFacility',
    11: 'ShieldBattery',
    12: 'Stargate',
    13: 'TemplarArchive',
    14: 'TwilightCouncil',
    15: 'WarpGate',

    # Units
    16: 'Probe',
    17: 'Zealot',
    18: 'Sentry',
    19: 'Adept',
    20: 'Stalker',
    21: 'HighTemplar',
    22: 'DarkTemplar',
    23: 'Archon',
    24: 'Colossus',
    25: 'Disruptor',
    26: 'Observer',
    27: 'Immortal',
    28: 'WarpPrism',
    29: 'Phoenix',
    30: 'Oracle',
    31: 'VoidRay',
    32: 'Tempest',
    33: 'Carrier',
    34: 'Interceptor',
    35: 'Mothership',
    36: 'MothershipCore',

    # Abilities
    37: 'AdeptPhaseShift',
    38: 'ForceField',
    39: 'ObserverSurveillanceMode',
    40: 'DisruptorPhased',
    41: 'WarpPrismPhasing',
    42: 'PylonOvercharged',
    43: 'StasisTrap'
}

# Mapping of upgrades (ability_ids) to indexes in list
protoss_upgrade_to_name_mapper = {
    0: 'CARRIERLAUNCHSPEEDUPGRADE',
    1: 'PROTOSSGROUNDWEAPONSLEVEL1',
    2: 'PROTOSSGROUNDWEAPONSLEVEL2',
    3: 'PROTOSSGROUNDWEAPONSLEVEL3',
    4: 'PROTOSSGROUNDARMORSLEVEL1',
    5: 'PROTOSSGROUNDARMORSLEVEL2',
    6: 'PROTOSSGROUNDARMORSLEVEL3',
    7: 'PROTOSSSHIELDSLEVEL1',
    8: 'PROTOSSSHIELDSLEVEL2',
    9: 'PROTOSSSHIELDSLEVEL3',
    10: 'OBSERVERGRAVITICBOOSTER',
    11: 'GRAVITICDRIVE',
    12: 'EXTENDEDTHERMALLANCE',
    13: 'PSISTORMTECH',
    14: 'PROTOSSAIRWEAPONSLEVEL1',
    15: 'PROTOSSAIRWEAPONSLEVEL2',
    16: 'PROTOSSAIRWEAPONSLEVEL3',
    17: 'PROTOSSAIRARMORSLEVEL1',
    18: 'PROTOSSAIRARMORSLEVEL2',
    19: 'PROTOSSAIRARMORSLEVEL3',
    20: 'WARPGATERESEARCH',
    21: 'CHARGE',
    22: 'BLINKTECH',
    23: 'PHOENIXRANGEUPGRADE',
    24: 'ADEPTPIERCINGATTACK',
    25: 'DARKTEMPLARBLINKUPGRADE'
}

# Maps to output action
protoss_output_to_action_mapper = {
    # Build
    0: UnitTypeId.ASSIMILATOR,    # BUILD_ASSIMILATOR
    1: UnitTypeId.CYBERNETICSCORE,    # BUILD_CYBERNETICSCORE
    2: UnitTypeId.DARKSHRINE,    # BUILD_DARKSHRINE
    3: UnitTypeId.FLEETBEACON,    # BUILD_FLEETBEACON
    4: UnitTypeId.FORGE,    # BUILD_FORGE
    5: UnitTypeId.GATEWAY,    # BUILD_GATEWAY
    6: UnitTypeId.INTERCEPTOR,   # BUILD_INTERCEPTORS
    7: UnitTypeId.NEXUS,    # BUILD_NEXUS
    8: UnitTypeId.PHOTONCANNON,    # BUILD_PHOTONCANNON
    9: UnitTypeId.PYLON,    # BUILD_PYLON
    10: UnitTypeId.ROBOTICSBAY,   # BUILD_ROBOTICSBAY
    11: UnitTypeId.ROBOTICSFACILITY,   # BUILD_ROBOTICSFACILITY
    12: UnitTypeId.SHIELDBATTERY,   # BUILD_SHIELDBATTERY
    13: UnitTypeId.STARGATE,   # BUILD_STARGATE
    14: UnitTypeId.TEMPLARARCHIVE,   # BUILD_TEMPLARARCHIVE
    15: UnitTypeId.TWILIGHTCOUNCIL,   # BUILD_TWILIGHTCOUNCIL

    # Morph
    16: UnitTypeId.ARCHON,  # MORPH_ARCHON
    5: UnitTypeId.GATEWAY,  # MORPH_GATEWAY
    17: UnitTypeId.MOTHERSHIP,  # MORPH_MOTHERSHIP
    18: UnitTypeId.WARPGATE,  # MORPH_WARPGATE

    # Research
    19: UpgradeId.ADEPTPIERCINGATTACK,  # RESEARCH_ADEPTRESONATINGGLAIVES
    20: UpgradeId.BLINKTECH,  # RESEARCH_BLINK
    21: UpgradeId.CHARGE,  # RESEARCH_CHARGE
    22: UpgradeId.EXTENDEDTHERMALLANCE,  # RESEARCH_EXTENDEDTHERMALLANCE
    23: UpgradeId.GRAVITICTHRUSTERS,  # RESEARCH_GRAVITICBOOSTER
    24: UpgradeId.GRAVITICDRIVE,  # RESEARCH_GRAVITICDRIVE
    25: UpgradeId.CARRIERLAUNCHSPEEDUPGRADE,    # RESEARCH_INTERCEPTORGRAVITONCATAPULT
    26: UpgradeId.PHOENIXRANGEUPGRADE,    # RESEARCH_PHOENIXANIONPULSECRYSTALS
    27: UpgradeId.PROTOSSAIRARMORSLEVEL1,  # RESEARCH_PROTOSSAIRARMORLEVEL1
    27: UpgradeId.PROTOSSAIRARMORSLEVEL2,  # RESEARCH_PROTOSSAIRARMORLEVEL2
    27: UpgradeId.PROTOSSAIRARMORSLEVEL3,  # RESEARCH_PROTOSSAIRARMORLEVEL3
    28: UpgradeId.PROTOSSAIRWEAPONSLEVEL1,  # RESEARCH_PROTOSSAIRWEAPONSLEVEL1
    28: UpgradeId.PROTOSSAIRWEAPONSLEVEL2,  # RESEARCH_PROTOSSAIRWEAPONSLEVEL2
    28: UpgradeId.PROTOSSAIRWEAPONSLEVEL3,  # RESEARCH_PROTOSSAIRWEAPONSLEVEL3
    29: UpgradeId.PROTOSSGROUNDARMORSLEVEL1,  # RESEARCH_PROTOSSGROUNDARMORLEVEL1
    29: UpgradeId.PROTOSSGROUNDARMORSLEVEL2,  # RESEARCH_PROTOSSGROUNDARMORLEVEL2
    29: UpgradeId.PROTOSSGROUNDARMORSLEVEL3,  # RESEARCH_PROTOSSGROUNDARMORLEVEL3
    30: UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1,  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1
    30: UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2,  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2
    30: UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3,  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3
    31: UpgradeId.PROTOSSSHIELDSLEVEL1,  # RESEARCH_PROTOSSSHIELDSLEVEL1
    31: UpgradeId.PROTOSSSHIELDSLEVEL2,  # RESEARCH_PROTOSSSHIELDSLEVEL2
    31: UpgradeId.PROTOSSSHIELDSLEVEL3,  # RESEARCH_PROTOSSSHIELDSLEVEL3
    32: UpgradeId.PSISTORMTECH,  # RESEARCH_PSISTORM
    33: UpgradeId.DARKTEMPLARBLINKUPGRADE,  # RESEARCH_SHADOWSTRIKE
    34: UpgradeId.WARPGATERESEARCH,  # RESEARCH_WARPGATE

    # Train
    35: UnitTypeId.ADEPT,   # TRAIN_ADEPT
    36: UnitTypeId.CARRIER,   # TRAIN_CARRIER
    37: UnitTypeId.COLOSSUS,   # TRAIN_COLOSSUS
    38: UnitTypeId.DARKTEMPLAR,   # TRAIN_DARKTEMPLAR
    39: UnitTypeId.DISRUPTOR,   # TRAIN_DISRUPTOR
    40: UnitTypeId.HIGHTEMPLAR,   # TRAIN_HIGHTEMPLAR
    41: UnitTypeId.IMMORTAL,   # TRAIN_IMMORTAL
    42: UnitTypeId.MOTHERSHIP,   # TRAIN_MOTHERSHIP
    43: UnitTypeId.MOTHERSHIPCORE,  # TRAIN_MOTHERSHIPCORE
    44: UnitTypeId.OBSERVER,   # TRAIN_OBSERVER
    45: UnitTypeId.ORACLE,   # TRAIN_ORACLE
    46: UnitTypeId.PHOENIX,   # TRAIN_PHOENIX
    47: UnitTypeId.PROBE,  # TRAIN_PROBE
    48: UnitTypeId.SENTRY,   # TRAIN_SENTRY
    49: UnitTypeId.STALKER,   # TRAIN_STALKER
    50: UnitTypeId.TEMPEST,   # TRAIN_TEMPEST
    51: UnitTypeId.VOIDRAY,   # TRAIN_VOIDRAY
    52: UnitTypeId.WARPPRISM,   # TRAIN_WARPPRISM
    53: UnitTypeId.ZEALOT,   # TRAIN_ZEALOT

    # TrainWarp
    35: UnitTypeId.ADEPT,  # TRAINWARP_ADEPT
    38: UnitTypeId.DARKTEMPLAR,  # TRAINWARP_DARKTEMPLAR
    40: UnitTypeId.HIGHTEMPLAR,  # TRAINWARP_HIGHTEMPLAR
    48: UnitTypeId.SENTRY,  # TRAINWARP_SENTRY
    49: UnitTypeId.STALKER,  # TRAINWARP_STALKER
    53: UnitTypeId.ZEALOT,  # TRAINWARP_ZEALOT
}


action_to_type_mapper = {
        # Build
    UnitTypeId.ASSIMILATOR: 'build',    # BUILD_ASSIMILATOR
    UnitTypeId.CYBERNETICSCORE: 'build',    # BUILD_CYBERNETICSCORE
    UnitTypeId.DARKSHRINE: 'build',    # BUILD_DARKSHRINE
    UnitTypeId.FLEETBEACON: 'build',    # BUILD_FLEETBEACON
    UnitTypeId.FORGE: 'build',    # BUILD_FORGE
    UnitTypeId.GATEWAY: 'build',    # BUILD_GATEWAY
    UnitTypeId.INTERCEPTOR: 'build',   # BUILD_INTERCEPTORS
    UnitTypeId.NEXUS: 'build',    # BUILD_NEXUS
    UnitTypeId.PHOTONCANNON: 'build',    # BUILD_PHOTONCANNON
    UnitTypeId.PYLON: 'build',    # BUILD_PYLON
    UnitTypeId.ROBOTICSBAY: 'build',   # BUILD_ROBOTICSBAY
    UnitTypeId.ROBOTICSFACILITY: 'build',   # BUILD_ROBOTICSFACILITY
    UnitTypeId.SHIELDBATTERY: 'build',   # BUILD_SHIELDBATTERY
    UnitTypeId.STARGATE: 'build',   # BUILD_STARGATE
    UnitTypeId.TEMPLARARCHIVE: 'build',   # BUILD_TEMPLARARCHIVE
    UnitTypeId.TWILIGHTCOUNCIL: 'build',   # BUILD_TWILIGHTCOUNCIL

    # Morph
    UnitTypeId.ARCHON: 'ability',  # MORPH_ARCHON
    UnitTypeId.GATEWAY: 'ability',  # MORPH_GATEWAY
    UnitTypeId.WARPGATE: 'ability',  # MORPH_WARPGATE

    # Research
    UpgradeId.ADEPTPIERCINGATTACK: 'upgrade',  # RESEARCH_ADEPTRESONATINGGLAIVES
    UpgradeId.BLINKTECH: 'upgrade',  # RESEARCH_BLINK
    UpgradeId.CHARGE: 'upgrade',  # RESEARCH_CHARGE
    UpgradeId.EXTENDEDTHERMALLANCE: 'upgrade',  # RESEARCH_EXTENDEDTHERMALLANCE
    UpgradeId.GRAVITICTHRUSTERS: 'upgrade',  # RESEARCH_GRAVITICBOOSTER
    UpgradeId.GRAVITICDRIVE: 'upgrade',  # RESEARCH_GRAVITICDRIVE
    UpgradeId.CARRIERLAUNCHSPEEDUPGRADE: 'upgrade',    # RESEARCH_INTERCEPTORGRAVITONCATAPULT
    UpgradeId.PHOENIXRANGEUPGRADE: 'upgrade',    # RESEARCH_PHOENIXANIONPULSECRYSTALS
    UpgradeId.PROTOSSAIRARMORSLEVEL1: 'upgrade',  # RESEARCH_PROTOSSAIRARMORLEVEL1
    UpgradeId.PROTOSSAIRARMORSLEVEL2: 'upgrade',  # RESEARCH_PROTOSSAIRARMORLEVEL2
    UpgradeId.PROTOSSAIRARMORSLEVEL3: 'upgrade',  # RESEARCH_PROTOSSAIRARMORLEVEL3
    UpgradeId.PROTOSSAIRWEAPONSLEVEL1: 'upgrade',  # RESEARCH_PROTOSSAIRWEAPONSLEVEL1
    UpgradeId.PROTOSSAIRWEAPONSLEVEL2: 'upgrade',  # RESEARCH_PROTOSSAIRWEAPONSLEVEL2
    UpgradeId.PROTOSSAIRWEAPONSLEVEL3: 'upgrade',  # RESEARCH_PROTOSSAIRWEAPONSLEVEL3
    UpgradeId.PROTOSSGROUNDARMORSLEVEL1: 'upgrade',  # RESEARCH_PROTOSSGROUNDARMORLEVEL1
    UpgradeId.PROTOSSGROUNDARMORSLEVEL2: 'upgrade',  # RESEARCH_PROTOSSGROUNDARMORLEVEL2
    UpgradeId.PROTOSSGROUNDARMORSLEVEL3: 'upgrade',  # RESEARCH_PROTOSSGROUNDARMORLEVEL3
    UpgradeId.PROTOSSGROUNDWEAPONSLEVEL1: 'upgrade',  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1
    UpgradeId.PROTOSSGROUNDWEAPONSLEVEL2: 'upgrade',  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2
    UpgradeId.PROTOSSGROUNDWEAPONSLEVEL3: 'upgrade',  # RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3
    UpgradeId.PROTOSSSHIELDSLEVEL1: 'upgrade',  # RESEARCH_PROTOSSSHIELDSLEVEL1
    UpgradeId.PROTOSSSHIELDSLEVEL2: 'upgrade',  # RESEARCH_PROTOSSSHIELDSLEVEL2
    UpgradeId.PROTOSSSHIELDSLEVEL3: 'upgrade',  # RESEARCH_PROTOSSSHIELDSLEVEL3
    UpgradeId.PSISTORMTECH: 'upgrade',  # RESEARCH_PSISTORM
    UpgradeId.DARKTEMPLARBLINKUPGRADE: 'upgrade',  # RESEARCH_SHADOWSTRIKE
    UpgradeId.WARPGATERESEARCH: 'upgrade',  # RESEARCH_WARPGATE

    # Train
    UnitTypeId.ADEPT: 'train',   # TRAIN_ADEPT
    UnitTypeId.CARRIER: 'train',   # TRAIN_CARRIER
    UnitTypeId.COLOSSUS: 'train',   # TRAIN_COLOSSUS
    UnitTypeId.DARKTEMPLAR: 'train',   # TRAIN_DARKTEMPLAR
    UnitTypeId.DISRUPTOR: 'train',   # TRAIN_DISRUPTOR
    UnitTypeId.HIGHTEMPLAR: 'train',   # TRAIN_HIGHTEMPLAR
    UnitTypeId.IMMORTAL: 'train',   # TRAIN_IMMORTAL
    UnitTypeId.MOTHERSHIP: 'train',   # TRAIN_MOTHERSHIP
    UnitTypeId.MOTHERSHIPCORE: 'train',  # TRAIN_MOTHERSHIPCORE
    UnitTypeId.OBSERVER: 'train',   # TRAIN_OBSERVER
    UnitTypeId.ORACLE: 'train',   # TRAIN_ORACLE
    UnitTypeId.PHOENIX: 'train',   # TRAIN_PHOENIX
    UnitTypeId.PROBE: 'train',  # TRAIN_PROBE
    UnitTypeId.SENTRY: 'train',   # TRAIN_SENTRY
    UnitTypeId.STALKER: 'train',   # TRAIN_STALKER
    UnitTypeId.TEMPEST: 'train',   # TRAIN_TEMPEST
    UnitTypeId.VOIDRAY: 'train',   # TRAIN_VOIDRAY
    UnitTypeId.WARPPRISM: 'train',   # TRAIN_WARPPRISM
    UnitTypeId.ZEALOT: 'train',   # TRAIN_ZEALOT
    UnitTypeId.MOTHERSHIP: 'train',  # MORPH_MOTHERSHIP

    # TrainWarp
    UnitTypeId.ADEPT: 'train',  # TRAINWARP_ADEPT
    UnitTypeId.DARKTEMPLAR: 'train',  # TRAINWARP_DARKTEMPLAR
    UnitTypeId.HIGHTEMPLAR: 'train',  # TRAINWARP_HIGHTEMPLAR
    UnitTypeId.SENTRY: 'train',  # TRAINWARP_SENTRY
    UnitTypeId.STALKER: 'train',  # TRAINWARP_STALKER
    UnitTypeId.ZEALOT: 'train',  # TRAINWARP_ZEALOT
}
