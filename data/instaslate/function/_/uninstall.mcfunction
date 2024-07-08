#####################################################################
# _/uninstall.mcfunction
# written by Eroxen
#
# Removes the datapack and all associated scoreboards & storage.
#####################################################################

item modify entity @a[predicate=instaslate:boost_valid] weapon.mainhand instaslate:reset_tool

data remove storage instaslate:calc internal

function instaslate:signature
function eroxified2:core/api/disable_signature

datapack disable "file/instaslate"

tellraw @a {"text":"[InstaSlate] Uninstalled datapack. If you renamed the datapack file, make sure to disable it manually using /datapack disable.","color":"gold"}