# C++

"""class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int>A;
        map<char, int>B;

        if (s.size() != t.size()){
            return false;
        }
        else{
            for(int i = 0; i < s.size(); i++){
                if (A.count(s[i]) == 0){
                    A[s[i]] = 1;
                }
                else{
                    A[s[i]] ++;
                }

                if (B.count(t[i]) == 0){
                    B[t[i]] = 1;
                }
                else{
                    B[t[i]] ++;
                }
            }
        }

        if(A == B){
            return true;
        }
        else{
            return false;
        }
    }
};"""

