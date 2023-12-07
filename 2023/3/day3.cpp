#include <iostream>
#include <fstream>

int getLineValue(std::string before, std::string l, std::string after) {
    std::string numBuffer = "";
    int ret = 0;
    bool isParsing = false;
    int numBegin = 0;
    int numEnd = 0;
    for (int x = 0; x < l.length(); x ++) {
        if (isdigit(l[x])) {
            if (!isParsing) {
                numBegin = x;
            }
            isParsing = true;
            numBuffer += l[x];
        }
        else if (isParsing) {
            if (numEnd == 0) {
                numEnd = x - 1;
            }
            for (int y = numBegin-1; y < numEnd+2; y ++) {
                if ((before[y] != '.')) {
                    ret += std::stoi(numBuffer);
                }
                if ((after[y] != '.')) {
                    ret += std::stoi(numBuffer);
                }
            }
            if ((l[numBegin-1] != '.') || (l[numEnd+1] != '.')) {
                ret += std::stoi(numBuffer);
            }

            numBuffer = "";
            numEnd = 0;
            isParsing = false;

            
        }
    }
    return ret;
}

int main() {
    std::ifstream file;
    std::string buffer;
    std::string man;
    std::string lines[142];
    int lineNum = 0;
    int total = 0;
    file.open("day3-input.txt");
    if (file.is_open()) {
        while (std::getline(file, buffer)) {
            lines[lineNum] = buffer;
            lineNum ++;
        }
        total += getLineValue("...................................................................................................................", lines[0], lines[1]);
        for (int x = 1; x < 141; x ++) {
            total += getLineValue(lines[x-1], lines[x], lines[x+1]);
            //std::cin >> man;
        }
    }
    std::cout << total << std::endl;
    return 0;
}