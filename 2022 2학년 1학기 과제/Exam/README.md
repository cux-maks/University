## Problem 1

![문제](https://user-images.githubusercontent.com/82014995/172813324-cf70fc41-5746-4cbb-bafe-45d7ff036bd7.png)


```c++
#include <iostream>

using std::cout;
using std::endl;

using std::ostream;

class Vector {

	double x, y, z;

public:

	Vector() {}
	Vector(double _x, double _y, double _z) {
		x = _x;
		y = _y;
		z = _z;
	}
	Vector(Vector& v) {
		x = v.x;
		y = v.y;
		z = v.z;
	}
	~Vector() {}

	void SetX(double _x) { x = _x; }
	void SetY(double _y) { y = _y; }
	void SetZ(double _z) { z = _z; }

	void Display() {
		cout << "(" << x << ", " << y << ", " << z << ")" << endl;
	}

	Vector operator+(const Vector& v) {

		Vector temp;

		temp.SetX(x + v.x);
		temp.SetY(y + v.y);
		temp.SetZ(z + v.z);

		return temp;

	}

	Vector operator-(const Vector& v) {

		Vector temp;

		temp.SetX(x - v.x);
		temp.SetY(y - v.y);
		temp.SetZ(z - v.z);

		return temp;

	}

	Vector operator*(const double _k) {

		Vector temp;

		temp.SetX(x * _k);
		temp.SetY(y * _k);
		temp.SetZ(z * _k);

		return temp;

	}


	double operator*(const Vector &v) {

		double temp;

		temp = (x * v.x) + (y * v.y) + (z * v.z);

		return temp;

	}

	Vector operator%(const Vector &v) {

		Vector temp;

		temp.SetX(y*(v.z) - z*(v.y));
		temp.SetY(z*(v.x) - x*(v.z));
		temp.SetZ(x*(v.y) - y*(v.x));

		return temp;

	}

	Vector operator-() {

		Vector temp;
		
		temp.SetX((-1) * x);
		temp.SetY((-1) * y);
		temp.SetZ((-1) * z);

		return temp;

	}

	friend ostream& operator<<(ostream& os, const Vector& v) {
		os << "(" << v.x << ", " << v.y << ", " << v.z << ")" << endl;
		return os;
	}

};

int main() {

	Vector U(3.2, 5.3, 2.5), V(6.0, 7.0, 8.0);
	double k = 2.3;

	cout << "Vector U is ";
	U.Display();
	cout << "Vector V is ";
	V.Display();

	Vector R;

	R = U + V;
	cout << "Vector U + V = " << R << endl;

	R = U - V;
	cout << "Vector U - V = " << R << endl;

	/*R = k * V;
	cout << "Vector k * V = " << R << endl;*/

	R = V * k;
	cout << "Vector V * k = " << R << endl;

	R = -V;
	cout << "Vector -V = " << R << endl;

	double temp = U * V;
	cout << "Vector U * V = " << temp << endl << endl;

	R = U % V;
	cout << "Vector U % V = " << R << endl;

	return 0;

}
```

## Problem 2

![문제](https://user-images.githubusercontent.com/82014995/172813414-0d14a7d5-19ca-4553-9177-129269c7b13f.jpg)

```c++
#include <iostream>
#include <math.h>

const double PI = 3.14159;
const double g = 9.81;

using namespace std;

double DegreeToRadian(double d) {
	return (d * PI) / 180;
}

class Cannonball {

	double X_Position, Y_Position = 0;
	double angle, time_interval;
	double X_velocity, Y_velocity;

public:

	Cannonball() {}
	Cannonball(double x = 0) { X_Position = x; }
	~Cannonball() {}

	void move(double time_interval) {

		X_Position = (X_velocity * time_interval);
		Y_Position = (Y_velocity * time_interval - 0.5 * g * time_interval * time_interval);

	}

	void Display_Position() {
		cout << "X_Position: " << X_Position << ", Y_Position: " << Y_Position << endl;
	}

	void Shoot(double _angle, double _init_velocity, double time_interval = 0.1) {

		X_velocity = _init_velocity * cos(DegreeToRadian(_angle));
		Y_velocity = _init_velocity * sin(DegreeToRadian(_angle));

		for (double i = 0; i - time_interval <= 2*(Y_velocity / g); i += time_interval) {

			this->move(i);
			this->Display_Position();

		}

	}

};

int main() {

	cout << "초기 발사 각도: 45" << endl << "초기 속도: 30" << endl;

	double Angle = 45;
	double Init_velocity = 30;

	Cannonball Ball_1(0);
	Ball_1.Shoot(Angle, Init_velocity);

	cout << "---------------------------------------------------" << endl;

	cout << "초기 발사 각도: 60" << endl << "초기 속도: 50" << endl;

	Angle = 60;
	Init_velocity = 50;

	Cannonball Ball_2(0);
	Ball_2.Shoot(Angle, Init_velocity);

	cout << "---------------------------------------------------" << endl;

	return 0;

}

/*

초기 발사 각도: 45
초기 속도: 30
X_Position: 0, Y_Position: 0
X_Position: 2.12132, Y_Position: 2.07227
X_Position: 4.24264, Y_Position: 4.04644
X_Position: 6.36397, Y_Position: 5.92251
X_Position: 8.48529, Y_Position: 7.70048
X_Position: 10.6066, Y_Position: 9.38034
X_Position: 12.7279, Y_Position: 10.9621
X_Position: 14.8493, Y_Position: 12.4458
X_Position: 16.9706, Y_Position: 13.8314
X_Position: 19.0919, Y_Position: 15.1188
X_Position: 21.2132, Y_Position: 16.3082
X_Position: 23.3345, Y_Position: 17.3995
X_Position: 25.4559, Y_Position: 18.3926
X_Position: 27.5772, Y_Position: 19.2877
X_Position: 29.6985, Y_Position: 20.0847
X_Position: 31.8198, Y_Position: 20.7835
X_Position: 33.9411, Y_Position: 21.3843
X_Position: 36.0625, Y_Position: 21.887
X_Position: 38.1838, Y_Position: 22.2915
X_Position: 40.3051, Y_Position: 22.598
X_Position: 42.4264, Y_Position: 22.8064
X_Position: 44.5478, Y_Position: 22.9166
X_Position: 46.6691, Y_Position: 22.9288
X_Position: 48.7904, Y_Position: 22.8429
X_Position: 50.9117, Y_Position: 22.6589
X_Position: 53.033, Y_Position: 22.3767
X_Position: 55.1544, Y_Position: 21.9965
X_Position: 57.2757, Y_Position: 21.5182
X_Position: 59.397, Y_Position: 20.9417
X_Position: 61.5183, Y_Position: 20.2672
X_Position: 63.6397, Y_Position: 19.4946
X_Position: 65.761, Y_Position: 18.6238
X_Position: 67.8823, Y_Position: 17.655
X_Position: 70.0036, Y_Position: 16.5881
X_Position: 72.1249, Y_Position: 15.423
X_Position: 74.2463, Y_Position: 14.1599
X_Position: 76.3676, Y_Position: 12.7987
X_Position: 78.4889, Y_Position: 11.3394
X_Position: 80.6102, Y_Position: 9.78192
X_Position: 82.7315, Y_Position: 8.12639
X_Position: 84.8529, Y_Position: 6.37276
X_Position: 86.9742, Y_Position: 4.52103
X_Position: 89.0955, Y_Position: 2.5712
X_Position: 91.2168, Y_Position: 0.523264
X_Position: 93.3382, Y_Position: -1.62277
---------------------------------------------------

초기 발사 각도: 60
초기 속도: 50
X_Position: 0, Y_Position: 0
X_Position: 2.5, Y_Position: 4.28107
X_Position: 5.00001, Y_Position: 8.46405
X_Position: 7.50001, Y_Position: 12.5489
X_Position: 10, Y_Position: 16.5357
X_Position: 12.5, Y_Position: 20.4244
X_Position: 15, Y_Position: 24.2149
X_Position: 17.5, Y_Position: 27.9074
X_Position: 20, Y_Position: 31.5018
X_Position: 22.5, Y_Position: 34.9981
X_Position: 25, Y_Position: 38.3962
X_Position: 27.5, Y_Position: 41.6963
X_Position: 30, Y_Position: 44.8983
X_Position: 32.5, Y_Position: 48.0022
X_Position: 35.0001, Y_Position: 51.0079
X_Position: 37.5001, Y_Position: 53.9156
X_Position: 40.0001, Y_Position: 56.7252
X_Position: 42.5001, Y_Position: 59.4367
X_Position: 45.0001, Y_Position: 62.05
X_Position: 47.5001, Y_Position: 64.5653
X_Position: 50.0001, Y_Position: 66.9825
X_Position: 52.5001, Y_Position: 69.3016
X_Position: 55.0001, Y_Position: 71.5225
X_Position: 57.5001, Y_Position: 73.6454
X_Position: 60.0001, Y_Position: 75.6702
X_Position: 62.5001, Y_Position: 77.5969
X_Position: 65.0001, Y_Position: 79.4254
X_Position: 67.5001, Y_Position: 81.1559
X_Position: 70.0001, Y_Position: 82.7883
X_Position: 72.5001, Y_Position: 84.3226
X_Position: 75.0001, Y_Position: 85.7587
X_Position: 77.5001, Y_Position: 87.0968
X_Position: 80.0001, Y_Position: 88.3368
X_Position: 82.5001, Y_Position: 89.4787
X_Position: 85.0001, Y_Position: 90.5224
X_Position: 87.5001, Y_Position: 91.4681
X_Position: 90.0001, Y_Position: 92.3157
X_Position: 92.5001, Y_Position: 93.0652
X_Position: 95.0001, Y_Position: 93.7165
X_Position: 97.5001, Y_Position: 94.2698
X_Position: 100, Y_Position: 94.725
X_Position: 102.5, Y_Position: 95.0821
X_Position: 105, Y_Position: 95.341
X_Position: 107.5, Y_Position: 95.5019
X_Position: 110, Y_Position: 95.5647
X_Position: 112.5, Y_Position: 95.5294
X_Position: 115, Y_Position: 95.3959
X_Position: 117.5, Y_Position: 95.1644
X_Position: 120, Y_Position: 94.8348
X_Position: 122.5, Y_Position: 94.4071
X_Position: 125, Y_Position: 93.8812
X_Position: 127.5, Y_Position: 93.2573
X_Position: 130, Y_Position: 92.5353
X_Position: 132.5, Y_Position: 91.7152
X_Position: 135, Y_Position: 90.7969
X_Position: 137.5, Y_Position: 89.7806
X_Position: 140, Y_Position: 88.6662
X_Position: 142.5, Y_Position: 87.4537
X_Position: 145, Y_Position: 86.143
X_Position: 147.5, Y_Position: 84.7343
X_Position: 150, Y_Position: 83.2275
X_Position: 152.5, Y_Position: 81.6226
X_Position: 155, Y_Position: 79.9195
X_Position: 157.5, Y_Position: 78.1184
X_Position: 160, Y_Position: 76.2192
X_Position: 162.5, Y_Position: 74.2219
X_Position: 165, Y_Position: 72.1264
X_Position: 167.5, Y_Position: 69.9329
X_Position: 170, Y_Position: 67.6413
X_Position: 172.5, Y_Position: 65.2516
X_Position: 175, Y_Position: 62.7637
X_Position: 177.5, Y_Position: 60.1778
X_Position: 180, Y_Position: 57.4938
X_Position: 182.5, Y_Position: 54.7117
X_Position: 185, Y_Position: 51.8314
X_Position: 187.5, Y_Position: 48.8531
X_Position: 190, Y_Position: 45.7767
X_Position: 192.5, Y_Position: 42.6022
X_Position: 195, Y_Position: 39.3295
X_Position: 197.5, Y_Position: 35.9588
X_Position: 200, Y_Position: 32.49
X_Position: 202.5, Y_Position: 28.9231
X_Position: 205, Y_Position: 25.258
X_Position: 207.5, Y_Position: 21.4949
X_Position: 210, Y_Position: 17.6337
X_Position: 212.5, Y_Position: 13.6744
X_Position: 215, Y_Position: 9.61693
X_Position: 217.5, Y_Position: 5.46141
X_Position: 220, Y_Position: 1.20778
X_Position: 222.5, Y_Position: -3.14394
---------------------------------------------------

*/
```
