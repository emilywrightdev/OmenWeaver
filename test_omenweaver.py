# test_omenweaver.py
"""
Tests for OmenWeaver module.
"""

import unittest
from omenweaver import OmenWeaver

class TestOmenWeaver(unittest.TestCase):
    """Test cases for OmenWeaver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmenWeaver()
        self.assertIsInstance(instance, OmenWeaver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmenWeaver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
