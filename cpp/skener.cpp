// https://open.kattis.com/problems/skener

#include <iostream>
#include <string>
using namespace std;

string scanLine(string line, int zRows, int zColumns) {
	string outRow = "";
	for (char const &c: line) {
		outRow += string(zColumns, c);
	}
	string outLine = "";
	for (int i = 0; i < zRows; i++) {
		outLine = outLine + outRow + "\n"; 
	}
	return outLine;
}

int main() {
	int rows;
	int columns;
	int zRows;
	int zColumns;
	std::cin >> rows >> columns >> zRows >> zColumns;
	
	string line;
	getline(cin, line);
	string output[rows];
	for (int i = 0; i < rows; i++) {
		getline(cin, line);
		std::cout << scanLine(line, zRows, zColumns);
	}
}
