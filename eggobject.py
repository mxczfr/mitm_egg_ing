import binascii

class EpicResearch:

    def __init__(self):
        self.research = {}
        
        # Contains the maximum values for every modifier
        self.researchs = {
        'hold_to_hatch':10,
        'epic_hatchery':20,
        'epic_internal_incubators':20,
        'video_doubler_time':12,
        'epic_clucking':10,
        'epic_multiplier':75,
        'cheaper_contractors':10,
        'bust_unions':10,
        'cheaper_research':10,
        'epic_silo_quality':40,
        'silo_capacity':10,
        'int_hatch_sharing':10,
        'int_hatch_calm':20,
        'accounting_tricks':20,
        'soul_eggs':140,
        'prestige_bonus':20,
        'drone_rewards':20,
        'epic_egg_laying':20,
        'transportation_lobbyist':30,
        'warp_shift':16,
        'prophecy_bonus':5,
        'hold_to_research':8
        }

    def processing(self, binary_save, research_name):
        size = len(research_name)
        index = binary_save.index(research_name.encode())
        value = binary_save[index + size + 1: index + size + 2]  # +1 to skip the x10 bytes
        return int(value.hex(), 16)

    def run(self, binary_save):
        for name in self.researchs:
            self.research[name] = self.processing(binary_save, name)

    def mod(self, binary_save):
        for name in self.researchs:

            if name == 'soul_eggs': #I have bug with this one. Backup corruption or something like that
                continue

            size = len(name)
            index = binary_save.index(name.encode())

            full_name = binary_save[index : index + size + 2]
            value = binary_save[index + size + 1: index + size + 2]  # +1 to skip the x10 bytes

            new_value = i2b(self.researchs[name])
            binary_save = binary_save.replace(full_name, full_name.replace(value, new_value))

        return binary_save

    def display(self):
        for name in self.research_names:
            print("{} : {}".format(name, self.research[name]))


def i2b(value):
    h_val = convert_hex(hex(value))
    return binascii.a2b_hex(h_val)

def convert_hex(hex):
    if len(hex) > 3:
        return hex.replace('0x','')
    return hex.replace('x','')
