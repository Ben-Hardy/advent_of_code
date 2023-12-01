#include "p1.hpp"

void p1() {
	auto input {read_file("p1input.txt")};
	input.pop_back();

	std::vector<int> str_nums {};

	for (auto itr : input) {
		std::stringstream ss {};
		for (auto chr : itr) {
			if (isdigit(chr)) {
				ss << chr;
			}
		}
		std::stringstream result {};
		result << ss.str().at(0) << ss.str().at(ss.str().size() - 1);
		str_nums.push_back(std::stoi(result.str()));
	}

	int total {0};

	for (auto i : str_nums) {
		total += i;
	}

	std::cout << "Total: " << total << '\n';
}