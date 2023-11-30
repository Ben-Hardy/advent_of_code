#pragma once
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>

std::vector<std::string> read_file(std::string file_name);

std::vector<std::string> split_string(std::string str, char delimiter);