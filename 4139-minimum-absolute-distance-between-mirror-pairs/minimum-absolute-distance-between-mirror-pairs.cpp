#include <memory_resource>
pmr::unsynchronized_pool_resource pool;
class Solution {
public:
    static int rev(int x){
        int ans=0;
        for(; x>0; x/=10){
            const int d=x%10;
            ans=10*ans+d;
        }
        return ans;
    }
    static int minMirrorPairDistance(vector<int>& nums) {
        const int n=nums.size();
        pmr::unordered_map<int, int> mp(&pool);
        mp.reserve(n);
        int dist=INT_MAX;
        for(int i=0; i<n; i++){
            const int x=nums[i], R=rev(x);
        //    cout<<i<<"->"<< x<<", Rev="<<R<<endl;
            auto it=mp.find(x);
            if (it!=mp.end())
                dist=min(dist, i-it->second);
            mp[R]=i;
        }
        return dist==INT_MAX?-1:dist;
    }
};