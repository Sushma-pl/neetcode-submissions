class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int> mp1 ;
        unordered_map<int,int> mp2 ;
        int ans = 0, count = 1;

        for(int i : nums)
        {
            mp1[i]++;
        }

        //find out starting point
        for(int i : nums)
        {
            if(mp1.find(i-1) == mp1.end())
            {
                mp2[i]++;
            }
        }

        //ans
        for(const auto &it : mp2)
        {
            cout << it.first << endl ;
            int num = it.first;
            while(mp1.find(num + 1) != mp1.end())
            {
                count++;
                num = num+1;
            }

            ans = max(ans, count);
            count = 1;
        }

        return ans;
    }
};
