CXX = clang++
CXXFLAGS = -Wall -Werror -std=c++20

SRCS = main.cpp
DEPS = p1.hpp p2.hpp ../lib/fileio.hpp
OBJ = p1.o p2.o ../lib/fileio.o

%.o: %.cpp $(DEPS)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

exe: $(OBJ)
	$(CXX) $(SRCS) -o $@ $^ $(CXXFLAGS)

run:
	./exe

clean:
	rm exe $(OBJ)
