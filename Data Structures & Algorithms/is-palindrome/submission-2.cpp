class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.length()-1 ;
        
        while(i <= j)
        {
            if(!iswalnum(s[i]) || s[i] == ' ')
            {
                i++;
            }
            else if(!iswalnum(s[j]) || s[i] == ' ')
            {
                j--;
            }
            else if(tolower(s[i]) == tolower(s[j]))
            {
                i++;
                j--;
            }
            else if(s[i] != s[j])
            {
                return false;
            }   
            
        }

        return true;
    }
};
