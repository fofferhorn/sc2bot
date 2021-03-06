class Manager:

    def __init__(self, bot):
        self.bot = bot
        self.actions = []
        self.locked = False

    async def execute(self):
        if not self.locked:
            self.locked = True
            if len(self.actions) > 0:
                actions = [action for action in self.actions]
                self.actions = []
                await self.bot.do_actions(actions)
            else:
                await self.run()
            self.locked = False

    async def run(self):
        """ Override this in your manager class. """
        pass

    async def on_unit_destroyed(self, unit_tag):
        """ Override this in your manager class. """
        pass

    async def on_unit_created(self, unit):
        """ Override this in your manager class. """
        pass

    async def on_building_construction_started(self, unit):
        """ Override this in your manager class. """
        pass

    async def on_building_construction_complete(self, unit):
        """ Override this in your manager class. """
        pass


class ProductionManager(Manager):

    def __init__(self, bot, worker_manager, building_manager):
        super().__init__(bot)
        self.worker_manager = worker_manager
        self.building_manager = building_manager

    async def run(self):
        raise NotImplementedError("Must be overridden by subclass")


class ScoutingManager(Manager):

    def __init__(self, bot, worker_manager, building_manager):
        super().__init__(bot)
        self.worker_manager = worker_manager
        self.building_manager = building_manager

    async def run(self):
        raise NotImplementedError("Must be overridden by subclass")


class AssaultManager(Manager):

    def __init__(self, bot, army_manager, worker_manager):
        super().__init__(bot)
        self.army_manager = army_manager
        self.worker_manager = worker_manager

    async def run(self):
        raise NotImplementedError("Must be overridden by subclass")


class WorkerManager(Manager):

    def __init__(self, bot):
        super().__init__(bot)

    async def run(self):
        raise NotImplementedError("Must be overridden by subclass")

    async def distribute(self):
        raise NotImplementedError("Must be overridden by subclass")

    async def build(self, building, location=None):
        raise NotImplementedError("Must be overridden by subclass")

    async def scout(self, location):
        raise NotImplementedError("Must be overridden by subclass")

    async def rush(self, location):
        raise NotImplementedError("Must be overridden by subclass")

    async def defend(self, location):
        raise NotImplementedError("Must be overridden by subclass")

    def is_building(self, building_type):
        raise NotImplementedError("Must be overridden by subclass")

    def has_unstarted_plan(self):
        raise NotImplementedError("Must be overridden by subclass")


class BuildingManager(Manager):

    def __init__(self, bot, worker_manager):
        super().__init__(bot)
        self.worker_manager = worker_manager

    async def run(self):
        raise NotImplementedError("Must be overridden by subclass")

    async def train(self, unit):
        raise NotImplementedError("Must be overridden by subclass")

    async def add_on(self, add_on):
        raise NotImplementedError("Must be overridden by subclass")

    async def research(self, upgrade):
        raise NotImplementedError("Must be overridden by subclass")

    async def upgrade(self, upgrade):
        raise NotImplementedError("Must be overridden by subclass")

    async def calldown_mule(self):
        raise NotImplementedError("Must be overridden by subclass")

    async def scan(self, location):
        raise NotImplementedError("Must be overridden by subclass")

    async def can_train(self, unit_type):
        raise NotImplementedError("Must be overridden by subclass")

    def can_upgrade(self, upgrade_type):
        raise NotImplementedError("Must be overridden by subclass")

    def can_add_on(self, add_on):
        raise NotImplementedError("Must be overridden by subclass")

    def is_legal_training_action(self, unit_type):
        raise NotImplementedError("Must be overridden by subclass")

    def is_legal_upgrade_action(self, upgrade_type):
        raise NotImplementedError("Must be overridden by subclass")

    def is_legal_build_action(self, build_type):
        raise NotImplementedError("Must be overridden by subclass")


class ArmyManager(Manager):

    def __init__(self, bot):
        super().__init__(bot)

    async def run(self):
        raise NotImplementedError("Must be overridden by subclass")

    async def attack(self, location, unit_types=None):
        raise NotImplementedError("Must be overridden by subclass")

    async def defend(self, location, unit_types=None):
        raise NotImplementedError("Must be overridden by subclass")
