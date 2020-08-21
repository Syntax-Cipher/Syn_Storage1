class Fighters:

    def __init__(self, name, stam, agi, defence, max_hp):
        self.name = name
        self.stam = stam
        self.agi = agi
        self.defence = defence
        self.max_hp = max_hp
        return None

    def __repr__(self):
        return "\n~ Name: {}, Stamina: {}, Agility: {}, Defence: {}, Max_hp: {} ~\n".format(self.name, self.stam, self.agi, self.defence, self.max_hp)

    def stats_matrix(self):
        stat_mat = []
        stat_mat = [self.name, self.stam, self.agi, self.defence, self.max_hp]
        return stat_mat

    def fighter_one_mods(self, other):
        stam_mod = 1.0
        agi_mod = 1.0
        defence_mod = 1.0
        if (samurai and shinobi) or (samurai and archer) or (shinobi and samurai) or (shinobi and archer) or (archer and samurai) or (archer and shinobi):
            if self.stam > other.stam:
                stam_mod = 1.2
            elif self.stam < other.stam:
                stam_mod = 0.8
            else:
                stam_mod = 1.0
            if self.agi > other.agi:
                agi_mod = 1.2
            elif self.agi < other.agi:
                agi_mod = 0.8
            else:
                agi_mod = 1.0
            if self.defence > other.defence:
                defence_mod = 1.2
            elif self.defence < other.defence:
                defence_mod = 0.8
            else:
                defence_mod = 1.0
            return "\n stamina mod of first fighter is {}, agility mod of first fighter is {}, defence mod of first fighter is {}".format(stam_mod,agi_mod,defence_mod)

    def fighter_two_mods(other, self):
        stam_mod = 1.0
        agi_mod = 1.0
        defence_mod = 1.0
        if (samurai and shinobi) or (samurai and archer) or (shinobi and samurai) or (shinobi and archer) or (archer and samurai) or (archer and shinobi):
            if self.stam > other.stam:
                stam_mod = 1.2
            elif self.stam < other.stam:
                stam_mod = 0.8
            else:
                stam_mod = 1.0
            if self.agi > other.agi:
                agi_mod = 1.2
            elif self.agi < other.agi:
                agi_mod = 0.8
            else:
                agi_mod = 1.0
            if self.defence > other.defence:
                defence_mod = 1.2
            elif self.defence < other.defence:
                defence_mod = 0.8
            else:
                defence_mod = 1.0
            return "\n stamina mod of second fighter is {}, agility mod of second fighter is {}, defence mod of second fighter is {}".format(
                stam_mod, agi_mod, defence_mod)



samurai = Fighters("Sakai The Samurai", 90, 80, 90, 100)
print(samurai)
print(samurai.stats_matrix())

shinobi = Fighters("Ryozu The Shinobi", 80, 80, 70, 100)
print(shinobi)
print(shinobi.stats_matrix())

archer = Fighters("Istewa The Archer", 70, 70, 70, 100)
print(archer)
print(archer.stats_matrix())

mods_one = Fighters.fighter_one_mods(shinobi, samurai)
print(mods_one)

mods_two = Fighters.fighter_two_mods(shinobi, samurai)
print(mods_two)

win_value1 = winner(0.8, 1.0, 0.8)
print(win_value1)
win_value2 = winner(1.2, 1.0, 1.2)
print(win_value2)

#multiply each individual's stat in stat matrix by multiplier modification AKA stam mod, defence mod etc. Then, add total stat numbers up and compare with other fighter to determine winner