all_slots = ['player.cursor', 'weapon.offhand'] + [f'inventory.{i}' for i in range(27)] + [f'hotbar.{i}' for i in range(9)]

def generate_scan_inventory():
    path = 'data/instaslate/function/pickaxe/api/scan_inventory.mcfunction'
    with open(path, 'a') as file:
        for slot in all_slots:
            command = [
                "execute if items entity @p",
                slot,
                "minecraft:netherite_pickaxe[minecraft:tool={rules:[{blocks:\"#minecraft:incorrect_for_netherite_tool\",correct_for_drops:false},{blocks:\"minecraft:deepslate\",correct_for_drops:true,speed:38.3},{blocks:\"#minecraft:mineable/pickaxe\",correct_for_drops:true,speed:9.0}]}]",
                "run item modify entity @s",
                slot,
                "instaslate:reset_tool"
            ]
            if slot.startswith('hotbar.'):
                i = slot[7:]
                command.insert(3, "unless data storage instaslate:calc internal.pickaxe{selected_slot:" + i + "}")
            file.write(' '.join(command) + '\n')

if __name__ == '__main__':
    generate_scan_inventory()