class Solution {
public:
    bool checkRow(vector<vector<char>>& board, int row)
    {
        unordered_map<char,int> mp ;
        for(int i = 0;i < 9 ; i++)
        {
            if(board[row][i] != '.' && mp.find(board[row][i]) != mp.end())
            {
                return false;
            }

            mp[board[row][i]]++;
        }

        return true;
    }

    bool checkCol(vector<vector<char>>& board, int col)
    {
        unordered_map<char,int> mp ;
        for(int i = 0;i < 9 ; i++)
        {
            if(board[i][col] != '.' && mp.find(board[i][col]) != mp.end())
            {
                return false;
            }

            mp[board[i][col]]++;
        }

        return true;
    }

    bool check3x3(vector<vector<char>>& board, int row, int col)
    {
        unordered_map<char,int> mp ;
        for(int i = 0;i < 3 ; i++)
        {
            for(int j = 0; j < 3 ; j++)
            {
                if(board[row + i][col + j] != '.' && mp.find(board[row + i][col + j]) != mp.end())
                {
                    return false;
                }

                mp[board[row + i][col + j]]++;
            }
            
        }

        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        //check rows;
        for(int row = 0 ; row < 9 ; row++)
        {
            if(!checkRow(board,row))
            {
                return false;
            }
        }

        //check col;
        for(int col = 0 ; col < 9 ; col++)
        {
            if(!checkCol(board,col))
            {
                return false;
            }
        }

        //chech 3x3
        for(int i = 0; i < 3 ; i++)
        {
            for(int j = 0; j < 3 ; j++)
            {
                if(!check3x3(board,i*3, j*3))
                {
                    return false;
                }
            }
        }

        return true;
    }
};
