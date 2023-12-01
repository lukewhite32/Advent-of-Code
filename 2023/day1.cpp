#include <iostream>
#include <fstream>

std::string numStrs[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
// Returns the most recent string number it finds
int parseStringToNum(std::string input) {
    for (int x = 0; x < input.length(); x ++) {
        for (int y = 0; y < 10; y ++) {
            if (isdigit(input[x])) {
                return -1;
            }
            if (input.substr(x, numStrs[y].length()) == numStrs[y]) {
                return y;
            }
        }
    }
    return -1;
}

int getNumStringLoc(std::string input) {
    for (int x = 0; x < input.length(); x ++) {
        for (int y = 0; y < 10; y ++) {
            if (input.substr(x, numStrs[y].length()) == numStrs[y]) {
                return x;
            }
        }
    }
    return -1;
}

int getNum(std::string input) {
    std::string ret = "";
    for (int x = 0; x < input.length(); x ++) {
        if (isdigit(input[x])) {
            ret += input[x];
        }
        else {
            int n = parseStringToNum(input.substr(x));
            if (n != -1) {
                ret += std::to_string(n);
            }
            if (n == 0) {
                std::cout << "ye" << std::endl;
            }
        }
    }
    ret = std::string(1, ret[0]) + std::string(1, ret[ret.length()-1]);
    std::cout << "RET: " << ret << std::endl;
    return std::stoi(ret);
}

int main() {
    std::ifstream file;
    std::string buffer;
    int ret = 0;
    file.open("day1-input.txt");
    if (file.is_open()) {
        while (std::getline(file, buffer)) {
            ret += getNum(buffer);
        }
    }
    std::cout << ret << std::endl;
    return 0;
}