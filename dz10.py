class animal:
    def make_sound(self):
        print("животное издает звук")

class dog(animal):
    def make_sound(self):
        print("собака говорит гав гав")

class cat(animal):
    def make_sound(self):
        print("кошка говорит мяу")

class cow(animal):
    def make_sound(self):
        print("корова говорит мууу")

dog_instance = dog()
cat_instance = cat()
cow_instance = cow()

dog_instance.make_sound()
cat_instance.make_sound()
cow_instance.make_sound()