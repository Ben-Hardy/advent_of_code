#include "p2.hpp"

void p2() {
	auto input {read_file("p1input.txt")};
	int total {0};


	for (auto itr : input) {

										// red, green, blue
		std::array<int, 3> colour_counts {0, 0, 0};
		std::stringstream str_chunks {itr};

		std::string token;
		std::string extra_token;
		while (str_chunks >> token) {
			if (token == "Game") {
				str_chunks >> extra_token;
			}
			else {
				str_chunks >> extra_token;
				if (extra_token.substr(0,3) == "red") {
					if (std::stoi(token) > colour_counts.at(0)) {
						colour_counts[0] = std::stoi(token);
					}
				}
				else if (extra_token.substr(0,5) == "green") {
					if (std::stoi(token) > colour_counts.at(1)) {
						colour_counts[1] = std::stoi(token);
					}
				}
				else if (extra_token.substr(0,4) == "blue") {
					if (std::stoi(token) > colour_counts.at(2)) {
						colour_counts[2] = std::stoi(token);
					}
				}
			}
		}
		total += colour_counts.at(0) * colour_counts.at(1) * colour_counts.at(2);
	}
	std::cout << "P2 Total: " << total << '\n';

}