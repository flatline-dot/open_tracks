from unittest import TestCase, main
import sys
import os

sys.path.append(os.path.abspath('run_module'))

from review_model import *


class InintCompotsTest(TestCase):
    def test_init(self):
        comport.init_comports()
        self.assertFalse(comport.active_ports)


if __name__ == '__main__':
    main()