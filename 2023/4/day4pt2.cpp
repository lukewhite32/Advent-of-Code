#include <iostream>
#include <fstream>
#include <vector>

int cardAmts[198];

int getCardNum(std::string s) {
    return std::stoi(s.substr(5, 3));
}
 
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
                ret ++;
            }
        }
    }
    return ret;
}

int main() {
    std::ifstream file;
    std::string line;
    int v = 0;
    int currCard = 0;
    int total = 0;
    file.open("day4-input.txt");
    for (int x = 0; x < 198; x ++) {
        cardAmts[x] = 1;
    }

    if (file.is_open()) {
        while (std::getline(file, line)) {
            v = getLineValue(line);
            for (int x = 0; x < cardAmts[currCard]; x ++) {
                for (int y = currCard+1; y < currCard+v+1; y ++) {
                    if (y == 5) {
                        std::cout << "caused on " << currCard << std::endl;
                    }
                    cardAmts[y] ++;
                }
            }

            currCard ++;
        }
    }
    for (int x = 0; x < 198; x ++) {
        std::cout << "Card " << x << ": " << cardAmts[x] << std::endl;
        total += cardAmts[x];
    }
    std::cout << total << std::endl;

    return 0;
}