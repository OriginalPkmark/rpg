from playertype import Warrior, Support, Tank, Thief, Assassin

def print_player_info(player):
    print("- Max HP:", player.get_max_hp())
    print("- Max SHIELD:", player.get_max_shield_hp())
    print("- Strength:", player.get_strength())
    print("- Intellect:", player.get_intellect())
    print("- Agility:", player.get_agility())
    print("- Mana:", player.get_mana())
    print("- Luck:", player.get_luck())

def main():
    warrior1 = Warrior()
    support1 = Support()
    tank1 = Tank()
    thief1 = Thief()
    assassin1 = Assassin()

    print("Warrior:")
    print_player_info(warrior1)

    print("\nSupport:")
    print_player_info(support1)

    print("\nTank:")
    print_player_info(tank1)

    print("\nThief:")
    print_player_info(thief1)

    print("\nAssassin:")
    print_player_info(assassin1)

if __name__ == "__main__":
    main()
