#####################################################################
# _/uninstall.mcfunction
# written by Eroxen
#
# Removes the datapack and all associated scoreboards & storage.
#####################################################################

item modify entity @a[predicate=instaslate:boost_valid] weapon.mainhand instaslate:reset_tool

data remove storage instaslate:calc internal

tellraw @a {"text":"[InstaSlate] Uninstalled datapack. You can now remove the file or disable it using /datapack disable.","color":"gold"}