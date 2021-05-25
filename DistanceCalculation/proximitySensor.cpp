#include <iostream>
#include <string>
#include <SFML/Graphics.hpp>
#include <fstream>
#include <cmath>
using std::cout;
using std::string;
using std::__cxx11::to_string;
using std::ifstream;


void read_serial();

void parse_serial();

int main() {
  string line, sub;
  ifstream MyReadFile("fake_GPS_data.txt");
  int position, i;
  double coordinates [4], x_bike_double, y_bike_double;

// Set Window
  sf::RenderWindow window(sf::VideoMode(400, 400), "wcholden@bu.edu");
  window.clear();
  window.setFramerateLimit(1);

// Build Car Rectangle
  sf::RectangleShape car(sf::Vector2f(40, 100));
  car.setFillColor(sf::Color::Blue);
  car.setPosition(180, 150);

// Build Directional
  sf::RectangleShape directional_horizontal(sf::Vector2f(100, 10));
  sf::RectangleShape directional_vertical(sf::Vector2f(10, 100));

// Display Text
  sf::Text msg;
  sf::Font font;
  font.loadFromFile("/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf");
  msg.setFont(font);
  msg.setCharacterSize(32);
  msg.setPosition(250, 50);
  string msg_str;
  double dist;







// Acquire GPS Data
  while (getline (MyReadFile, line)) {
    for (i = 0; i < 4; i++) {
      position = line.find(", ");
      coordinates[i] = stod(line.substr(0, position));
      line = line.substr(position + 2);
    }

    x_bike_double = 111139.0 * (coordinates[3] - coordinates[1]);
    y_bike_double = 111139.0 * (coordinates[2] - coordinates[0]);

    dist = pow((pow(x_bike_double, 2) + pow(y_bike_double, 2)), 0.5);
    msg_str = "Alert: \nBike " + to_string(dist) + "m \naway";
    msg.setString(msg_str);


    cout << "bike is " << dist << " meters away \n";


    if ((x_bike_double > 0) & (y_bike_double > 0)) { 
      directional_horizontal.setPosition(300, 0);
      directional_vertical.setPosition(390, 0);
    } else if ((x_bike_double < 0) & (y_bike_double > 0)) { // top left 
      directional_horizontal.setPosition(0, 0);
      directional_vertical.setPosition(0, 0);
    } else if ((x_bike_double < 0) & (y_bike_double < 0)) { // 
      directional_horizontal.setPosition(0, 390);
      directional_vertical.setPosition(0, 300);
    } else if ((x_bike_double > 0) & (y_bike_double < 0)) {
      directional_horizontal.setPosition(300, 390);
      directional_vertical.setPosition(390, 300);
    } else if ((x_bike_double > 0) & (y_bike_double == 0)) {
      directional_horizontal.setPosition(300, 195);
      directional_vertical.setPosition(390, 150);
    } else if ((x_bike_double < 0) & (y_bike_double == 0)) {
      directional_horizontal.setPosition(0, 195);
      directional_vertical.setPosition(0, 150);
    } else if ((x_bike_double == 0) & (y_bike_double < 0)) {
      directional_horizontal.setPosition(150, 390);
      directional_vertical.setPosition(390, 150);
    } else if ((x_bike_double == 0) & (y_bike_double > 0)) {
      directional_horizontal.setPosition(150, 0);
      directional_vertical.setPosition(195, 0);
    }


    sf::Event event;
    while (window.pollEvent(event)) {
      if (event.type == sf::Event::Closed)
        window.close();
    }

    window.clear();

    if (dist < 12.0) {
      msg.setFillColor(sf::Color::Red);
      directional_horizontal.setFillColor(sf::Color::Red);
      directional_vertical.setFillColor(sf::Color::Red);
      window.draw(msg);
      window.draw(directional_horizontal);
      window.draw(directional_vertical);
    } else if (dist < 16.0) {
      msg.setFillColor(sf::Color::Yellow);
      directional_horizontal.setFillColor(sf::Color::Yellow);
      directional_vertical.setFillColor(sf::Color::Yellow);
      window.draw(msg);
      window.draw(directional_horizontal);
      window.draw(directional_vertical);
    }


    window.draw(car);
    window.display();


  }

// Close the file
  MyReadFile.close();


  return 0;
}