from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        #pass
            print("This scene is not yet configured.")
            exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while  True:
            print('\n-------')
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
        "You dies. You kinda suck at this",
        "Your mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an " )
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when" )
        print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the" )
        print("Armory and about to pull a weapon to blast you.")

        action = input(">")

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your laser hits his costume but misses him entirely. This")
            print("completely ruins his brand new costume his mother bought him, which")
            print("makes him fly into a rage and blast you repeatedly in the face until")
            print("you are dead. Then he eats you.")
            return 'death'

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            return 'death'

        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")

        else:
            print("Lucky for you they made you learn Gothon insults in the academy.")
            return 'central_corridor'



class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):   

    def enter(self):
        #print("You rush through the ship desperately trying to make it to")
        #print("the escape pod before the whole ship explodes. It seems like"）
        print("hardly any Gothons are on the ship, so your run is clear of"）
        print("interference. You get to the chamber with the escape pods, and"）
        print("now need to pick one to take. Some of them could be damaged"）
        print("but you don't have time to look. There's 5 pods, which one"）
        print("do you take?"）

        good_pod = randint(1,5)
        guess = input("[pod #]>")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            return 'You won. finished'


class Map(object):

    scenes = [
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    ]

    def __init__(self, start_scene):
        #print('init')
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map("CentralCorridor")
a_game = Engine(a_map)
a_game.play()
