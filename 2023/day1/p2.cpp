#include "p2.hpp"

void p2() {
	auto input {read_file("p1input.txt")};
	input.pop_back();

	std::vector<int> str_nums {};

	for (std::string itr : input) {
		std::stringstream ss {};
		std::string cur {itr};
		
		for (int i = 0; i < cur.size(); i++) {
			if (isdigit(cur.at(i))) {
				ss << cur.at(i);
			}
			else if (cur.substr(i, 3) == "one") {
						ss << "1";
			}
			else if (cur.substr(i, 5) == "three") {
				ss << "3";
			}
			else if (cur.substr(i, 3) == "two") {
				ss << "2";
			}
			else if (cur.substr(i,4) == "four") {
				ss << "4";
			}
			else if (cur.substr(i,4) == "five") {
				ss << "5";
			}
			else if (cur.substr(i,5) == "seven") {
				ss << "7";
			}
			else if (cur.substr(i,3) == "six") {
				ss << "6";
			}
			else if (cur.substr(i,5) == "eight") {
				ss << "8";
			}
			else if (cur.substr(i,4) == "nine") {
				ss << "9";
			}
		}
		if (ss.str().size() > 0) {
			std::stringstream result {};
			result << ss.str().at(0) << ss.str().at(ss.str().size() - 1);
			str_nums.push_back(std::stoi(result.str()));
		}
	}

	int total {0};

	for (auto i : str_nums) {
		total += i;
	}

	std::cout << "Total: " << total << '\n';
}