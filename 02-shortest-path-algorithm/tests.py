import unittest
from io import StringIO
from unittest.mock import patch


from shortest_path_algorithm import shortest_path

# graphs:
graph_01 = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

graph_02 = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


class Tests(unittest.TestCase):
    
    def test_paths_graph_01_a_to_c(self):
        """
        check paths "C" is Equal to ["A","B","C"]
        paths["C"] == A -> B -> C 
        """
        _,paths = shortest_path(graph_01, "A")
        path_expected = ["A","B", "C"]
        self.assertEqual(paths["C"], path_expected)


    def test_paths_graph_01_d_to_b(self):
        """
        check paths "B" is Equal to ["D","A","B"]
        paths["B"] == D -> A -> B 
        """
        _,paths = shortest_path(graph_01, "D")
        path_expected = ["D","A","B"]
        self.assertEqual(paths["B"], path_expected)


    def test_paths_graph_01_c_to_b(self):
        """
        check paths "B" is Equal to ["C","B"]
        paths["B"] == C -> B 
        """
        _,paths = shortest_path(graph_01, "C")
        path_expected = ["C","B"]
        self.assertEqual(paths["B"], path_expected)


    def test_paths_graph_02_f_to_e(self):
        """
        check paths "E" is Equal to "F","B", "C", "E"]
        """
        _,paths = shortest_path(graph_02, "F", "E")
        path_expected = ["F","B", "C", "E"]
        self.assertEqual(paths["E"], path_expected)


    def test_distance_graph_01_a_to_d(self):
        """
        check distances "A" to "D" is Equal to 1
        """
        distances, _ = shortest_path(graph_01, "A", "D")
        distance_expected = 1
        self.assertEqual(distances["D"], distance_expected)


    def test_distance_graph_01_b_to_d(self):
        """
        check distances "B" to "D" is Equal to 4
        """
        distances, _ = shortest_path(graph_01, "B")
        distance_expected = 4
        self.assertEqual(distances["D"], distance_expected)


    def test_distances_graph_02_a_to_c(self):
        """
        check distances "A" to "C" is Equal to 3
        """
        distances, _ = shortest_path(graph_02, "A", "C")
        distance_expected = 3
        self.assertEqual(distances["C"], distance_expected)

 
    def test_distances_graph_02_a_to_f(self):
        """
        check distances "A" to "F" is Equal to 7
        """
        distances, _ = shortest_path(graph_02, "A")
        distance_expected = 6
        self.assertEqual(distances["F"], distance_expected)


    def test_distances_graph_02_c_to_f(self):
        """
        check distances "C" to "F" is Equal to 7
        """
        distances, _ = shortest_path(graph_02, "C")
        distance_expected = 3
        self.assertEqual(distances["F"], distance_expected)


    def test_distances_and_path_graph_01_b_to_d(self):
        """
        check paths "B" to "D" is Equal to ["B","A","D"]
        check distances "B" to "D" is Equal to 4
        """
        distances, paths= shortest_path(graph_01, "B")
        
        path_expected = ["B","A","D"]
        distance_expected = 4
        
        self.assertEqual(paths["D"], path_expected)
        self.assertEqual(distances["D"], distance_expected)


    def test_distances_and_path_graph_01_c_to_a(self):
        """
        check paths "C" to "A" is Equal to ["B","A","D"]
        check distances "C" to "A" is Equal to 4
        """
        distances, paths= shortest_path(graph_01, "C", "A")
        
        path_expected = ["C","B","A"]
        distance_expected = 7
        
        self.assertEqual(paths["A"], path_expected)
        self.assertEqual(distances["A"], distance_expected)


    def test_distances_and_path_graph_02_e_to_f(self):
        """
        check paths "E" to "F" is Equal to ["E","C","B","F"]
        check distances "E" to "F" is Equal to 8
        """
        distances, paths= shortest_path(graph_02, "E", "F")
        
        path_expected = ["E","C", "B","F"]
        distance_expected = 8
        
        self.assertEqual(paths["F"], path_expected)
        self.assertEqual(distances["F"], distance_expected)


    def test_distances_and_path_graph_02_b_to_d(self):
        """
        check paths "B" to "D" is Equal to ["B","C", "D"]
        check distances "B" to "D" is Equal to 2
        """
        distances, paths= shortest_path(graph_02, "B")
        
        path_expected = ["B","C", "D"]
        distance_expected = 2
        
        self.assertEqual(paths["D"], path_expected)
        self.assertEqual(distances["D"], distance_expected)


    @patch('sys.stdout', new_callable=StringIO)
    def test_message_graph_01_a_to_d(self, mock_stdout):
        """
        Verify that the printed output for the shortest path from "A" to "D" is:
        A-C distance: 1
        Path: A -> D
        """
        # function
        shortest_path(graph_01, "A", 'D')
        
        expected_output = '\nA-D distance: 1\nPath: A -> D\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_message_graph_01_a_to_c(self, mock_stdout):
        """
        Verify that the printed output for the shortest path from "A" to "C" is:
        A-C distance: 7
        Path: A -> B -> C
        """
        # function
        shortest_path(graph_01, "A", 'C')
        
        expected_output = '\nA-C distance: 7\nPath: A -> B -> C\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_message_graph_02_d_to_a(self, mock_stdout):
        """
        Verify that the printed output for the shortest path from "D" to "A" is:
        A-C distance: 4
        Path: D -> C -> A
        """
        # function
        shortest_path(graph_02, "D", 'A')
        
        expected_output = '\nD-A distance: 4\nPath: D -> C -> A\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_message_graph_02_f_to_e(self, mock_stdout):
        """
        Verify that the printed output for the shortest path from "D" to "A" is:
        A-C distance: 8
        Path: F -> B -> C -> E
        """
        # function
        shortest_path(graph_02, "F", 'E')
        
        expected_output = '\nF-E distance: 8\nPath: F -> B -> C -> E\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_paths_different_graph_format(self, mock_stdout):      
        """
        check paths "A" to "X" is Equal to ["A","X"],
        check distances "A" to "X" is Equal to 4,
        Verify that the printed output for the shortest path from "A" to "X" is:
            A-C distance: 4
            Path: A -> X
        """
        graph_03 = {
            'A':  [('X', 4)],
            'X': [('Y', 2), ('Z', 3), ('A', 4)],
        }
        
        # function
        distances ,paths = shortest_path(graph_03, "A", 'X')
        
        # Expected outputs
        path_expected = ["A","X"]
        distance_expected = 4
        expected_print_output = '\nA-X distance: 4\nPath: A -> X\n'
        
        # Verify expected results
        self.assertEqual(paths["X"], path_expected)
        self.assertEqual(distances["X"], distance_expected)
        self.assertEqual(mock_stdout.getvalue(), expected_print_output)        


if __name__ == "__main__":
    unittest.main()