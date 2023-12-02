#include <iostream>
#include <fstream>

int parseGameId(std::string s) {
    std::string buffer = "";
    for (int x = 5; x < s.length(); x ++) {
        if (s[x] == ':') {
            return std::stoi(buffer);
        }
        buffer += s[x];
    }
    return std::stoi(buffer);
}

bool isPossible(std::string s) {
    std::string numBuffer = "";
    int index = 0;
    for (int x = 0; x < s.length(); x ++) {
        if (s[x] == ':') {
            index = x + 1;
            break;
        }
    }
    for (int x = index; x < s.length(); x ++) {
        if (s[x] == ' ') {
            std::cout << "Buffer est " << numBuffer << std::endl;
            if (s[x+1] == 'b') {
                if (std::stoi(numBuffer) > 14) {
                    return false;
                }
            }
            else if (s[x+1] == 'g') {
                if (std::stoi(numBuffer) > 13) {
                    return false;
                }
            }
            else if (s[x+1] == 'r') {
                if (std::stoi(numBuffer) > 12) {
                    return false;
                }
            }
            numBuffer = "";
        }
        else {
            numBuffer += s[x];
        }
    }
    return true;
}

int getValueOfGame(std::string s) {
    std::string numBuffer = "";
    bool buffering = false;
    int index = 0;
    for (int x = 0; x < s.length(); x ++) {
        if (s[x] == ':') {
            index = x + 2;
            break;
        }
    }
    int greatestRed = 0;
    int greatestGreen = 0;
    int greatestBlue = 0;

    int num = 0;
    for (int x = index; x < s.length(); x ++) {
        if (s[x] == ' ') {
            buffering = !buffering;
            if (buffering) {
                num = std::stoi(numBuffer);
                if (s[x+1] == 'b') {
                    if (num > greatestBlue) {
                        greatestBlue = num;
                    }
                }
                else if (s[x+1] == 'g') {
                    if (num > greatestGreen) {
                        greatestGreen = num;
                    }
                }
                else if (s[x+1] == 'r') {
                    if (num > greatestRed) {
                        greatestRed = num;
                    }
                }
                numBuffer = "";
            }

        }
        else {
             if (!buffering) {
                numBuffer += s[x];
             }
        }
    }
    return greatestBlue * greatestGreen * greatestRed;
}

int main() {
    std::ifstream file;
    std::string buffer;
    int total = 0;
    file.open("day2-input.txt");

    if (file.is_open()) {
        while (std::getline(file, buffer)) {
            total += getValueOfGame(buffer);
        }
    }
    std::cout << total << std::endl;
    return 0;
}