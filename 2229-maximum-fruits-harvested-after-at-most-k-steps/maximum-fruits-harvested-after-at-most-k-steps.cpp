class Solution {
public:
    int step(int R, int L, int startPos) {// goes left then right but also right then left
        return min(startPos-2*L+R, 2*R-startPos-L);// both should > k
    }
    
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int i0=lower_bound(fruits.begin(), fruits.end(), vector<int>(1,startPos-k))-fruits.begin();
        int iN=upper_bound(fruits.begin()+i0, fruits.end(), vector<int>(1,startPos+k+1))-fruits.begin();

        int ans=0, wsum=0;
        for (int l=i0, r=i0; r<iN; r++) {
            wsum+=fruits[r][1];
            const int R=fruits[r][0];
            while (l<=r && step(R, fruits[l][0], startPos) > k){
                wsum-=fruits[l][1];
                l++;
            }
            ans=max(ans, wsum);
        }
        return ans;
    }
};
