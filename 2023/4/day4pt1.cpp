#include <iostream>
#include <fstream>
#include <vector>

int getLineValue(std::string line) {
    std::vector<int> winningNums;
    std::vector<int> checkingNums;

    std::string buffer;
    std::string currNum;
    bool isParsing = false;
    int ret = 0;

    for (int x = 0; x < line.length(); x ++) {
        if (line[x] == ':') {
            isParsing = true;
        }
        else if (isParsing) {
            if (line[x] == '|') {
                for (char c : buffer) {
                    if (c == ' ') {
                        if (currNum != "") {
                            winningNums.push_back(std::stoi(currNum));
                            currNum = "";
                        } 
                    }
                    else {
                        currNum += c;
                    }
                }
                buffer = "";
            }
            else {
                buffer += line[x];
            }
        }
    }
    currNum = "";
    for (char c : buffer) {
        if (c == ' ') {
            if (currNum != "") {
                checkingNums.push_back(std::stoi(currNum));
                currNum = "";
            }
        }
        else {
            currNum += c;
        }
    }
    checkingNums.push_back(std::stoi(currNum));
    for (int x = 0; x < checkingNums.size(); x ++) {
        for (int y = 0; y < winningNums.size(); y ++) {
            if (checkingNums.at(x) == winningNums.at(y)) {
                if (ret == 0) {
                    ret = 1;
                }
                else {
                    ret *= 2;
                }
            }
        }
    }
    return ret;
}

int main() {
    std::ifstream file;
    std::string line;
    int total = 0;
    file.open("day4-input.txt");

    if (file.is_open()) {
        while (std::getline(file, line)) {
            total += getLineValue(line);
        }
    }
    std::cout << total << std::endl;
    return 0;
}