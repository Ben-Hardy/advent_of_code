#include "p1.hpp"

void p1() {
	auto input {read_file("p1input.txt")};
	std::string symbols {"*=+/@-#$%"};

	for (auto line : input) {
		std::cout << line << '\n';
	}

	int row_count {(int) input.size() - 1};
	int col_count {(int) input.at(0).size()};
	// std::cout << "Rows: " << line_count << ", Columns: " << col_count << '\n';

	int total {0};
	
	// add all numbers to the total. we are going to be subtracting those that
	// aren't adjacent to symbols rather than trying to determin which ones
	// are adjacent.
	for (auto i {0}; i < row_count; i++) {
		std::string ss {};
		bool is_adj {false};
		for (auto j {0}; j < col_count; j++) {
			if (input.at(i).at(j) == '.' || symbols.find(input.at(i).at(j)) != std::string::npos) {
				if (ss.size() > 0) {
					if (is_adj) {
						total += std::stoi(ss);
					}
					ss.clear();
					is_adj = false;
				}
			} else if (isdigit(input.at(i).at(j))) {
				ss += input.at(i).at(j);
				// check around the string for symbols
				
				// before I start I need to vent. Why the hell doesn't C++ have string.contains()? They just added
				// it to the C++23 standard but it's not in Apple clang yet. This is completely stupid. Every other
				// language I've used except C and fortran have some kind of string.contains() function. This is basic
				// stuff and C++ not having something as basic as contains() really shows what's wrong with the language.
				// I'm already regretting trying to use C++ for this year's advent of code.
				
				// check entries to the left
				if (j - 1 >= 0) {
					if (i - 1 >= 0) {
						if (symbols.find(input.at(i - 1).at(j - 1)) != std::string::npos) {
							is_adj = true;
						}
					}
					if (symbols.find(input.at(i).at(j - 1)) != std::string::npos) {
						is_adj = true;
					}
					if (i + 1 < row_count) {
						if (symbols.find(input.at(i + 1).at(j - 1)) != std::string::npos) {
							is_adj = true;
						}
					}
				}
				// check entries directly above and below
				if (i - 1 >= 0) {
					if (symbols.find(input.at(i - 1).at(j)) != std::string::npos) {
						is_adj = true;
					}
				}
				if (i + 1 < col_count) {
					if (symbols.find(input.at(i + 1).at(j)) != std::string::npos) {
						is_adj = true;
					}
				}
				// check entries to the right
				if (j + 1 < col_count) {
					if (i - 1 > 0) {
						if (symbols.find(input.at(i - 1).at(j + 1)) != std::string::npos) {
							is_adj = true;
						}
					}
					if (symbols.find(input.at(i).at(j + 1)) != std::string::npos) {
						is_adj = true;
					}
					if (i + 1 < row_count) {
						if (symbols.find(input.at(i + 1).at(j + 1)) != std::string::npos) {
							is_adj = true;
						}
					}
				}
			}
		}
		if (ss.size() > 0) {
			if (is_adj) {
				total += std::stoi(ss);
			}
			ss.clear();
			is_adj = false;
			}
	}
	std::cout << "Total before: " << total << '\n';
}