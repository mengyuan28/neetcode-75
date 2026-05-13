class Solution {
public:
    void getFrequency(string s, unordered_map<char, int>&mapping) {
        for (int i = 0; i < s.size(); i++) {
            if (mapping.contains(s[i])) {
                mapping[s[i]]++;
            } else {
                mapping[s[i]] = 1;
            }
        }
    }
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_check;
        getFrequency(s, s_check);
        unordered_map<char, int> t_check;
        getFrequency(t, t_check);
        return t_check == s_check;
    }
};
