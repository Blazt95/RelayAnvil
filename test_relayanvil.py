# test_relayanvil.py
"""
Tests for RelayAnvil module.
"""

import unittest
from relayanvil import RelayAnvil

class TestRelayAnvil(unittest.TestCase):
    """Test cases for RelayAnvil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RelayAnvil()
        self.assertIsInstance(instance, RelayAnvil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RelayAnvil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
