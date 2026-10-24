class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        //one solution could be that we take two array prefix and postfix 
        int n = nums.size();
        vector<int> prefix(n,1);
        vector<int> postfix(n,1);

        long prod = 1 ;
        for(int i = 0; i < n-1 ; i++)
        {
            prod *= nums[i];
            prefix[i+1] = prod;
        }

        prod = 1 ;
        for(int j = n-1 ; j > 0 ; j--)
        {
            prod *= nums[j];
            postfix[j-1] = prod ;
        }

        vector<int> ans(n,1);
        for(int i = 0; i < n ; i++)
        {
           ans[i] = prefix[i]*postfix[i];
        }

        return ans;
    }
};
