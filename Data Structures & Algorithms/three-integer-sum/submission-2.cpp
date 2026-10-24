class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // for removing duplicates: we need to sort the array
        sort(nums.begin(), nums.end());
        set<vector<int>> ans;
        
        int k=0;
        int target;

        while(k < nums.size())
        {
            target = -nums[k];
        
            //two sum
            int i = k+1, j = nums.size()-1 ;
            while(i < j)
            {
                if(nums[i]+nums[j] == target)
                {
                    ans.insert({nums[k], nums[i], nums[j]});
                    i++;
                    j--;
                }
                else if(nums[i]+nums[j] < target)
                {
                    i++;
                } 
                else if(nums[i]+nums[j] > target)
                {
                    j--;
                }
            }

            //remove duplicates
            k++;
        }

        return vector<vector<int>>(ans.begin(), ans.end());
    }
};
