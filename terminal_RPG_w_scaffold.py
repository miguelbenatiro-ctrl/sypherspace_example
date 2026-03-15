import random

# TODO: Set the player's starting HP
player_hp = ______

# TODO: Set the goblin's starting HP
enemy_hp = ______

print("A wild Goblin appears!")

# TODO: Complete the battle condition so the fight continues
# while BOTH the player and enemy still have HP
while ______________________________:

    print("\nYour HP:", player_hp)
    print("Goblin HP:", enemy_hp)

    print("\nChoose an action:")
    print("1 - Attack")
    print("2 - Heal")

    choice = input("> ")

    # Attack option
    if choice == "1":

        # TODO: Generate random damage
        damage = random.randint(____ , ____)

        # TODO: Reduce the enemy HP by the damage
        enemy_hp = ______________________

        print("You dealt", damage, "damage!")

    # Heal option
    elif choice == "2":

        # TODO: Generate a heal amount
        heal = random.randint(____ , ____)

        # TODO: Increase the player's HP by the heal amount
        player_hp = ______________________

        print("You healed", heal, "HP!")

    else:
        print("Invalid choice!")

    # Goblin attacks back if still alive
    if enemy_hp > 0:

        # TODO: Generate enemy damage
        enemy_damage = random.randint(____ , ____)

        # TODO: Reduce player HP by enemy damage
        player_hp = ______________________

        print("Goblin dealt", enemy_damage, "damage!")

# End of battle
# TODO: Finish the win condition
if __________________:
    print("\nYou defeated the Goblin!")
else:
    print("\nYou were defeated...")
