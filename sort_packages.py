class sort_packages:
    
    def __init__(self):
        self.standard = []
        self.special = []
        self.rejected = []
    
    def sort(self, width, height, length, mass):
        if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
            return "Invalid"
        
        if self.is_bulky(width, height, length) and self.is_heavy(mass):
            self.rejected.append([width, height, length, mass])
            return "Rejected"
        elif self.is_bulky(width, height, length) or self.is_heavy(mass):
            self.special.append([width, height, length, mass])
            return "Special"
        else:
            self.standard.append([width, height, length, mass])
            return "Standard"
        
    def is_bulky(self, width, height, length):
        if width >= 150 or height >= 150 or length >= 150:
            return True
        
        if width * height * length >= 1000000:
            return True

    def is_heavy(self, mass):
        if mass >= 20:
            return True
        


sort_obj = sort_packages()

print(sort_obj.sort(100, 100, 100, 10))
print(sort_obj.sort(100, 100, 100, 20))
print(sort_obj.sort(150, 150, 150, 10))
print(sort_obj.sort(150, 150, 150, 20))
print(sort_obj.sort(15, 15, 15, 10))