import unittest
import shutil
import tempfile
from io import StringIO
import sys
import os

TEST_DIR = os.path.dirname(__file__)
MODULE_DIR = os.path.join(TEST_DIR, '..', 'src')
sys.path.append(MODULE_DIR)

from tree import print_tree



class TestPrintTree(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

        os.makedirs(os.path.join(self.test_dir, "subdir1"))
        os.makedirs(os.path.join(self.test_dir, "subdir2"))
        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("This is file1.txt")
        with open(os.path.join(self.test_dir, "subdir1", "file2.txt"), "w") as f:
            f.write("This is file2.txt")
        os.symlink(os.path.join(self.test_dir, "file1.txt"), os.path.join(self.test_dir, "symlink1"))

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_print_tree(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_tree(self.test_dir, show_symlinks=True, show_hidden=True)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("test_dir", output)
        self.assertIn("|   +---subdir1", output)
        self.assertIn("|   |   +---file2.txt", output)
        self.assertIn("|   +---subdir2", output)
        self.assertIn("|   +---file1.txt", output)
        self.assertIn("|   +---symlink1", output)

    def test_print_tree_hidden(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print_tree(self.test_dir, show_hidden=True)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn(".hidden_file", output)
        self.assertIn(".hidden_dir", output)

if __name__ == '__main__':
    unittest.main()
