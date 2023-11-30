CXX = clang++
CXXFLAGS = -Wall -Werror -std=c++20

SRCS = main.cpp
DEPS = day1p1.hpp day1p2.hpp ../../lib/fileio.hpp
OBJ = day1p1.o day1p2.o ../../lib/fileio.o

%.o: %.cpp $(DEPS)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

day1: $(OBJ)
	$(CXX) $(SRCS) -o $@ $^ $(CXXFLAGS)

run:
	./day1

clean:
	rm day1 $(OBJ)
