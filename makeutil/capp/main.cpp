#include <iostream>
#include <time.h>

int main(){
  time_t now = time(NULL);
  std::cout << "This is C++ app" << std::endl;
  std::cout << "Run time: " << now << std::endl;
  return 0;
}
