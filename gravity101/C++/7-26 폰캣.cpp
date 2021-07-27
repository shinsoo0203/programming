#include <vector>
#include <iostream>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    int n = nums.size() / 2;

    cout << n;
    int answer = 0;

    set<int> pocket(nums.begin(), nums.end());

    if (pocket.size() >= n)
    {
        return n;
    }
    else
    {
        return pocket.size();
    }

    return answer;
}
