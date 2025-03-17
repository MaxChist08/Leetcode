# C++

"""class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map <char, int>A;

        for (auto x : magazine) {
            if (A.count(x) == 0) {
                A[x] = 1;
            }
            else {
                A[x]++;
            }
        }

        for (auto x : ransomNote) {
            if (A.count(x) == 0) {
                return false;
            }
            if (A[x] == 0) {
                return false;
            }
            else {
                A[x]--;
            }
        }

        return true;
    }
};"""