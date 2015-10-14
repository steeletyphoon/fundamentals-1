# Bonus MadForms

This version allows many madforms to be written and placed in the
`madforms.d` directory where they are either randomly selected or
specifically selected by a command-line argument. This version adds
a `-l` as well to list all the available madforms to pick from. If
`search_system` is set this version will look in every user home directory
for a readable `madforms.d` directory or `repos/madforms.d` directory or
`repos/python-1/madforms.d` directory. If found the `.form` files there
will be added to the available list of madforms. This version also adds
a prompt to save the filled form as a file that can be emailed, etc.

