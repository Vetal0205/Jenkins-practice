from collections import deque

class Note:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Notebook:
    def __init__(self):
        self.notes = deque()

    def add_note(self, text):
        note = Note(text)
        self.notes.append(note)

    def remove_note(self, index):
        if 0 <= index < len(self.notes):
            self.notes.rotate(-index)
            removed = self.notes.popleft()
            self.notes.rotate(index)
            return removed
        return None


    def get_notes(self):
        return [str(note) for note in self.notes]

    def size(self):
        return len(self.notes)



class Menu:
    def __init__(self):
        self.notebook = Notebook()

    def start(self):
        while True:
            choice = self.show_menu()
            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.show_notes()
            elif choice == "3":
                self.remove_note()
            elif choice == "4":
                break

    def show_menu(self):
        print("\nNotebook Menu:")
        print("1. Add Note")
        print("2. Show Notes")
        print("3. Remove Note by Index")
        print("4. Exit")
        return input("> ")

    def add_note(self):
        text = input("Enter note text: ")
        self.notebook.add_note(text)
        print("Note added successfully!")

    def show_notes(self):
        notes = self.notebook.get_notes()
        for i, note in enumerate(notes):
            print(f"[{i}] {note}")

    def remove_note(self):
        index = int(input("Enter note index to remove: "))
        if 0 <= index < self.notebook.size():
            self.notebook.remove_note(index)
            print("Note removed successfully!")
        else:
            print("Invalid index!")

if __name__ == "__main__":
    menu = Menu()
    menu.start()
