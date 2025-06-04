class Solution {
public:
    string answerString(string word, int numFriends) {
        if(numFriends == 1) return word;

        vector<int> v;
        char ch = *max_element(word.begin(), word.end());
        int n = word.size();
        int ele = n - numFriends + 1;
        string maxa = "";

        // Store all indices of the maximum character
        for (int i = 0; i < n; ++i) {
            if (word[i] == ch) v.push_back(i);
        }

        // From each max character index, extract candidate substrings
        for (int i : v) {
            string ans = (ele <= n - i) ? word.substr(i, ele) : word.substr(i);
            maxa = max(maxa, ans);
        }

        return maxa;
    }
};