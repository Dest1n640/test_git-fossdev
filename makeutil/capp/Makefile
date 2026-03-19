.PHONY: another-app

# Might bw correct, but `build` and `app` are diffrent
build:
	g++ -o app main.cpp


# correct no PHONY
app: main.cpp
	g++ -o app main.cpp

# incorrect listed in PHONY
another-app: main.cpp
	g++ -o another-app main.cpp
