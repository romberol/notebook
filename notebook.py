"""
This module can be used to create notes, change them and navigate through notebook
"""
from datetime import datetime

class Note():
    """
    Note class
    """
    def __init__(self, memo, creation_date, tags):
        self.memo = memo
        self.creation_date = creation_date
        self.tags = tags
    
    def match(self, search_filter):
        """
        Check, if note has tag(search_filter)
        """
        return search_filter in self.tags

class Notebook():
    """
    Notebook class
    """
    def __init__(self):
        self.notes = list()

    def new_note(self, memo, creation_date, tags):
        """
        Creates new note and add it to list of notes.
        Memo - content of this note.
        Tags - list of tags.
        """
        note = Note(memo, creation_date, tags)
        self.notes.append(note)
    
    def search(self, filters):
        """
        Returns list of notes, which have tags(filters)
        """
        appropriate_notes = []
        for tag in filters:
            for note in self.notes:
                if note.match(tag) and note not in appropriate_notes:
                    appropriate_notes.append(note)
        return appropriate_notes
    
    def modify_memo(self, note_id, new_memo):
        """
        Modify note's memo, search note by note_id(creation_date)
        """
        for note in self.notes:
            if note.creation_date == note_id:
                note.memo = new_memo
    
    def modify_tags(self, note_id, new_tags):
        """
        Modify note's tags, search note by note_id(creation_date)
        """
        for note in self.notes:
            if note.creation_date == note_id:
                note.tags = new_tags

class CommandOption():

    def create_notebook(self):
        """
        Return memo, creation time, tags to create a note
        """
        print("\nType memo, please:")
        memo = input(">>> ")
        print("Type tags for your notes, please")
        tags = input("Separate them using space: ").split(" ")
        return memo, str(datetime.now()), tags

    def search(self):
        """
        Returns list of tags to find notes
        """
        print("\nType tags, by which you whant to find notes.")
        tags = input("Separate them using space: ").split(" ")
        return tags
    
    def read_note(self, note):
        """
        Return content of note
        """
        print("\nYour note's content:")
        return note.memo

    def get_new_memo(self):
        """
        Returns new memo to change note
        """
        print("\nType new memo for your note.")
        new_memo = input(">>> ")
        return new_memo
    
    def get_new_tags(self):
        """
        Returns new tags to change note
        """
        print("\nType new tags for your note.")
        new_tags = input("Separate them using space: ").split(" ")
        return new_tags
    

class Menu():
    def __init__(self):
        self.notebook = Notebook()
        self.comands = CommandOption()

    def next_action(self, action):
        """
        Provide functions to create, read or change notes.
        """
        if action == "create":
            memo, cr_date, tags = self.comands.create_notebook()
            self.notebook.new_note(memo, cr_date, tags)
            self.n_notes()
        if action == "find":
            print("Available tags:")
            av_tags = set()
            for note in self.notebook.notes:
                for tag in note.tags:
                    if tag not in av_tags: print(tag); av_tags.add(tag)
            tags = self.comands.search()
            available_notes = self.notebook.search(tags)
            if not available_notes: print("Nothing found"); self.n_notes()
            print("\nAvailable notes:")
            for i, note in enumerate(available_notes):
                print(i, "->", note.creation_date)
            print("\nIf you want to read note, type: read <number>}")
            print("If you want to change memo of note, type: memo <number>")
            print("If you want to change tags of note, type: tags <number>")
            try: action, numb = input(">>> ").split()
            except: print("Your input is unclear."); self.next_action(action)
            numb = int(numb)
            if action == "read":
                print(self.comands.read_note(available_notes[numb]))
                self.n_notes()
            if action == "memo":
                new_memo = self.comands.get_new_memo()
                self.notebook.modify_memo(available_notes[numb].creation_date, new_memo)
                self.n_notes()
            if action == "tags":
                new_tags = self.comands.get_new_tags()
                self.notebook.modify_tags(available_notes[numb].creation_date, new_tags)
                self.n_notes()
            else:
                print("Your input is unclear")
                self.n_notes()
            

    def n_notes(self):
        """
        Start function.
        Give user number of created notes and 
        provide funсtions to create, read or change note.
        """
        print(f"\nYou have {len(self.notebook.notes)} note(s).")
        print("To create new note, type: create")
        if len(self.notebook.notes)>0:
            print("To find and read or change your note type: find")
        print("To exit, type: exit")
        action = input(">>> ")
        if action not in ["create", "find", "exit"]: print("\nYour input is unclear!"); self.n_notes()
        if action == "exit": quit()
        return self.next_action(action)

if __name__=="__main__":
    menu = Menu()
    menu.n_notes()
