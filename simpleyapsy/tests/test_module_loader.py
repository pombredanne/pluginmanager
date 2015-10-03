import unittest
from simpleyapsy.module_loader import ModuleLoader


class TestClass:
    pass


class TestModuleLoader(unittest.TestCase):
    def setUp(self):
        self.module_loader = ModuleLoader()

    def test_set_module_parsers(self):
        test_obj = TestClass()
        previous_module = self.module_loader.module_parsers[0]
        self.module_loader.set_module_parsers(test_obj)
        self.assertIn(test_obj, self.module_loader.module_parsers)
        self.assertNotIn(previous_module, self.module_loader.module_parsers)

    def test_add_module_parser(self):
        test_obj = TestClass()
        self.module_loader.add_module_parsers(test_obj)
        self.assertIn(test_obj, self.module_loader.module_parsers)

    def test_blacklist_filepaths(self):
        test_filepath = 'fancy/dir'
        self.module_loader.blacklist_filepaths(test_filepath)
        test_filepaths = ['dir/d', 'dir/b']
        self.module_loader.blacklist_filepaths(test_filepaths)
        self.assertIn(test_filepath, self.module_loader.blacklisted_filepaths)
        self.assertIn(test_filepaths[0], self.module_loader.blacklisted_filepaths)

    def test_set_blacklist_filepaths(self):
        removed_dir = 'test/dir'
        self.module_loader.blacklist_filepaths(removed_dir)
        single_dir = 'dir/b'
        self.module_loader.set_blacklisted_filepaths(single_dir)
        self.assertIn(single_dir, self.module_loader.blacklisted_filepaths)
        mulitple_dirs = ['dir/a', 'dir/b']
        self.module_loader.set_blacklisted_filepaths(mulitple_dirs)
        self.assertIn(mulitple_dirs[0], self.module_loader.blacklisted_filepaths)
        
