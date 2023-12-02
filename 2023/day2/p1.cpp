#include "p1.hpp"

void p1() {
	auto input {read_file("p1input.txt")};
	int total {0};
										// red, green, blue
	std::array<int, 3> max_accepted_inputs {12, 13, 14};


	for (auto itr : input) {
		int cur_game {0};
										// red, green, blue
		std::array<int, 3> colour_counts {0, 0, 0};
		std::stringstream str_chunks {itr};

		std::string token;
		std::string extra_token;
		while (str_chunks >> token) {
			if (token == "Game") {
				str_chunks >> extra_token;
				cur_game = std::stoi(extra_token.substr(0, extra_token.size() - 1));
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
		
		if (colour_counts.at(0) <= max_accepted_inputs.at(0) 
		 && colour_counts.at(1) <= max_accepted_inputs.at(1) 
		 && colour_counts.at(2) <= max_accepted_inputs.at(2)) {
			total += cur_game;
		}
	}
	std::cout << "P1 Total: " << total << '\n';
}