# invEngine
A python compiler module for a mini language that allows you to create Minecraft mini games within the player's inventory with a SINGLE command

*Temporary wiki*
# Basic syntax
Item names are written as regular item IDs without the `minecraft:`.
# Current version
## Commands
### Done
- `setItem(slot,item)` -  Sets the corresponding slot to the specified item
    Slot syntax: Number (1-9) for column followed by letter (A-D) for line (e.g. 2C)
### To-Do
- `defaultItem = <item>` - Sets the item to use for empty slots
- `if` support
- tick repetition support
## Current limitations
> I don't wanna learn about ASTs, so deal with it I guess /j
- `defaultItem` must be used exaclty once. 
- Item components aren't supported
- Everything must be set as a string, as dynamic parsing isn't supported.
# Plans
- Variable support
- Object definition
- Movement system
- Components support