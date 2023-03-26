import unittest
import NQueen
class TestNQueen(unittest.TestCase):
    def test_verify(self):
        
        #Test case for invalid input
        result=NQueen.verify(5,'b')
        self.assertEqual(result,False)
        
        #Test case for invalid position
        result=NQueen.verify(5,'c6')
        self.assertEqual(result,False)
        
        #Test case for valid input
        result=NQueen.verify(5,'d1')
        self.assertEqual(result,True)
    
    def test_solve(self):
        def check(N,r,c):
            board=[["." for i in range(N)] for j in range(N)]
            board[r][c]="Q"
            col,pos_diagonal,neg_diagonal=set(),set(),set()
            col.add(c)
            pos_diagonal.add(r)
            neg_diagonal.add(c)
            return NQueen.solve(N,0,board,col,pos_diagonal,neg_diagonal,r)

        #Test case for 8x8 with solution
        self.assertTrue(check(8,0,0))

        #Test case for 4x4 without solution
        self.assertFalse(check(4,0,0))

if __name__=='__main__':
    unittest.main()