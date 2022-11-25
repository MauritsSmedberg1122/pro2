class Hero:
    def init(self, name, secret_identity, weakness, catch_phrase, exposed, rivals) -> None:
        self.name = name
        self.secret_identity = secret_identity
        self.weakness = weakness
        self.catch_phrase = catch_phrase
        self.exposed = exposed
        self.rivals = rivals

    def say_catch_phrase(self):
        return self.catch_phrase

    def expose(self):
        self.expose == True

    def get_identity(self):
        return self.secret_identity

class Villan:
    def init(self, name, secret_identity: str, hideout: str, secret_plan: str, henchman: list, nemesis: Hero) -> None:
        self.name = name
        self.secret_identity = secret_identity
        self.hideout = hideout
        self.secret_plan = secret_plan
        self.henchman = henchman
        self.nemesis = nemesis

    def get_identity(self):
        return self.secret_identity

    def reveal_plan(self):
        return self.secret_plan

    def recruit_new_hench(self, newhench):
        self.henchman == newhench

class Henchman(Villan):
    def init(self, name, secret_identity: str, hideout: str, secret_plan: str, henchman: list, nemesis: Hero, sallary, role) -> None:
        super().init(name, secret_identity, hideout, secret_plan, henchman, nemesis)
        self.name = name
        self.works_for = Villan
        self.sallary = sallary
        self.role = role