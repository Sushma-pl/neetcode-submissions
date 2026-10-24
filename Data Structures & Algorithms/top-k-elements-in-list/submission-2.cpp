class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp ;
        
        for(int i: nums)
        {
            mp[i]++;
        }

        //using bucket sort for unbounded array numbers
        //using frequency for buckets
        vector<vector<int>> bucket(nums.size()+1);
        for(const auto &it : mp)
        {
            bucket[it.second].push_back(it.first);
        }

        vector<int> ans ;
        for(int i = bucket.size()-1; i>= 0; i--)
        {
            for(int j : bucket[i])
            {
                ans.push_back(j);
                if(ans.size()==k) return ans ;
            }
        }

        return ans;
    }
};
