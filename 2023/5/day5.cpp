#include <iostream>
#include <fstream>
#include <vector>

std::vector<long> parseSeeds(std::string line) {
    std::vector<long> ret;
    std::string buffer;
    for (int x = 7; x < line.length(); x ++) {
        if (line[x] == ' ') {
            std::cout << "buffer est " << buffer << std::endl;
            ret.push_back(std::stol(buffer));
            buffer = "";
        }
        else {
            buffer += line[x];
        }
    }
    if (buffer != "") {
        ret.push_back(std::stol(buffer));
    }
    return ret;
}

int mapValue(long source, long dest, long range, long num) {
    
}

int main() {
    std::ifstream file;
    file.open("day5-input.txt");
    std::string buffer;
    std::string lines[174];
    int lineNum = 0;

    if (file.is_open()) {
        while (std::getline(file, buffer)) {
            lines[lineNum] = buffer;
            lineNum ++;
        }
        std::vector<long> seeds = parseSeeds(lines[0]);
        for (int x = 0; x < seeds.size(); x ++) {
            std::cout << seeds.at(x) << std::endl;
        }
    }
}