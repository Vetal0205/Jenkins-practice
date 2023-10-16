import unittest
from notebook import Note, Notebook
import logging

# Налаштування логування
logging.basicConfig(filename='notebook_tests.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
class TestNote(unittest.TestCase):
    def test_str_representation(self):
        note = Note("Test note")
        self.assertEqual(str(note), "Test note")

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()

    def test_add_note(self):
        self.notebook.add_note("First note")
        self.assertEqual(len(self.notebook.notes), 1)
        self.assertEqual(str(self.notebook.notes[0]), "First note")

    def test_remove_note(self):
        self.notebook.add_note("First note")
        self.notebook.add_note("Second note")
        
        removed_note = self.notebook.remove_note(0)
        self.assertEqual(str(removed_note), "First note")
        self.assertEqual(len(self.notebook.notes), 1)
        
        non_existent_note = self.notebook.remove_note(10)
        self.assertIsNone(non_existent_note)

    def test_get_notes(self):
        self.notebook.add_note("First note")
        self.notebook.add_note("Second note")
        
        notes = self.notebook.get_notes()
        self.assertEqual(notes, ["First note", "Second note"])

    def test_size(self):
        self.assertEqual(self.notebook.size(), 0)
        self.notebook.add_note("First note")
        self.assertEqual(self.notebook.size(), 1)
        self.notebook.add_note("Second note")
        self.assertEqual(self.notebook.size(), 2)
        self.notebook.remove_note(0)
        self.assertEqual(self.notebook.size(), 1)
    def tearDown(self):
        if hasattr(self, '_outcome'):
            result = self._outcome.result
        if result:
            all_problems = result.errors + result.failures
            for test, problem in all_problems:
                if problem and test._testMethodName == self._testMethodName:
                    trace = problem.split('\n')
                    # Знаходимо рядок і файл, де сталася помилка
                    location = [line for line in trace if "test_note_book.py" in line]
                    if location:
                        # Шукаємо рядок з AssertionError або іншою помилкою
                        error_line = [line for line in trace if "AssertionError" in line]
                        if error_line:
                            logger.error(f"{location[0]} - {error_line[0]}")
                        else:
                            logger.error(f"{location[0]}")
if __name__ == "__main__":
    unittest.main()
