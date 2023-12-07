#include <iostream>
#include <fstream>
#include <vector>

int calculateDistanceTravelled(int buttonTime, int raceTime) {
    int ret = 0;
    for (int x = buttonTime; x < raceTime; x ++) {
        ret += buttonTime;
    }
    return ret;
}

std::vector<int> parseValues(std::string s) {
    std::vector<int> ret;
    std::string buffer;

    for (int x = 0; x < s.length(); x ++) {
        if (isdigit(s[x])) {
            buffer += s[x];
        }
        else {
            if (buffer != "") {
                ret.push_back(std::stoi(buffer));
                buffer = "";
            }
        }
    }
    if (buffer != "") {
        ret.push_back(std::stoi(buffer));
    }
    return ret;
}

int main() {
    std::vector<int> distances = parseValues("Distance:   282   1079   1147   1062");
    std::vector<int> times = parseValues("Time:        47     70     75     66");
    std::vector<int> winPossibilities;
    int total = 0;;

    for (int x = 0; x < distances.size(); x ++) {
        for (int y = 0; y < times.at(x); y ++) {
            if (calculateDistanceTravelled(y, times.at(x)) > distances.at(x)) {
                total ++;
            }
        }
        winPossibilities.push_back(total);
        total = 0;
    }
    int buff = winPossibilities.at(0);
    for (int x = 1; x < winPossibilities.size(); x ++) {
        buff *= winPossibilities.at(x);
    }
    std::cout << buff <<std::endl;
}