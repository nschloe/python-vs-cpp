#include <limits>
#include <random>
#include <chrono>
#include <iostream>


int main() {
  const int r = 100;

  std::random_device rd;
  std::mt19937 e2(rd());
  std::uniform_real_distribution<> dist(0, 1);

  for (int pow = 0; pow < 27; pow++) {
    const int n = std::pow(2, pow);

    // init vectors
    std::vector<double> u(n);
    std::vector<double> v(n);
    for (int i=0; i < n; i++) {
      u[i] = dist(e2);
      v[i] = dist(e2);
    }

    double cpu_time_used = std::numeric_limits<double>::max();
    for (int k = 0; k < r; k++) {
      auto t1 = std::chrono::high_resolution_clock::now();
      // Use the volatile keyword to prevent optimizing out away
      volatile double out = 0.0;
      for (int i=0; i < n; i++) {
        out += u[i] * v[i];
      }
      auto t2 = std::chrono::high_resolution_clock::now();
      auto time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);
      cpu_time_used = std::min(time_span.count(), cpu_time_used);
    }
    std::cout << n << " " << cpu_time_used << std::endl;;
  }
  return 0;
}
