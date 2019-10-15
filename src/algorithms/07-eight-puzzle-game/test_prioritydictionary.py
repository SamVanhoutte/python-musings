from priority_queue import PriorityQ
import unittest   
import puzzle as pz
import numpy as np


class TestObject:
    stringvalue = ''
    def __init__(self, stringval):
        self.stringvalue = stringval

class TestMethods(unittest.TestCase):
    def test_queue_sequence_objects(self):
        q = PriorityQ()
        q.put(2, TestObject('two'))
        q.put(1, TestObject('one'))
        seq, value = q.peek()
        self.assertEqual(value[1].stringvalue, 'one')
        q.complete(seq)
        self.assertEqual(1, q.get_depth())
        seq, value = q.receive_delete()
        self.assertEqual(value[1].stringvalue, 'two')
        self.assertEqual(0, q.get_depth())
        self.assertIsNone(q.peek())

    def test_queue_sequence(self):
        q = PriorityQ()
        q.put(2, 'two')
        q.put(1, 'one')
        seq, value = q.peek()
        self.assertEqual(value[1], 'one')
        q.complete(seq)
        self.assertEqual(1, q.get_depth())
        seq, value = q.receive_delete()
        self.assertEqual(value[1], 'two')
        self.assertEqual(0, q.get_depth())
        self.assertIsNone(q.peek())
