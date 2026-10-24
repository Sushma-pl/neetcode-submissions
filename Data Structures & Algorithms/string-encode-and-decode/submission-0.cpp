class Solution {
public:

    string encode(vector<string>& strs) {
        string res ="" ;

        for(int i = 0 ;  i < strs.size() ; i++)
        {
            res += to_string(strs[i].length()) + "#" + strs[i];
        }

        return res;
    }

    vector<string> decode(string s) {
        vector<string> res ;
        int i = 0 ;
        while(i < s.length())
        {
            //length could be more than one digit 
            int j = i;
            while(s[j] != '#')
            {
                j++;
            }

            int length = stoi(s.substr(i, j - i));
            string temp = s.substr(j+1, length);
            res.push_back(temp);
            i = j + length + 1;
        }

        return res ;
    }
};
