class Solution {
public:
    int trap(vector<int>& height) {
        // using two pointers
        int maxl = 0 , maxr = 0 ;
        int i = 0, j = height.size()-1 ;
        int ans = 0 ;
        while(i <= j)
        {
            if(maxl <= maxr)
            {
                // ''shift l pointer
                ans += max(0, maxl-height[i]);
                maxl = max(maxl, height[i]);
                i++;
            }
            else
            {
                ans += max(0, maxr-height[j]);
                maxr = max(maxr, height[j]);
                j--;
            }
        }

        return ans;
    }
};
