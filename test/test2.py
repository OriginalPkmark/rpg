class HP:
    def __init__(self, current_hp=1, max_hp=1, current_shield=1, max_shield=1):
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.current_shield = current_shield
        self.max_shield = max_shield
        
    def set_max_hp(self, new_max_hp):
        if new_max_hp < 1:
            return False
        self.max_hp = new_max_hp
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
        return True
    
    def set_max_shield(self, new_max_shield):
        if new_max_shield < 1:
            return False
        self.max_shield = new_max_shield
        if self.current_shield > self.max_shield:
            self.current_shield = self.max_shield
        return True
    
    def take_damage(self, damage):
        if damage >= self.current_hp + self.current_shield:
            self.current_hp = 0
            self.current_shield = 0
        elif damage <= self.current_shield:
            self.current_shield -= damage
        elif damage >= self.current_shield:
            remaining_damage = damage - self.current_shield
            self.current_shield = 0
            self.current_hp -= remaining_damage
    
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.pos_overheal()
    
    def heal_shield_hp(self, amount):
        self.current_shield += amount
        if self.current_shield > self.max_shield:
            self.current_shield = self.max_shield
    
    def pos_overheal(self):
        if self.current_hp > self.max_hp:
            overheal_amount = self.current_hp - self.max_hp
            self.current_hp = self.max_hp
            self.current_shield += overheal_amount
            if self.current_shield > self.max_shield:
                self.current_shield = self.max_shield
