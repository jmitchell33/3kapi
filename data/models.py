from django.db import models

# Create your models here.

DAMAGE_CHOICES = (
    ('edged', 'edged'),
    ('blunt', 'blunt'),
    ('fire', 'fire'),
    ('ice', 'ice'),
    ('acid', 'acid'),
    ('electricity', 'electricity'),
    ('mind', 'mind'),
    ('energy', 'energy'),
    ('poison', 'poison'),
    ('radiation', 'radiation')
)

COMPONENT_QUALITY_CHOICES = (
    ('legendary', 'legendary'),
    ('superior', 'superior'),
    ('good', 'good'),
    ('average', 'average'),
    ('poor', 'poor'),
)

COMPONENT_CHOICES = (
    ('aquamarine', 'aquamarine'),
    ('aquamarine dust', 'aquamarine dust'),
    ('copper shards', 'copper shards'),
    ('morganite', 'morganite'),
    ('morganite dust', 'morganite dust'),
    ('tigers eye', 'tigers eye'),
    ('tigers eye dust', 'tigers eye dust'),
    ('fragment of light', 'fragment of light'),
    ('fragment of water', 'fragment of water'),
    ('fragment of shadow', 'fragment of shadow'),
    ('bronze shards', 'bronze shards'),
    ('cats eye', 'cats eye'),
    ('cats eye dust', 'cats eye dust'),
    ('eye of flame', 'eye of flame'),
    ('garnet', 'garnet'),
    ('garnet dust', 'garnet dust'),
    ('fragment of might', 'fragment of might'),
    ('alexandrite', 'alexandrite'),
    ('alexandrite dust', 'alexandrite dust'),
    ('eye of frost', 'eye of frost'),
    ('iron shards', 'iron shards'),
    ('fragment of rejuvenation', 'fragment of rejuvenation'),
    ('fragment of rage', 'fragment of rage'),
    ('fragment of soul', 'fragment of soul'),
    ('steel shards', 'steel shards'),
    ('fragment of the unseen', 'fragment of the unseen'),
    ('beryl', 'beryl'),
    ('beryl dust', 'beryl dust'),
    ('eye of earth', 'eye of earth'),
    ('pyrite', 'pyrite'),
    ('pyrite dust', 'pyrite dust'),
    ('roans tears', 'roans tears'),
    ('silver shards', 'silver shards'),
    ('tourmaline', 'tourmaline'),
    ('tourmaline dust', 'tourmaline dust'),
    ('fragment of ascension', 'fragment of ascension'),
    ('fragment of blasting', 'fragment of blasting'),
    ('fragment of damnation', 'fragment of damnation'),
    ('amethyst', 'amethyst'),
    ('amethyst dust', 'amethyst dust'),
    ('eye of air', 'eye of air'),
    ('gold shards', 'gold shards'),
    ('happy eds tears', 'happy eds tears'),
    ('topaz', 'topaz'),
    ('topaz dust', 'topaz dust'),
    ('fragment of willy', 'fragment of willy'),
    ('fragment of destruction', 'fragment of destruction'),
    ('fragment of compassion', 'fragment of compassion'),
    ('fragment of knowledge', 'fragment of knowledge'),
    ('core of flame', 'core of flame'),
    ('essence of light', 'essence of light'),
    ('heliodor', 'heliodor'),
    ('heliodor dust', 'heliodor dust'),
    ('hematite', 'hematite'),
    ('hematite dust', 'hematite dust'),
    ('mithril shards', 'mithril shards'),
    ('essence of water', 'essence of water'),
    ('essence of shadow', 'essence of shadow'),
    ('essence of might', 'essence of might'),
    ('core of frost', 'core of frost'),
    ('peridot', 'peridot'),
    ('peridot dust', 'peridot dust'),
    ('titanium shards', 'titanium shards'),
    ('essence of rejuvenation', 'essence of rejuvenation'),
    ('essence of rage', 'essence of rage'),
    ('essence of soul', 'essence of soul'),
    ('essence of the unseen', 'essence of the unseen'),
    ('core of earth', 'core of earth'),
    ('ebon shards', 'ebon shards'),
    ('essence of ascension', 'essence of ascension'),
    ('essence of blasting', 'essence of blasting'),
    ('adamantim shards', 'adamantim shards'),
    ('core of air', 'core of air'),
    ('essence of damnation', 'essence of damnation'),
    ('pearl', 'pearl'),
    ('pearl dust', 'pearl dust'),
    ('essence of willy', 'essence of willy'),
    ('essence of destruction', 'essence of destruction'),
    ('ghotis tears', 'ghotis tears'),
    ('obsidian shards', 'obsidian shards'),
    ('opal', 'opal'),
    ('opal dust', 'opal dust'),
    ('essence of compassion', 'essence of compassion'),
    ('essence of knowledge', 'essence of knowledge'),
    ('star of flame', 'star of flame'),
    ('nethernium shards', 'nethernium shards'),
    ('heart of light', 'heart of light'),
    ('heart of water', 'heart of water'),
    ('heart of shadow', 'heart of shadow'),
    ('heart of might', 'heart of might'),
    ('diamond', 'diamond'),
    ('diamond dust', 'diamond dust'),
    ('star of frost', 'star of frost'),
    ('shansabyks tears', 'shansabyks tears'),
    ('voidstone shards', 'voidstone shards'),
    ('heart of rejuvenation', 'heart of rejuvenation'),
    ('heart of rage', 'heart of rage'),
    ('heart of soul', 'heart of soul'),
    ('emerald', 'emerald'),
    ('emerald dust', 'emerald dust'),
    ('star of air', 'star of air'),
    ('star of earth', 'star of earth'),
    ('sapphire dust', 'sapphire dust'),
    ('sapphire', 'sapphire'),
    ('phasemetal shards', 'phasemetal shards'),
    ('heart of the unseen', 'heart of the unseen'),
    ('heart of ascension', 'heart of ascension'),
    ('heart of blasting', 'heart of blasting'),
    ('heart of damnation', 'heart of damnation'),
    ('chaostone shards', 'chaostone shards'),
    ('ruby', 'ruby'),
    ('heart of willy', 'heart of willy'),
    ('heart of destruction', 'heart of destruction'),
    ('heart of compassion', 'heart of compassion'),
    ('heart of knowledge', 'heart of knowledge'),
    ('mithril ore', 'mithril ore'),
    ('titanium ore', 'titanium ore'),
    ('ebon ore', 'ebon ore'),
    ('obsidian ore', 'obsidian ore'),
    ('nethernium ore', 'nethernium ore'),
    ('voidstone ore', 'voidstone ore'),
    ('phasemetal ore', 'phasemetal ore'),
    ('chaostone ore', 'chaostone ore')
)

