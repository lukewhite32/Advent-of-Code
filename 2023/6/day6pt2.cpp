#include <iostream>
#include <fstream>
#include <vector>

long calculateDistanceTravelled(long buttonTime, long raceTime) {
    return buttonTime * (raceTime - buttonTime); // thanks tyler
}

long parseValues(std::string s) {
    std::string buffer;

    for (int x = 0; x < s.length(); x ++) {
        if (isdigit(s[x])) {
            buffer += s[x];
        }
    }
    return std::stol(buffer);
}

int main() {
    long distance = parseValues("Distance:   282   1079   1147   1062");
    long time = parseValues("Time:        47     70     75     66");
    long total = 0;
    std::cout << "d: " << distance << ", t: " << time << std::endl;

        for (long y = 0; y < time; y ++) {
            if (calculateDistanceTravelled(y, time) > distance) {
                total ++;
            }
        }
    std::cout << total << std::endl;
}