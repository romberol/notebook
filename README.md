# Notebook
This module can be used to create notes, change them and navigate through notebook.
## Example of user interface
```
>python notebook.py

You have 0 note(s).
To create new note, type: create
To exit, type: exit
>>> create

Type memo, please:
>>> Glory to Ukraine!
Type tags for your notes, please
Separate them using space: war peace

You have 1 note(s).
To create new note, type: create
To find and read or change your note type: find
To exit, type: exit
>>> create

Type memo, please:
>>> Glory to heroes!
Type tags for your notes, please
Separate them using space: peace

You have 2 note(s).
To create new note, type: create
To find and read or change your note type: find
To exit, type: exit
>>> find
Available tags:
war
peace

Type tags, by which you whant to find notes.
Separate them using space: peace

Available notes:
0 -> 2022-02-24 15:42:56.373173
1 -> 2022-02-24 15:43:18.000901

If you want to read note, type: read <number>}
If you want to change memo of note, type: memo <number>
If you want to change tags of note, type: tags <number>
>>> read 0

Your note's content:
Glory to Ukraine!

You have 2 note(s).
To create new note, type: create
To find and read or change your note type: find
To exit, type: exit
>>> exit
```
