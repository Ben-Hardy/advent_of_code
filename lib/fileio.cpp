#include "fileio.hpp"

std::vector<std::string> read_file(std::string file_name) {
	std::vector<std::string> file_contents {};

	std::ifstream input_file{file_name};

	if (!input_file) {
		std::cerr << file_name << " could not be read.\n";
	}

	while (input_file) {
		std::string file_line {};
		std::getline(input_file, file_line);
		file_contents.push_back(file_line);
	}
	
	return file_contents;
}

std::vector<std::string> split_string(std::string str) {
	std::stringstream str_str(str);
	std::vector<std::string> tokens {};
	std::string token;
	while (str_str >> token) {
		tokens.push_back(token);
	}

	return tokens;
}