ATTACK_TYPE_CHOICES = (
    ('Normal', 'Normal'),
    ('Special', 'Special')
)

WEIGHT_CHOICES = (
    ("It looks very light.", "It looks very light."),
    ("It looks light.", "It looks light."),
    ("It doesn't look too heavy.", "It doesn't look too heavy."),
    ("It looks heavy.", "It looks heavy."),
    ("It would take considerable effort to lift this.", "It would take considerable effort to lift this."),
    ("You'll most likely herniate a disc lifting this.", "You'll most likely herniate a disc lifting this.")
)

ITEM_CLASSIFICATION = (
    ('Normal', 'Normal'),
    ('Legendary', 'Legendary'),
    ('World Drop', 'World Drop'),
    ('Guild Artifact', 'Guild Artifact')
)

ITEM_SLOT = (
    ('Object', 'Object'),
    ('Weapon', 'Weapon'),
    ('Wand', 'Wand'),
    ('Head', 'Head'),
    ('Around neck', 'Around neck'),
    ('Heavy Body', 'Heavy Body'),
    ('Upper body', 'Upper body'),
    ('On legs', 'On legs'),
    ('Light body', 'Light body'),
    ('Hands', 'Hands'),
    ('Feet', 'Feet'),
    ('On fingers', 'On fingers'),
    ('Shield', 'Shield'),
    ('Other', 'Other'),
    ('Magical', 'Magical'),
    ('Unknown', 'Unknown'),
    ('Cloak', 'Cloak'),
    ('Ring', 'Ring'),
    ('Armour', 'Armour'),
    ('Other', 'Other'),
    ('Amulet', 'Amulet'),
    ('Helmet', 'Helmet'),
    ('Gloves', 'Gloves'),
    ('Boots', 'Boots'),
    ('Headband', 'Headband'),
)

