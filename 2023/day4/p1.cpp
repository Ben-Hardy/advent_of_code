#include "p1.hpp"

void p1() {
	auto input {read_file("p1input.txt")};
	int score {0};
	for (auto line : input) {
		std::stringstream ss {line};
		std::string token {};
		std::vector<int> winning_numbers {};
		std::vector<int> player_numbers;
		
		// clear out the beginning of each line
		ss >> token;
		ss >> token;
		
		for (int i {0}; i < 10; i++) {
			ss >> token;
			if (token.size() > 0) {
				winning_numbers.push_back(std::stoi(token));
			}
		}
		ss >> token;
		
		for (int i : winning_numbers) {
			std::cout << i << " ";
		}
		std::cout << '\n';
		
		for (int i {0}; i < 25; i++) {
			ss >> token;
			if (token.size() > 0) {
				player_numbers.push_back(std::stoi(token));
			}
		}
		int matches {0};
		for (int i : player_numbers) {
			std::cout << i << " ";
			if (std::find(winning_numbers.begin(), winning_numbers.end(), i) != winning_numbers.end()) {
				matches++;
			}
		}
		int temp_score {0};
		if (matches == 1) {
			temp_score = 1;
		} else {
			temp_score += pow(2, matches - 1);
		}
		score += temp_score;
		
		std::cout << '\n';
	}
	std::cout << "Score: " << score << '\n';
}