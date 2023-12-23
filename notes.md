Eternal Powers API
List and Create Eternal Powers

    URL: https://www.3kpi.icu/api/eternal_powers/
    HTTP Methods: GET, POST

Example GET Request: 
curl -X GET https://www.3kpi.icu/api/eternal_powers/

Example POST Request:
curl -X POST https://www.3kpi.icu/api/eternal_powers/ -H "Content-Type: application/json" -d '{
    "character": "Player123",
    "hmheal": true,
    "destroy": false,
    "divine_insight": true,
    "duplicate_creature": false,
    "duplicate_item": true,
    "embiggen": false,
    "energy_well": true,
    "enlarge": false,
    "farsight": true,
    "fry": false,
    "hasten": true,
    "heal": false,
    "heightened_awareness": true,
    "immortality": false,
    "pick_pocket": true,
    "protection": false,
    "quicken": true,
    "redact": false,
    "refresh_area": true,
    "refresh_item": false,
    "reset_dungeon": true,
    "resurrect": false,
    "shred": true,
    "summon": false,
    "teleport": true,
    "unload_room": false,
    "reload_item": true,
    "cooldown_hmheal": "2023-08-22T12:00:00Z",
    "cooldown_destroy": "2023-08-22T12:00:00Z",
    "cooldown_divine_insight": "2023-08-22T12:00:00Z",
    "cooldown_duplicate_creature": "2023-08-22T12:00:00Z",
    "cooldown_duplicate_item": "2023-08-22T12:00:00Z",
    "cooldown_embiggen": "2023-08-22T12:00:00Z",
    "cooldown_energy_well": "2023-08-22T12:00:00Z",
    "cooldown_enlarge": "2023-08-22T12:00:00Z",
    "cooldown_farsight": "2023-08-22T12:00:00Z",
    "cooldown_fry": "2023-08-22T12:00:00Z",
    "cooldown_hasten": "2023-08-22T12:00:00Z",
    "cooldown_heal": "2023-08-22T12:00:00Z",
    "cooldown_heightened_awareness": "2023-08-22T12:00:00Z",
    "cooldown_immortality": "2023-08-22T12:00:00Z",
    "cooldown_pick_pocket": "2023-08-22T12:00:00Z",
    "cooldown_protection": "2023-08-22T12:00:00Z",
    "cooldown_quicken": "2023-08-22T12:00:00Z",
    "cooldown_redact": "2023-08-22T12:00:00Z",
    "cooldown_refresh_area": "2023-08-22T12:00:00Z",
    "cooldown_refresh_item": "2023-08-22T12:00:00Z",
    "cooldown_reset_dungeon": "2023-08-22T12:00:00Z",
    "cooldown_resurrect": "2023-08-22T12:00:00Z",
    "cooldown_shred": "2023-08-22T12:00:00Z",
    "cooldown_summon": "2023-08-22T12:00:00Z",
    "cooldown_teleport": "2023-08-22T12:00:00Z",
    "cooldown_unload_room": "2023-08-22T12:00:00Z",
    "cooldown_reload_item": "2023-08-22T12:00:00Z"
}'


Area API
List and Create Areas
    URL: https://www.3kpi.icu/api/area/
    HTTP Methods: GET, POST

Example GET Request:
curl -X GET https://www.3kpi.icu/api/area/

GET /area/:id/
Retrieves details of a specific area.
Replace :id with the actual ID of the area.

curl https://www.3kpi.icu/api/area/:id/


Example POST Request:
curl -X POST https://www.3kpi.icu/api/area/ -H "Content-Type: application/json" -d '{
    "name": "Mystic Forest",
    "realm": "Fantasy",
    "dungeon": false
}'


PUT /area/:id/
Request:
curl -X PUT -H "Content-Type: application/json" -d '{"name": "New Name"}' https://www.3kpi.icu/api/area/:id/



Item API
List and Create Items
    URL: https://www.3kpi.icu/api/item/
    HTTP Methods: GET, POST

Example GET Request:
curl -X GET https://www.3kpi.icu/api/item/

GET /item/:id/
Retrieves details of a specific item.  Replace :id with the actual ID of the item.
curl https://www.3kpi.icu/api/item/:id/

PUT /item/:id/
Updates details of a specific item.  Replace :id with the actual ID of the item.
curl -X PUT -H "Content-Type: application/json" -d '{"short": "New Short Name"}' https://www.3kpi.icu/api/item/:id/

Example POST Request:
curl -X POST https://www.3kpi.icu/api/item/ -H "Content-Type: application/json" -d '{
    "parent_monster": null,
    "parent_area": null,
    "short": "Sword of Fire",
    "description": "A blazing sword forged in the heart of a volcano.",
    "slot": "Weapon",
    "weight": "It looks heavy.",
    "unbreakable": true,
    "cursed": false,
    "hp_regen": 5,
    "sp_regen": 3,
    "hp_drain": 2,
    "sp_drain": 1,
    "ftouchable": false,
    "transmutable": true,
    "duplicable": false,
    "bind_on_pickup": true,
    "bind_on_equip": false,
    "stats_str": 10,
    "stats_con": 8,
    "stats_int": 4,
    "stats_wis": 6,
    "stats_dex": 7,
    "stats_cha": 5,
    "smd": true,
    "specials": "Deals additional fire damage on hit.",
    "edged": 20,
    "blunt": 5,
    "fire": 30,
    "ice": 10,
    "acid": 5,
    "electricity": 15,
    "mind": 5,
    "energy": 15,
    "poison": 5,
    "radiation": 0
}'






Monster API
List and Create Monsters

    URL: https://www.3kpi.icu/api/monster/
    HTTP Methods: GET, POST

Example GET Request:
curl -X GET https://www.3kpi.icu/api/monster/

Example POST Request:

shell

curl -X POST https://www.3kpi.icu/api/monster/ -H "Content-Type: application/json" -d '{
    "parent_area": null,
    "short": "Fire Elemental",
    ...
}'

Monster Attack API
List and Create Monster Attacks

    URL: https://www.3kpi.icu/api/monster_attack/
    HTTP Methods: GET, POST

Example GET Request:

shell

curl -X GET https://www.3kpi.icu/api/monster_attack/

Example POST Request:

shell

curl -X POST https://www.3kpi.icu/api/monster_attack/ -H "Content-Type: application/json" -d '{
    "parent_monster": 1,
    "damage_type": "fire",
    "attack_type": "Special"
}'

Updating and Deleting Resources
Update and Delete Specific Resource

    URL: https://www.3kpi.icu/api/resource/{resource_id}/
    HTTP Methods: GET, PATCH, DELETE

Example GET Request:

shell

curl -X GET https://www.3kpi.icu/api/eternal_powers/1/

Example PATCH Request:

shell

curl -X PATCH https://www.3kpi.icu/api/eternal_powers/1/ -H "Content-Type: application/json" -d '{
    "hmheal": false
}'

Example DELETE Request:

shell

curl -X DELETE https://www.3kpi.icu/api/eternal_powers/1/