ITEM_MUD_TYPE = (
    ('i','i'),
    ('a','a'),
    ('w', 'w'),
    ('o', 'o'),
)

REALM_CHOICES = (
    ('Chaos', 'Chaos'),
    ('Fantasy', 'Fantasy'),
    ('Science,', 'Science'),
    ('Pinnacle', 'Pinnacle')
)

class Area(models.Model):
    name = models.CharField(max_length=255, blank=False)
    wizard = models.CharField(max_length=255, blank=True)
    realm = models.CharField(choices=REALM_CHOICES, max_length=100, blank=True)
    dungeon = models.BooleanField(default=False)
    room_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    roomID = models.IntegerField(blank=True, null=True)
    parent_area = models.ForeignKey(Area, related_name='area_rooms', on_delete=models.CASCADE, blank=True, null=True)
    room_short = models.CharField(max_length=255, blank=True)
    room_exits = models.CharField(max_length=255, blank=True)
    room_long = models.TextField(blank=True)

    def __str__(self):
        return self.room_short

class Monster(models.Model):
    parent_area = models.ForeignKey(Area, related_name='area_monsters', on_delete=models.CASCADE, blank=True, null=True)
    parent_room = models.ForeignKey(Room, related_name='room_monsters', on_delete=models.CASCADE, blank=True, null=True)
    short = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    size = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    scaler = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%a (Sclr: %a)' % (self.short, self.scaler)

class Monster_AttackType(models.Model):
    parent_monster = models.ForeignKey(Monster, related_name='monster_damage_types', on_delete=models.CASCADE, blank=True, null=True)
    damage_type = models.CharField(choices=DAMAGE_CHOICES, max_length=50, blank=True)
    attack_type = models.CharField(choices=ATTACK_TYPE_CHOICES, max_length=50, blank=True)

class Item(models.Model):
    parent_monster = models.ForeignKey(Monster, related_name='monster_items', on_delete=models.CASCADE, blank=True, null=True)
    parent_area = models.ForeignKey(Area, related_name='area_items', on_delete=models.CASCADE, blank=True, null=True)
    parent_room = models.ForeignKey(Room, related_name='room_items', on_delete=models.CASCADE, blank=True, null=True)
    short = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    type = models.CharField(choices=ITEM_MUD_TYPE, max_length=10, blank=True)
    classifaction = models.CharField(choices=ITEM_CLASSIFICATION, max_length=20, blank=True)
    slot = models.CharField(choices=ITEM_SLOT, max_length=100, blank=True)
    weight = models.CharField(choices=WEIGHT_CHOICES, max_length=255, blank=True)
    unbreakable = models.BooleanField(default=False, blank=False)
    cursed = models.BooleanField(default=False, blank=False)
    standard_resist_range = models.BooleanField(default=True, blank=True)
    block = models.IntegerField(null=True)
    hp_regen = models.IntegerField(null=True)
    sp_regen = models.IntegerField(null=True)
    hp_drain = models.IntegerField(null=True)
    sp_drain = models.IntegerField(null=True)
    ftouchable = models.BooleanField(default=False, blank=False)
    transmutable = models.BooleanField(default=False, blank=False)
    duplicable = models.BooleanField(default=False, blank=False)
    bind_on_pickup = models.BooleanField(default=False, blank=False)
    bind_on_equip = models.BooleanField(default=False, blank=False)
    legendary = models.BooleanField(default=False, blank=False)
    stats_str = models.IntegerField(null=True)
    stats_con = models.IntegerField(null=True)
    stats_int = models.IntegerField(null=True)
    stats_wis = models.IntegerField(null=True)
    stats_dex = models.IntegerField(null=True)
    stats_cha = models.IntegerField(null=True)
    smd = models.BooleanField(default=False, blank=False)
    specials = models.TextField(blank=True)
    edged = models.IntegerField(null=True)
    blunt = models.IntegerField(null=True)
    fire = models.IntegerField(null=True)
    ice = models.IntegerField(null=True)
    acid = models.IntegerField(null=True)
    electricity = models.IntegerField(null=True)
    mind = models.IntegerField(null=True)
    energy = models.IntegerField(null=True)
    poison = models.IntegerField(null=True)
    radiation = models.IntegerField(null=True)

    def __str__(self):
        return self.short

