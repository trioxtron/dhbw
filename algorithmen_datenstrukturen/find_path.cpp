#include <iostream>
#include <vector>
#include <chrono>
using namespace std;


int find(int x, vector<int>& parent) {
    int root = x;
    while (root != parent[root]) {
        parent[root] = parent[parent[root]];
        root = parent[root];
    }
            
    while (x != root) {
        int tmp = parent[x];
        parent[x] = root;
        x = tmp;
    }

    return root;
}

int find_recursive(int x, vector<int>& parent) {
    if (x == parent[x]) {
        return x;
    }
    parent[x] = find(parent[x], parent); // Path compression
    return parent[x];
}

void union_nodes(int x, int y, vector<int>& parent, vector<int>& depth) {
    int xRoot = find(x, parent);
    int yRoot = find(y, parent);

    if (xRoot == yRoot) return;

    if (depth[xRoot] > depth[yRoot]) {
        parent[yRoot] = xRoot;
    } else if (depth[xRoot] < depth[yRoot]) {
        parent[xRoot] = yRoot;
    } else {
        parent[yRoot] = xRoot;
        depth[xRoot]++;
    }
}

void union_nodes_recursive(int x, int y, vector<int>& parent, vector<int>& depth) {
    int xRoot = find_recursive(x, parent);
    int yRoot = find_recursive(y, parent);

    if (xRoot == yRoot) return;

    if (depth[xRoot] > depth[yRoot]) {
        parent[yRoot] = xRoot;
    } else if (depth[xRoot] < depth[yRoot]) {
        parent[xRoot] = yRoot;
    } else {
        parent[yRoot] = xRoot;
        depth[xRoot]++;
    }
}



bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
    vector<int> parent;
    vector<int> depth;

    for (int i=0; i < n; i++) {
        parent.push_back(i);
        depth.push_back(1);
    }

    for (int i=0; i < edges.size(); i++) {
        union_nodes(edges[i][0], edges[i][1], parent, depth);
    }


    return find(source, parent) == find(destination, parent);
}

bool validPath_recursive(int n, vector<vector<int>>& edges, int source, int destination) {
    vector<int> parent;
    vector<int> depth;

    for (int i=0; i < n; i++) {
        parent.push_back(i);
        depth.push_back(1);
    }

    for (int i=0; i < edges.size(); i++) {
        union_nodes_recursive(edges[i][0], edges[i][1], parent, depth);
    }


    return find_recursive(source, parent) == find_recursive(destination, parent);
}


int main() {
    int n = 5;
    vector<vector<int>> edges = {{0,1},{1,2},{2,3},{3,4}};
    int source = 0;
    int destination = 4;


    // Measure the time taken to find a valid path
    auto start = chrono::high_resolution_clock::now();
    validPath(n, edges, source, destination);
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Time taken: " << duration.count() << " microseconds" << endl;

    // Measure the time taken to find a valid path
    start = chrono::high_resolution_clock::now();
    validPath_recursive(n, edges, source, destination);
    end = chrono::high_resolution_clock::now();
    duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Time taken: " << duration.count() << " microseconds" << endl;

    n = 2;
    edges.clear();
    edges = {{0,1},{1,2},{0,2}};
    source = 0;
    destination = 2;

    // Measure the time taken to find a valid path for a large graph
    start = chrono::high_resolution_clock::now();
    validPath(n, edges, source, destination);
    end = chrono::high_resolution_clock::now();
    duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Time taken: " << duration.count() << " microseconds" << endl;

    // Measure the time taken to find a valid path
    start = chrono::high_resolution_clock::now();
    validPath_recursive(n, edges, source, destination);
    end = chrono::high_resolution_clock::now();
    duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Time taken: " << duration.count() << " microseconds" << endl;


    n = 100000;
    edges.clear();
    for (int i = 0; i < n - 1; i++) {
        edges.push_back({i, i + 1});
    }
    source = 0;
    destination = n - 1;

    // Measure the time taken to find a valid path for a large graph
    start = chrono::high_resolution_clock::now();
    validPath(n, edges, source, destination);
    end = chrono::high_resolution_clock::now();
    duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Time taken: " << duration.count() << " microseconds" << endl;

    // Measure the time taken to find a valid path
    start = chrono::high_resolution_clock::now();
    validPath_recursive(n, edges, source, destination);
    end = chrono::high_resolution_clock::now();
    duration = chrono::duration_cast<chrono::microseconds>(end - start);
    cout << "Time taken: " << duration.count() << " microseconds" << endl;

    return 0;
}
