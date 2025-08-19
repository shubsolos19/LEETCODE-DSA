class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        const int n=nums.size();
        long long sum=0, a_len=0;
        for (int l=0, r=0; l<n; ){
            if (nums[l]!=0){
                l++;
                continue;
            }
            for(r=l; r<n && nums[r]==0; r++);
            a_len=(r-l);
            sum+=(a_len+1LL)*a_len/2;
            l=r;
        }
        return sum;
    }
};