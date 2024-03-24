from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(173, 90, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, mp=10, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),    
)
orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, mp=0, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),   
    level=Level(xp_given=35),    
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, mp=0, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0), 
    level=Level(xp_given=100),    
)

goblin = Actor(
    char="g",
    color=(127, 127, 0),
    name="Goblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=6, mp=0, base_defense=0, base_power=2),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=20),
)

dragon = Actor(
    char="D",
    color=(255, 0, 0),
    name="Dragon",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=50, mp=0, base_defense=5, base_power=10),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=500),
)

skeleton = Actor(
    char="S",
    color=(192, 192, 192),
    name="Skeleton",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=8, mp=0, base_defense=1, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=30),
)

ghost = Actor(
    char="G",
    color=(127, 127, 255),
    name="Ghost",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=12, mp=0, base_defense=2, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=40),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    color=(68, 103, 161),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger())
shortsword = Item(char="/", color=(0, 191, 255), name="Short Sword", equippable=equippable.ShortSword())
sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

battle_axe = Item(char="/",color=(255, 0, 0),name="Battle Axe",equippable=equippable.BattleAxe())
staff = Item(    char="/",    color=(128, 128, 128),    name="Staff",    equippable=equippable.Staff())
wand = Item(    char="/",    color=(255, 255, 0),    name="Wand",    equippable=equippable.Wand())
plate_armor = Item(char="[",color=(192, 192, 192),name="Plate Armor", equippable=equippable.PlateArmor())
robe = Item(    char="[",    color=(0, 0, 255),    name="Robe",    equippable=equippable.Robe())

leather_armor = Item(char="[",color=(139, 69, 19),name="Leather Armor",equippable=equippable.LeatherArmor())
chain_mail = Item(char="[", color=(0, 191, 255), name="Chain Mail", equippable=equippable.ChainMail())