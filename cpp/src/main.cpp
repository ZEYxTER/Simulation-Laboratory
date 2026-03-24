#include <iostream>
#include <ctime> // include time to logs

int main(int argc, char *argv[]){
    time_t timestamp;
    time(&timestamp);
    std::cout << ctime(&timestamp) << std::endl;
}