class Crafting_Component(models.Model):
    component_name = models.CharField(choices=COMPONENT_CHOICES, max_length=100, blank=False)
    min_level = models.IntegerField(null=False)
    max_level = models.IntegerField(null=False)

    def __str__(self) -> str:
        return '%a' % (self.component_name)
    
class Crafting_Satchel(models.Model):
    character = models.CharField(max_length=255, blank=False)
    component = models.ForeignKey(Crafting_Component, related_name = 'satchel_components', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(null=True)
    component_quality = models.CharField(choices=COMPONENT_QUALITY_CHOICES, max_length=50, blank=False)

    def __str__(self) -> str:
        return '%a (Qty: %a)' % (self.component.component_name, self.quantity)

class Eternal_Powers(models.Model):
    character = models.CharField(max_length=255, blank=False)
    hmheal = models.BooleanField(default=False)
    destroy = models.BooleanField(default=False)
    divine_insight = models.BooleanField(default=False)
    duplicate_creature = models.BooleanField(default=False)
    duplicate_item = models.BooleanField(default=False)
    embiggen = models.BooleanField(default=False)
    energy_well = models.BooleanField(default=False)
    enlarge = models.BooleanField(default=False)
    farsight = models.BooleanField(default=False)
    fry = models.BooleanField(default=False)
    hasten = models.BooleanField(default=False)
    heal = models.BooleanField(default=False)
    heightened_awareness = models.BooleanField(default=False)
    immortality = models.BooleanField(default=False)
    pick_pocket = models.BooleanField(default=False)
    protection = models.BooleanField(default=False)
    quicken = models.BooleanField(default=False)
    redact = models.BooleanField(default=False)
    refresh_area = models.BooleanField(default=False)
    refresh_item = models.BooleanField(default=False)
    reset_dungeon = models.BooleanField(default=False)
    resurrect = models.BooleanField(default=False)
    shred = models.BooleanField(default=False)
    summon = models.BooleanField(default=False)
    teleport = models.BooleanField(default=False)
    unload_room = models.BooleanField(default=False)
    reload_item = models.BooleanField(default=False)
    cooldown_hmheal = models.DateTimeField(blank=True, null=True)
    cooldown_destroy = models.DateTimeField(blank=True, null=True)
    cooldown_divine_insight = models.DateTimeField(blank=True, null=True)
    cooldown_duplicate_creature = models.DateTimeField(blank=True, null=True)
    cooldown_duplicate_item = models.DateTimeField(blank=True, null=True)
    cooldown_embiggen = models.DateTimeField(blank=True, null=True)
    cooldown_energy_well = models.DateTimeField(blank=True, null=True)
    cooldown_enlarge = models.DateTimeField(blank=True, null=True)
    cooldown_farsight = models.DateTimeField(blank=True, null=True)
    cooldown_fry = models.DateTimeField(blank=True, null=True)
    cooldown_hasten = models.DateTimeField(blank=True, null=True)
    cooldown_heal = models.DateTimeField(blank=True, null=True)
    cooldown_heightened_awareness = models.DateTimeField(blank=True, null=True)
    cooldown_immortality = models.DateTimeField(blank=True, null=True)
    cooldown_pick_pocket = models.DateTimeField(blank=True, null=True)
    cooldown_protection = models.DateTimeField(blank=True, null=True)
    cooldown_quicken = models.DateTimeField(blank=True, null=True)
    cooldown_redact = models.DateTimeField(blank=True, null=True)
    cooldown_refresh_area = models.DateTimeField(blank=True, null=True)
    cooldown_refresh_item = models.DateTimeField(blank=True, null=True)
    cooldown_reset_dungeon = models.DateTimeField(blank=True, null=True)
    cooldown_resurrect = models.DateTimeField(blank=True, null=True)
    cooldown_shred = models.DateTimeField(blank=True, null=True)
    cooldown_summon = models.DateTimeField(blank=True, null=True)
    cooldown_teleport = models.DateTimeField(blank=True, null=True)
    cooldown_unload_room = models.DateTimeField(blank=True, null=True)
    cooldown_reload_item = models.DateTimeField(blank=True, null=True)    

    def __str__(self):
        return self.character