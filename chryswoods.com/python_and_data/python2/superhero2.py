"""
This module provides a set of classes for creating superheros
and supervillains. Have fun!

Author - Christopher Woods
License - BSD
"""

class Superhero:
    """This class allows you to create your own Superhero"""
    def __init__(self, name, weakness):
        """Construct a superhero with the specified name and the 
           specified weakness
        """
        self.setName(name)
        self.setWeakness(weakness)

    def setName(self, name):
        """Set the name of the superhero"""
        self._name = name

    def setWeakness(self, weakness):
        """Set the weakness of the superhero"""
        self._weakness = weakness

    def getName(self):
        """Return the name of the superhero"""
        return self._name

    def getWeakness(self):
        """Return the weakness of the superhero"""
        return self._weakness

    def isVulnerableTo(self, item):
        """Return whether or not this superhero is 
           vulnerable to 'item'"""
        return self.getWeakness().lower() == item.lower()

class Supervillain:
    """This class allows you to create your own supervillain"""
    def __init__(self, name):
        self.setName(name)
        self._loot = []

    def setName(self, name):
        """Set the name of the villain"""
        self._name = name

    def getName(self):
        """Return the name of the villain"""
        return self._name

    def steal(self, item):
        """Tell the villain to steal 'item'"""
        self._loot.append(item)

    def getLoot(self):
        """Return all of the loot that this villain has stolen"""
        return self._loot

def battle(superhero, supervillain):
    """This function will pitch the superhero and villain
       into battle, and will return the name of whoever wins!
    """

    try:
        for possession in supervillain.getLoot():
            if superhero.isVulnerableTo(possession):
                return supervillain.getName()
        return superhero.getName()
    except Exception as e:
        # Draw, so no-one won!
        return "No-one, because %s" % e

if __name__ == "__main__":
    superman = Superhero(name="Superman", weakness="kryptonite")

    print("Is it a bird? Is it a plane? No, it's %s!!!" % superman.getName())

    lex = Supervillain(name="Lex Luther")

    print("%s will battle %s. The winner is %s" \
       % (superman.getName(), lex.getName(), \
          battle(superman, lex) ) )

    print("Lex steals some krytonite...")
    lex.steal("kryptonite")

    print("They battle again... The winner is %s" \
        % battle(superman, lex))

