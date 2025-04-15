class user:
    def __init__(self, user, comments, like=0):
        self.user = user
        self.comments = comments
        self.like = like
    def add_like(self):
        self.like +=1
        return self.like

comment1 = user("Oleg", "салам")
print(comment1.like)
print(comment1.add_like())

#НЕ УДАЛЯТЬ!!!
