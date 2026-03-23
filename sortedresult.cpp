#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

void printSortedSet(const std::set<int>& s, const std::string& setName) {
    std::cout << setName << " (sorted): { ";
    for (const auto& elem : s) {
        std::cout << elem << " ";
    }
    std::cout << "}" << std::endl;
}


int main() {
    // Example sets
    std::set<int> running = {0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 16, 17, 18, 19,
                             20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36,
                             37, 39, 40, 41, 44, 45, 46, 47, 50, 51, 52, 53};

    std::set<int> hammer = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                            22, 23, 26, 28, 29, 30, 31, 32, 37, 38, 41, 44, 47, 48, 52, 55};

    std::set<int> actions_and_wanted = {0, 1, 2, 3, 5, 7, 9, 12, 15, 16, 17, 19, 24, 26,
                                        28, 29, 31, 37, 39, 40, 41, 42, 51, 53, 54};

    std::set<int> united_or_plane = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17,
                                     18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                                     33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47,
                                     48, 49, 50, 51, 52, 54, 55};

    std::set<int> pakistan_or_afganistan_or_aid = {1, 3, 4, 9, 16, 17, 18, 22, 29, 37, 39, 40, 41, 42};

    std::set<int> biggest_and_near_or_box = {4, 6, 18, 43, 44, 45, 46, 47, 50, 51, 53, 54};

    std::set<int> box_and_united_or_year = {4, 9, 18, 23, 25, 44, 45, 46, 47, 50, 54};

    std::set<int> biggest_and_plane_or_wanted_or_hour = {0, 1, 2, 4, 6, 7, 8, 16, 18, 19, 26, 30,
                                                         35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46,
                                                         47, 48, 49, 50, 51, 52, 53, 54};

    std::set<int> not_united_and_plane = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18,
                                          20, 21, 22, 23, 28, 31, 37, 38, 39, 40, 41, 42, 43, 44,
                                          45, 46, 47, 48, 49, 50, 51, 53, 54, 55};

    std::set<int> hillary_clinton = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19,
                                     20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                     36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                                     52, 53, 54};

    std::set<int> after_years = {6, 7, 44};

    std::set<int> develop_solutions = {5, 32};

    std::set<int> keep_out = {20, 24, 39, 40, 51};

    // Print sorted sets
    printSortedSet(running, "Running");
    printSortedSet(hammer, "Hammer");
    printSortedSet(actions_and_wanted, "Actions AND Wanted");
    printSortedSet(united_or_plane, "United OR Plane");
    printSortedSet(pakistan_or_afganistan_or_aid, "Pakistan OR Afganistan OR Aid");
    printSortedSet(biggest_and_near_or_box, "Biggest AND (Near OR Box)");
    printSortedSet(box_and_united_or_year, "Box AND (United OR Year)");
    printSortedSet(biggest_and_plane_or_wanted_or_hour, "Biggest AND (Plane OR Wanted OR Hour)");
    printSortedSet(not_united_and_plane, "NOT (United AND Plane)");
    printSortedSet(hillary_clinton, "Hillary Clinton");
    printSortedSet(after_years, "After Years");
    printSortedSet(develop_solutions, "Develop Solutions");
    printSortedSet(keep_out, "Keep Out");

    return 0;
}