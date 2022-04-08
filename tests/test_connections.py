from unittest import TestCase, main
import sys
import os

sys.path.append(os.path.abspath('run_module'))

from review_model import *


class ConnectionTest(TestCase):
    def test_connections(self):
        comport.check_connections()
        self.assertFalse(comport.active_names)


if __name__ == '__main__':
    main()