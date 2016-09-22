#__author__ = 'jhondev'
import os
import unittest

def analyze_text(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

class TextAnalysisTests(unittest.TestCase):
    
    #setUp it executes before testing starts
    def setUp(self):
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as file:
            file.write('Now we are engagd in \n\r'
                       'testing whether that nation')
    
    #tearDown it executes after testing
    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    #create methods with test word
    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename), 2)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()