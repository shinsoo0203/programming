#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long calc(long long a, long long b, char op)
{
    if (op == '-')   return a - b;
    else if (op == '+')  return a + b;
    else    return a * b;
}



long long solution(string expression) {

    long long answer = 0;

    vector<long long> number;
    string s = "";
    vector<char> oper;
    vector <char> oper_list = { '*', '+', '-' };

    for (int i = 0; i < expression.size(); i++)
    {
        if (expression[i] >= '0' and expression[i] <= '9')
        {
            s += expression[i];
        }
        else
        {
            oper.push_back(expression[i]);
            number.push_back(stoi(s));
            s = "";
        }
    }
    number.push_back(stoi(s));

    long long num_max = 0;
    vector<char> tmp_oper;
    vector<long long> tmp_number;

    do
    {
        tmp_number = number;
        tmp_oper = oper;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < tmp_oper.size(); j++)
            {
                if (tmp_oper[j] == oper_list[i])
                {
                    tmp_number[j] = calc(tmp_number[j], tmp_number[j + 1], oper_list[i]);
                    tmp_number.erase(tmp_number.begin() + j + 1);
                    tmp_oper.erase(tmp_oper.begin() + j);
                    j--;
                }
            }
        }
        if (num_max < abs(tmp_number[0]))   num_max = abs(tmp_number[0]);
    } while (next_permutation(oper_list.begin(), oper_list.end()));

    answer = num_max;
    return answer;
}