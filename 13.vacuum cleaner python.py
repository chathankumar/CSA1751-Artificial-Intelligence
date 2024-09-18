class VacuumCleaner:
    def __init__(self):
        self.room = 'A'  
        self.dirt = {'A': True, 'B': True}  
    def is_dirty(self):
        return self.dirt[self.room]
    def clean(self):
        if self.is_dirty():
            print(f"Cleaning room {self.room}")
            self.dirt[self.room] = False
        else:
            print(f"Room {self.room} is already clean")
    def move(self):
        if self.room == 'A':
            self.room = 'B'
        else:
            self.room = 'A'
        print(f"Moved to room {self.room}")
    def run(self):
        steps = 0
        while any(self.dirt.values()):
            print(f"Step {steps}:")
            if self.is_dirty():
                self.clean()
            else:
                self.move()
            steps += 1
        print("All rooms are clean!")
vacuum = VacuumCleaner()
vacuum.run()
