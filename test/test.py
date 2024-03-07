from test2 import HP



class TestWarrior:
    def __init__(self):
        self.hit_points = HP(current_hp=100, max_hp=100, current_shield=100, max_shield=100)

# Create a TestWarrior instance
test_warrior = TestWarrior()

# Access the hit points and shield of the test warrior
print("Initial HP:", test_warrior.hit_points.current_hp)
print("Initial Max HP:", test_warrior.hit_points.max_hp)
print("Initial Shield:", test_warrior.hit_points.current_shield)
print("Initial Max Shield:", test_warrior.hit_points.max_shield)




while True:
    # Display options to the user
    print("Options:")
    print("1. Attack")
    print("2. Heal HP")
    print("3. Heal Shield")
    print("4. Exit")

    # Get user input
    choice = input("Enter your choice (1/2/3/4): ")

    # Process user choice
    if choice == '1':
        # Attack
        damage = int(input("Enter the damage amount: "))
        test_warrior.hit_points.take_damage(damage)
        print("Warrior's HP after taking damage:", test_warrior.hit_points.current_hp)
        print("Warrior's Shield after taking damage:", test_warrior.hit_points.current_shield)
    elif choice == '2':
        # Heal HP
        amount = int(input("Enter the amount to heal HP: "))
        test_warrior.hit_points.heal(amount)
        print("Warrior's HP after healing:", test_warrior.hit_points.current_hp)
    elif choice == '3':
        # Heal Shield
        amount = int(input("Enter the amount to heal Shield: "))
        test_warrior.hit_points.heal_shield_hp(amount)
        print("Warrior's Shield after healing:", test_warrior.hit_points.current_shield)
    elif choice == '4':
        # Exit the loop
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
