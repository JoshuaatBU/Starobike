#include <iostream>
#include <string>
#include <SFML/Graphics.hpp>
#include <fstream>
#include <cmath>
using std::cout;
using std::string;
using std::__cxx11::to_string;
using std::ifstream;

int main() {
  string line, sub;
  ifstream MyReadFile("fake_GPS_data.txt");
  int position, i;
  double coordinates [4], x_bike_double, y_bike_double;

// Set Window
  sf::RenderWindow window(sf::VideoMode(800, 800), "wcholden@bu.edu");
  window.clear();
  window.setFramerateLimit(4);

// Build Car Rectangle
  sf::RectangleShape car(sf::Vector2f(40, 100));
  car.setFillColor(sf::Color::Blue);
  car.setPosition(380, 350);

// Build Lane Rectangles
  sf::RectangleShape left_lane(sf::Vector2f(50, 800));
  left_lane.setPosition(0, 0);
  left_lane.setFillColor(sf::Color::Green);
  sf::RectangleShape right_lane(sf::Vector2f(300, 800));
  right_lane.setPosition(500, 0);
  right_lane.setFillColor(sf::Color::Green);

// Build Bike Rectangle
  sf::RectangleShape bike(sf::Vector2f(10, 50));
  bike.setFillColor(sf::Color::Red);
  int x_bike, y_bike;

// Display Text
  sf::Text msg;
  sf::Font font;
  font.loadFromFile("/usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf");
  msg.setFont(font);
  msg.setCharacterSize(32);
  msg.setPosition(525, 50);
  string msg_str;

  double dist;







// Acquire GPS Data
  while (getline (MyReadFile, line)) {
    for (i = 0; i < 4; i++) {
      position = line.find(", ");
      coordinates[i] = stod(line.substr(0, position));
      line = line.substr(position + 2);
    }

    x_bike_double = 111139.0 * (coordinates[1] - coordinates[3]);
    y_bike_double = 111139.0 * (coordinates[0] - coordinates[2]);

    dist = pow((pow(x_bike_double, 2) + pow(y_bike_double, 2)), 0.5);
    msg_str = "Alert: \nBike " + to_string(dist) + "m \naway";
    msg.setString(msg_str);


    cout << "bike is " << floor(dist) << " meters away \n";

    x_bike = 400 + (5*x_bike_double);
    y_bike = 400 + (20*y_bike_double);


    bike.setPosition(x_bike, y_bike);

    sf::Event event;
    while (window.pollEvent(event)) {
      if (event.type == sf::Event::Closed)
        window.close();
    }

    window.clear();
    window.draw(left_lane);
    window.draw(right_lane);

    if (dist < 12.0) {
      window.draw(msg);
      msg.setFillColor(sf::Color::Red);
    }
    else if (dist < 16.0) {
      window.draw(msg);
      msg.setFillColor(sf::Color::Black);
    }


    window.draw(car);
    window.draw(bike);
    window.display();





  }

// Close the file
  MyReadFile.close();


  return 0;
}