class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __repr__(self):
        return f"{self.name}({self.id})"
    def __str__(self):
        return self.name

    
employees = [Employee(1, "Sarayu"), Employee(2, "Sarada"), Employee(3, "Raghu")]

for i in employees:
    print(i)

# By default when the print statement is called, dunder str will be executed. Now
# that we have given a value to the dunder str function, print will call that function

# Dunder repr isn't called when dunder str is given a value, only when it isn't
# given a value

# to explicitly call Dunder repr, do print(repr(i))

# repr(value) -> value.__repr__
# str(value) -> value.__str__