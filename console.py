from models.creature import Creature
from models.habitat import Habitat

import repositories.creature_repository as creature_repo
import repositories.habitat_repository as habitat_repo

# delete all from list to avoid repeats
creature_repo.delete_all()
habitat_repo.delete_all()

# adding all habitats to the table
habitat_1 = Habitat('Forest',"https://api.time.com/wp-content/uploads/2018/05/forest-bathing.jpg")
habitat_repo.save(habitat_1)

habitat_2 = Habitat('Volcano', "https://cdn.britannica.com/34/231234-050-5B2280BB/volcanic-eruption-Antigua-Guatemala-volcano.jpg")
habitat_repo.save(habitat_2)

habitat_3 = Habitat('Ocean', "https://images.theconversation.com/files/223729/original/file-20180619-126566-1jxjod2.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=675.0&fit=crop")
habitat_repo.save(habitat_3)

habitat_4 = Habitat('Icy Tundra', "https://scx2.b-cdn.net/gfx/news/2020/2-arctic.jpg")
habitat_repo.save(habitat_4)

habitat_5 = Habitat('Mountain', "https://i.natgeofe.com/n/c9107b46-78b1-4394-988d-53927646c72b/1095.jpg")
habitat_repo.save(habitat_5)

habitat_6 = Habitat('Subteranean',"https://img.freepik.com/premium-photo/raster-illustration-beautiful-underground-lake-cave-with-drinking-water-rock-type-mountains-cave-stone-sculptures-dungeon-subterranean-spooky-sight-3d-rendering-background_76964-2554.jpg?w=2000")
habitat_repo.save(habitat_6)

habitat_7 = Habitat('Jungle', "https://www.telegraph.co.uk/content/dam/Travel/2018/September/El-Yunque-morning-mist-iStock-535499464.jpg")
habitat_repo.save(habitat_7)

# adding al creatures to table
# ------------------HABITAT 1----------------------------
creature1 = Creature('Dwarf',habitat_1,'A member of a mythical race of short, stocky humanlike creatures who are generally skilled in mining and metalworking',22 ,25.00 ,39.99, "https://i.pinimg.com/originals/53/1e/a8/531ea878c1d8e778feaba178f2616f1e.png")
creature_repo.save(creature1)

# creature2 = Creature('Forest Nymph',habitat_1,'A nature spirit who lives in trees and takes the form of a beautiful young woman',123,30.00 ,40.99)
# creature_repo.save(creature2)

creature3 = Creature('Unicorn',habitat_1,'A mythical creature resembling a horse, with a single horn in the center of its forehead',5 ,100.00 ,140.00, "https://img.freepik.com/premium-vector/cute-unicorn-standing-icon-illustration-unicorn-mascot-cartoon-character-animal-icon-concept-white-isolated_138676-831.jpg?w=2000")
creature_repo.save(creature3)


# ------------------HABITAT 2----------------------------
# creature4 = Creature('Cheruf',habitat_2,'An evil humanoid creature made of rock crystals and magma',2 ,300.00 ,350.00)
# creature_repo.save(creature4)

creature5 = Creature('Dragon',habitat_2,'A huge, bat-winged, fire-breathing, scaly lizard or snake with a barbed tail',3 ,229.00 ,299.99, "https://easydrawingguides.com/wp-content/uploads/2022/01/easy-cartoon-dragon-step-by-step-drawing-tutorial-step-10.png")
creature_repo.save(creature5)

# creature6 = Creature('Hydra',habitat_2,'A ferocious snake-like monster with multiple heads, one of which was immortal and the rest of which will spawn multiple new heads if destroyed.',1 ,1000.00 ,1200.00)
# creature_repo.save(creature6)


# ------------------HABITAT 3----------------------------
creature7 = Creature('Kraken',habitat_3,'A gigantic tentacled sea monster of Scandinavian myth',2 ,1100.00 ,1220.00, "https://img.freepik.com/free-vector/cute-angry-octopus-cartoon-vector-icon-illustration-animal-nature-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-3635.jpg?w=2000")
creature_repo.save(creature7)

# creature8 = Creature('Siren',habitat_3,'A creature half bird and half woman who lures sailors to theri death',125 ,24.00 ,32.99)
# creature_repo.save(creature8)

# creature9 = Creature('Leviathan',habitat_3,'An enormous multi-headed sea serpent',1 ,4000.00 ,4500.00)
# creature_repo.save(creature9)


# ------------------HABITAT 4----------------------------
creature10 = Creature('Yeti',habitat_4,'Has white shaggy fur and a lean muscular body like an ape',24,15.00 ,28.50, "https://static.vecteezy.com/system/resources/previews/003/777/947/original/yeti-cartoon-illustrations-free-vector.jpg")
creature_repo.save(creature10)

# creature11 = Creature('Giant',habitat_4,'Enormous size and strength packed in a human form. Their main source of food is humans', 50, 28.00 ,42.99)
# creature_repo.save(creature11)


# ------------------HABITAT 5----------------------------
creature12 = Creature('Griffin',habitat_5,'Mythical creature known as a half-eagle, half-lion in various cultures. In legends and folklore, the beast guards the gold of the kings, as well as other priceless possessions.',220 ,30.00 ,50.00,"https://howtodrawforkids.com/wp-content/uploads/2022/01/how-to-draw-a-griffin.jpg" )
creature_repo.save(creature12)

creature13 = Creature('Troll',habitat_5,'trolls are huge. The adult troll has small, beady eyes, a bulbous, warty nose and sharp, yellow teeth. Most trolls have long, curly horns on their heads similar to a goat',250 ,5.00 ,12.99, "https://t4.ftcdn.net/jpg/03/11/23/11/360_F_311231181_62FSitmUD9CFrJIrQrIrFegwzriw9vt5.jpg")
creature_repo.save(creature13)


# ------------------HABITAT 6---------------------------- 
# creature17 = Creature('Golem',habitat_6,'A creature formed out of a lifeless substance such as dust or earth that is brought to life by ritual incantations and sequences of Hebrew letters',300 ,10.00 ,20.00)
# creature_repo.save(creature17)

creature18 = Creature('Minotaur',habitat_6,'monster of Crete that had the body of a man and the head of a bull',28,43.00 ,55.50, "https://thumbs.dreamstime.com/b/minotaur-eps-illustration-design-47882875.jpg")
creature_repo.save(creature18)


# ------------------HABITAT 7----------------------------
creature15 = Creature('Goblin',habitat_7,'A wandering sprite that is usually mischievous but often malicious',420 ,6.00 ,9.99, "https://static.vecteezy.com/system/resources/previews/004/497/587/original/funny-cartoon-goblin-or-troll-face-with-different-expressions-character-vector.jpg")
creature_repo.save(creature15)

creature16 = Creature('Dan',habitat_7,'A magical creature with a tiny human body and wings',312 ,7.00 ,13.99, "https://thumbs.dreamstime.com/b/cartoon-fairy-girl-flying-spreading-magical-dust-brown-haired-pixie-cute-pink-dress-fairytale-character-little-wings-108647922.jpg")
creature_repo.save(creature16)


