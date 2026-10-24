class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int> mp1 ;
        int ans = 0, count = 1;

        for(int i : nums)
        {
            mp1[i]++;
        }

        //find out starting point
        for(int i : nums)
        {
            count = 1;
            if(mp1.find(i-1) == mp1.end()) //start point 
            {
                int num = i;
                while(mp1.find(num + 1) != mp1.end())
                {
                    count++;
                    num = num+1;
                }

            }
            ans = max(ans, count);
        }

        
        return ans;
    }
};
