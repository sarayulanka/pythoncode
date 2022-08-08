# scope is basically the concept of where you can use a specific block of code
# For exmaple, when you define parameters to a function, where can you use the parameters?
# You can use the parameters inside the function you defined it to and not anywhere outside the function
# That is called scope

# Now that we know the basic concept of scope, let's talk about two types of scope
# The two scopes we are going to talk about are called local scope and global scope

# We are first going to talk about local scope:
# Local scope exists within functions

# To explain local scope, let me first create a function:

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Now we have created a variable named potion_strength inside the function and we printed it and got 2
# However, what if I wanted to print it out side the function?
# Try it out and you should get a name error saying that potion_strength isn't defined
# But that doesn't make sense, we defined it
# The reason it gives a name error is that potion_strength was only defined INSIDE the function
# Outside the function, there is no variable named potion_strength which is why we get a name error
# potion_strength is only valid inside the function drink_potion
# and that is called local scope


# Now let's talk about the second type of scope called global scope
# The only difference between global scope and local scope is that global scope can be accessed inside or outside of functions
# Let's try creating a variable that demonstrates the concept of global scope

player_strength = 10

def drink_potion2():
    potion_strength2 = 2
    print(player_strength)

drink_potion2()
print(player_strength)

# The variable player_strength demonstrated global scope because
# player_strength was able to be used both outside and inside the function without getting a name error

# Now global scope and local scope apply to anything you name. It can be lists, variables, etc.
# this full concept is called name space


# Now we are going to focus on how to modify variables using global scope.
# Let's create a function, analyze it, and then modify the variable using global scope

enemies = "skeleton"

def modify_enemy():
    enemies = "vampires"
    print(enemies)

modify_enemy
print(enemies)

# What we wanted to do was modify the variable and print it inside the function
# The problem with this code is that the first enemies variable is outside the function so it's a global scope
# But the second enemies variable was inside the function which makes it a ompletetly different variable which is local scope
# when we put enemies inside the function, we made a new enemies variable instead of taking a parameter and changing the old one
# Now let's try and fix it using global scope

# The way to fix this code is to specifically say in the function that enemies is a global scope variable
# and then it will know to change the old one instead of creating a new variable
# Let's make this code work correctly:

enemies2 = "skeleton"

def modify_enemies2():
    global enemies2
    enemies2 = "vampires"
    print(enemies2)

modify_enemy()
print()

# Now we get the same value meaning that the function successfully changed the global variable
# to contain vampires instead of skeleton