import re

itemsList = open("input.txt").read().split()
items = {''.join(i) for i in itemsList}
slotmatch = ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B', '3C', '3D', '4A', '4B', '4C', '4D', '5A', '5B', '5C', '5D', '6A', '6B', '6C', '6D', '7A', '7B', '7C', '7D', '8A', '8B', '8C', '8D', '9A', '9B', '9C', '9D']

def build(file):
    command = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    code = open(file, 'r', encoding='utf-8').read().splitlines()

    for line in code:
        # setItem command
        if line.startswith("setItem"):
            args = re.match(r"setItem\((?:\"|\')(.*)(?:\"|\'),(?:\"|\')(.*)(?:\"|\')\)",line)
            slot = slotmatch.index(args[1])
            if args[2] not in items:
                raise ValueError(f"Unknown item at line {line}: '{args[2]}'")
            command[slot].append(r"{pools:[{rolls:1,entries:[{type:\"minecraft:item\",name:minecraft:" + args[2] + r"}]}]}")
            
    return command