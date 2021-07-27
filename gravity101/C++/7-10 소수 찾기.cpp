#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>

using namespace std;

int solution(string numbers)
{
    int answer = 0;
    vector<int> v;
    vector<int> sum_total;
    set<int> s;
    for (auto element : numbers)
        v.push_back(element - 48);

    do
    {
        int sum = 0;
        int size = 1;
        for (int i = 0; i < numbers.size(); i++)
        {
            sum += v[i] * size;
            s.insert(sum);
            size *= 10;
        }

    } while (next_permutation(v.begin(), v.end()));

    bool check = true;

    set<int>::iterator iter;
    for (iter = s.begin(); iter != s.end(); iter++)
    {
        cout << sqrt(*iter) << ' ' << *iter;
        for (int j = 2; j <= sqrt(*iter); j++)
        {
            if (*iter % j == 0)
            {
                check = false;
                break;
            }
        }

        if (check == true and *iter != 0 and *iter != 1)
            answer++;
        else
            check = true;


        cout << endl;
    }




    return answer;
}




return answer;