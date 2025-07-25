class Solution {
public:
    int maxSum(vector<int>& nums) {
        bitset<101> seen=0;
        int sum=0, M=-100;
        for(int x: nums){
            M=max(M, x);
            if (x>=0 && !seen[x]){
                sum+=x;
                seen[x]=1;
            }
        }
        return seen==0?M:sum;
    }
};