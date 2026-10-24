class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long prod = 1 ;
        int count =  0;
        for(int i : nums)
        {
            if(i != 0)
            {
                prod *= i;
            }
            else 
            {
                count++;
            }
        }

        vector<int> res ;
        for(int i : nums)
        {
            if(i == 0 && count == 1)
                res.push_back(prod);
            else if(count >= 1)
            {
                res.push_back(0);
            }
            else if(count < 1)
            {
                res.push_back(prod/i);
            }
        }

        return res;
    }
};
