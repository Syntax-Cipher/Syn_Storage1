class Fighters:

    def __init__(self, name, stam, agi, defence, stam_mod, agi_mod, defence_mod):
        self.name = name
        self.stam = stam
        self.agi = agi
        self.defence = defence
        self.stam_mod = stam_mod
        self.agi_mod = agi_mod
        self.defence_mod = defence_mod


    def __repr__(self):
        return "\n~ Name: {}, Stamina: {}, Agility: {}, Defence: {}, Stamina Mod: {}, Agility Mod: {}, Defence Mod: {} ~\n".format(self.name, self.stam, self.agi, self.defence, self.stam_mod, self.agi_mod, self.defence_mod)

    def stats_matrix(self):
        stat_mat = []
        stat_mat = [self.name, self.stam, self.agi, self.defence, self.stam_mod, self.agi_mod, self.defence_mod]
        return stat_mat

    def fighter_one_mods(self, other):
        mod_matrix = []
        if (samurai and shinobi) or (samurai and archer) or (shinobi and samurai) or (shinobi and archer) or (archer and samurai) or (archer and shinobi):
            if self.stam > other.stam:
                stam_mod = 1.2
                mod_matrix.append(stam_mod)
            elif self.stam < other.stam:
                stam_mod = 0.8
                mod_matrix.append(stam_mod)
            else:
                stam_mod = 1.0
                mod_matrix.append(stam_mod)
            if self.agi > other.agi:
                agi_mod = 1.2
                mod_matrix.append(agi_mod)
            elif self.agi < other.agi:
                agi_mod = 0.8
                mod_matrix.append(agi_mod)
            else:
                agi_mod = 1.0
                mod_matrix.append(agi_mod)
            if self.defence > other.defence:
                defence_mod = 1.2
                mod_matrix.append(defence_mod)
            elif self.defence < other.defence:
                defence_mod = 0.8
                mod_matrix.append(defence_mod)
            else:
                defence_mod = 1.0
                mod_matrix.append(defence_mod)

            return mod_matrix

    def fighter_two_mods(other, self):
        stam_mod = 1.0
        agi_mod = 1.0
        defence_mod = 1.0
        mod_matrix = []
        if (samurai and shinobi) or (samurai and archer) or (shinobi and samurai) or (shinobi and archer) or (archer and samurai) or (archer and shinobi):
            if self.stam > other.stam:
                stam_mod = 1.2
                mod_matrix.append(stam_mod)
            elif self.stam < other.stam:
                stam_mod = 0.8
                mod_matrix.append(stam_mod)
            else:
                stam_mod = 1.0
                mod_matrix.append(stam_mod)
            if self.agi > other.agi:
                agi_mod = 1.2
                mod_matrix.append(agi_mod)
            elif self.agi < other.agi:
                agi_mod = 0.8
                mod_matrix.append(agi_mod)
            else:
                agi_mod = 1.0
                mod_matrix.append(agi_mod)
            if self.defence > other.defence:
                defence_mod = 1.2
                mod_matrix.append(defence_mod)
            elif self.defence < other.defence:
                defence_mod = 0.8
                mod_matrix.append(agi_mod)
            else:
                defence_mod = 1.0
                mod_matrix.append(agi_mod)
            return mod_matrix

class Styles(Fighters):
    def __init__(self, name, stam, agi, defence, stam_mod=1.0, agi_mod=1.0, defence_mod=1.0):
        super().__init__(name, stam, agi, defence, stam_mod, agi_mod, defence_mod)

    def winner(self, other):
        # must input same fighter1 and fighter 2 here:
        # insert fighter1 name        <----->
        mods1 = self.fighter_one_mods(samurai)
        win_value1 = []
        win_value1.append(1.0 * mods1[0])
        win_value1.append(1.0 * mods1[1])
        win_value1.append(1.0 * mods1[2])
        win_value1 = win_value1[0] + win_value1[1] + win_value1[2]
        print(win_value1)

        # insert fighter2 name       <----->
        mods2 = self.fighter_two_mods(shinobi)
        win_value2 = []
        win_value2.append(1.0 * mods2[0])
        win_value2.append(1.0 * mods2[1])
        win_value2.append(1.0 * mods2[2])
        win_value2 = win_value2[0] + win_value2[1] + win_value2[2]
        print(win_value2)
        
        if win_value1 > win_value2:
            return print("Fighter One Wins!!")
        elif win_value1 < win_value2:
            return print("Fighter Two Wins!!")
        else:
            return print("Tie game, please pick new fighters!!")

samurai = Styles("Sakai The Samurai", 90, 80, 90)
print(samurai)
print(samurai.stats_matrix())

shinobi = Styles("Ryuzo The Ronin", 80, 80, 70)
print(shinobi)
print(shinobi.stats_matrix())

archer = Styles("Ishikawa The Archer", 70, 70, 70)
print(archer)
print(archer.stats_matrix())

mods_one = Fighters.fighter_one_mods(samurai,shinobi)
print(mods_one)
mods_two = Fighters.fighter_two_mods(samurai, shinobi)
print(mods_two)

# need to input fighters here:
final_result = Styles.winner(samurai, shinobi)

print(final_result)
