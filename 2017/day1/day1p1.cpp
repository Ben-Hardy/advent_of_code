#include "day1p1.hpp"

void day1p1() {
	std::vector<std::string> in_vec {read_file("p1input.txt")};

	for (auto itr : in_vec) {
		std::string num_list {itr};
		std::cout << num_list << '\n';

		if (num_list.size() > 0) {
			int sum {0};
			for (int i {0}; i < (num_list.size() - 1); i++) {
				if (num_list.at(i) == num_list.at(i + 1)) {
					sum += (num_list.at(i) - '0'); // converts char of a digit to the digit
				}
			}
			
			// complete the circular list by comparing the first value to the last
			if (num_list.at(0) == num_list.at(num_list.size() - 1)) {
				sum += (num_list.at(0) - '0');	
			}

			std::cout << "total: " << sum << '\n';
		}
	}
}