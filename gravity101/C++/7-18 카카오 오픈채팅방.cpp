#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>

using namespace std;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    int col = record.size();
    string stringBuffer;
    vector<vector<string>> v(col, vector <string>());
    map<string, string> id_name;
    string temp = "";
    for (int i = 0; i < record.size(); i++)
    {
        for (int j = 0; j < record[i].size(); j++)
        {
            if (record[i][j] == ' ')
            {
                v[i].push_back(temp);
                temp = "";
            }
            else
            {
                temp += record[i][j];
            }
        }
        v[i].push_back(temp);
        temp = "";
    }


    for (int i = 0; i < v.size(); i++)
    {
        if (v[i][0] == "Enter" or v[i][0] == "Change")
        {
            if (id_name.find(v[i][1]) != id_name.end())
            {
                id_name.erase(v[i][1]);
            }

            id_name.insert({ v[i][1], v[i][2] });
        }
    }



    for (int i = 0; i < v.size(); i++)
    {
        temp = "";
        if (v[i][0] == "Enter")
        {
            temp += id_name[v[i][1]];
            temp += "´ÔÀÌ µé¾î¿Ô½À´Ï´Ù.";
            answer.push_back(temp);
        }
        else if (v[i][0] == "Leave")
        {
            temp += id_name[v[i][1]];
            temp += "´ÔÀÌ ³ª°¬½À´Ï´Ù.";
            answer.push_back(temp);
        }
    }
    return answer;
}