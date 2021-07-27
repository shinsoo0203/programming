#include <iostream>
#include<vector>
using namespace std;

int solution(vector<vector<int>> board)
{
    int answer = 1234;

    int n = min(board.size(), board[0].size());

    for (int t = n; t > 0; t--)
    {

        for (int i = 0; i <= board.size() - t; i++)
        {
            for (int j = 0; j <= board[i].size() - t; j++)
            {

                int count = 0;
                int check = 0;
                for (int x = i; x < t + i; x++)
                {
                    for (int y = j; y < t + j; y++)
                    {

                        if (board[x][y] == 0)
                        {
                            check = 1;
                            break;
                        }
                        count++;
                    }
                    if (check == 1)
                        break;
                }
                cout << count << endl;
                if (count == t * t)
                    return t * t;
            }
        }
    }
    return n;
}