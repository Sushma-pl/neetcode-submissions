class Solution {
public:
    bool isPalindrome(string str) {
        string s ;
        for(char ch : str)
        {
            if(ch != ' ' && iswalnum(ch))
            {
                s.push_back(tolower(ch));
            }
        }

        
        
        int i = 0, j = s.length()-1 ;
        cout << s << endl ;
        while(i <= j)
        {
            if(s[i] != s[j])
            {
                return false;
            }   
            i++;
            j--;
        }

        return true;
    }
};
