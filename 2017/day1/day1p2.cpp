#include "day1p2.hpp"

void day1p2() {
	auto in_vec {read_file("p2input.txt")};

	for (auto itr : in_vec) {
		std::string num_list {itr};
		std::cout << num_list << '\n';

		if (num_list.size() > 0) {
			int sum {0};
			int half_len {(int) num_list.size() / 2};
			for (int i {0}; i < num_list.size(); i++) {
				if (i < half_len) {
					if (num_list.at(i) == num_list.at(i + half_len)) {
						sum += (num_list.at(i) - '0');		
					}
				} else {
					if (num_list.at(i) == num_list.at(i - half_len)) {
						sum += (num_list.at(i) - '0');	
					}
				}
			}
			std::cout << "total: " << sum << '\n';
		}
	}
}