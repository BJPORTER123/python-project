from models.creature import Creature
from models.habitat import Habitat

import repositories.creature_repository as creature_repo
import repositories.habitat_repository as habitat_repo

# delete all from list to avoid repeats
creature_repo.delete_all()
habitat_repo.delete_all()

# adding all habitats to the table
habitat_1 = Habitat('Forest')
habitat_repo.save(habitat_1)

habitat_2 = Habitat('Volcano')
habitat_repo.save(habitat_2)

habitat_3 = Habitat('Ocean')
habitat_repo.save(habitat_3)

habitat_4 = Habitat('Icy Tundra')
habitat_repo.save(habitat_4)

habitat_5 = Habitat('Mountain')
habitat_repo.save(habitat_5)

habitat_6 = Habitat('Subteranean')
habitat_repo.save(habitat_6)

habitat_7 = Habitat('Jungle')
habitat_repo.save(habitat_7)

# adding al creatures to table
# ------------------HABITAT 1----------------------------
creature1 = Creature('Dwarf',habitat_1,'A member of a mythical race of short, stocky humanlike creatures who are generally skilled in mining and metalworking',22 ,25.00 ,39.99)
creature_repo.save(creature1)

creature2 = Creature('Forest Nymph',habitat_1,'A nature spirit who lives in trees and takes the form of a beautiful young woman',123,30.00 ,40.99)
creature_repo.save(creature2)

creature3 = Creature('Unicorn',habitat_1,'A mythical creature resembling a horse, with a single horn in the center of its forehead',5 ,100.00 ,140.00)
creature_repo.save(creature3)


# ------------------HABITAT 2----------------------------
creature4 = Creature('Cheruf',habitat_2,'An evil humanoid creature made of rock crystals and magma',2 ,300.00 ,350.00)
creature_repo.save(creature4)

creature5 = Creature('Dragon',habitat_2,'A huge, bat-winged, fire-breathing, scaly lizard or snake with a barbed tail',3 ,229.00 ,299.99)
creature_repo.save(creature5)

creature6 = Creature('Hydra',habitat_2,'A ferocious snake-like monster with multiple heads, one of which was immortal and the rest of which will spawn multiple new heads if destroyed.',1 ,1000.00 ,1200.00)
creature_repo.save(creature6)


# ------------------HABITAT 3----------------------------
creature7 = Creature('Kraken',habitat_3,'A gigantic tentacled sea monster of Scandinavian myth',2 ,1100.00 ,1220.00)
creature_repo.save(creature7)

creature8 = Creature('Siren',habitat_3,'A creature half bird and half woman who lures sailors to theri death',125 ,24.00 ,32.99)
creature_repo.save(creature8)

creature9 = Creature('Leviathan',habitat_3,'An enormous multi-headed sea serpent',1 ,4000.00 ,4500.00)
creature_repo.save(creature9)


# ------------------HABITAT 4----------------------------
creature10 = Creature('Yeti',habitat_4,'Has white shaggy fur and a lean muscular body like an ape',24,15.00 ,28.50)
creature_repo.save(creature10)

creature11 = Creature('Giant',habitat_4,'Enormous size and strength packed in a human form. Their main source of food is humans', 50, 28.00 ,42.99)
creature_repo.save(creature11)


# ------------------HABITAT 5----------------------------
creature12 = Creature('Griffin',habitat_5,'Mythical creature known as a half-eagle, half-lion in various cultures. In legends and folklore, the beast guards the gold of the kings, as well as other priceless possessions.',220 ,30.00 ,50.00)
creature_repo.save(creature12)

creature13 = Creature('Troll',habitat_5,'trolls are huge. The adult troll has small, beady eyes, a bulbous, warty nose and sharp, yellow teeth. Most trolls have long, curly horns on their heads similar to a goat',250 ,5.00 ,12.99)
creature_repo.save(creature13)


# ------------------HABITAT 6---------------------------- 
creature17 = Creature('Golem',habitat_6,'A creature formed out of a lifeless substance such as dust or earth that is brought to life by ritual incantations and sequences of Hebrew letters',300 ,10.00 ,20.00)
creature_repo.save(creature17)

creature18 = Creature('Minotaur',habitat_6,'monster of Crete that had the body of a man and the head of a bull',28,43.00 ,55.50)
creature_repo.save(creature18)


# ------------------HABITAT 7----------------------------
creature15 = Creature('Goblin',habitat_7,'A wandering sprite that is usually mischievous but often malicious',420 ,6.00 ,9.99)
creature_repo.save(creature15)

creature16 = Creature('Fairy',habitat_7,'A magical creature with a tiny human body and wings',312 ,7.00 ,13.99)
creature_repo.save(creature16)


