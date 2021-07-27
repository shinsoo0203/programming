#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    int dx[] = {1, 0};
    int dy[] = {0, 1};
    
    vector<vector<int>> route(n,vector <int>(m,1));
    
    for (int i; i<puddles.size(); i++)
    {
        int x = puddles[i][0];
        int y = puddles[i][1];
        route[x-1][y-1] = 0;
    }
    
    queue<pair<int,int>> q;
    
    q.push(make_pair(0,0));
    
    
    while ( q.size() > 0 )
    {
        pair<int, int> now = q.front();
        int a = now.first;
        int b = now.second;
        cout<<a<<" "<<b<<endl;
        q.pop();
        
        for (int i =0; i<2; i++)
        {
            int x = a + dx[i];
            int y = b + dy[i];
            cout<<x<<" "<<y<<endl;
            cout<<route[x][y]<<endl;
            if ( 0<= x < m and 0<= y < n and route[x][y] == 1)
            {
                route[x][y] = route[a][b] + 1;
                q.push(make_pair(1,1));
            }
        }
           
    }
    
    return answer;
}