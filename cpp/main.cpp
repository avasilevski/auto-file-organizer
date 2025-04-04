#include <iostream>
#include <fstream>
#include <chrono>
#include <ctime>
#include <filesystem>
using namespace std;

namespace fs = filesystem;

void log(const string& message, const string& filepath = "../logs/log.txt"){
    fs::create_directories("../logs");
    ofstream logFile(filepath, ios::app);
    if (logFile.is_open()) {
        auto now = chrono::system_clock::now();
        time_t timeNow = chrono::system_clock::to_time_t(now);
        char timeStr[100];
        strftime(timeStr, sizeof(timeStr), "[%Y-%m-%d %H:%M:%S]", localtime(&timeNow));  
        logFile << timeStr << " " << message << '\n';
        logFile.close();
    } else {
        cerr << "Failed to open log file.\n";
    }
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        string msg;
        for (int i = 1; i < argc; ++i) {
            msg += argv[i];
            if (i != argc - 1) msg += " ";
        }
        log(msg);
    } else {
        cerr << "No log message provided.\n";
    }
    return 0;
}