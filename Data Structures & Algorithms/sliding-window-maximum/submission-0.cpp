class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        int i = 0, j = 0;
        int n = nums.size();
        priority_queue<pair<int,int>> pq ;
        
        //sliding window question
        while(j < n)
        {
            //calculation
            pq.push({nums[j], j});

            if(j-i+1 == k)
            {
                while(!pq.empty() && pq.top().second < i)
                {
                    pq.pop();
                }

                ans.push_back(pq.top().first);
                //slide the window
                i++;
                j++;
            }
            else if(j-i+1 < k)
            {
                j++;
            }

            
        }

        return ans ;
    }
};
