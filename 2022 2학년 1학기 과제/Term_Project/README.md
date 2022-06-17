ΩOhm PC 관리 프로그램

## 필수 기능
#### 1. 회원제로 운영
#### 2. PC방 방문 횟수에 따른 포인트 점수 또는 Advantage 기능 부여

## 추가 기능
#### 1. 시간제 - 남은 시간 확인 및 종료 10분, 5분 전 알림
#### 2. 회원 등급 관리
#### 3. 음식 주분 - 기존 PC방과 동일
#### 4. 손님이 카운터에 문의하기 위한 메신저 기능
#### 5. 제자리 결제(Ex: 시간 충전, 음식 주문 등)
#### 6. 자리이동 및 외출 또는 자리 비움, 예약, 퇴장
#### 7. 회원 가입 및 탈퇴

###### \<PC_Management.cpp\>
```c++
#define _CRT_SECURE_NO_WARNINGS
#define admin_id "ohm_admin"
#define admin_pw "ohm_716_admin"

#include "non_member.h"
#include <Windows.h>
#include <iostream>
#include "member.h"
#include <fstream>
#include <sstream>
#include <vector>
#include <ctime>

using namespace std;

time_t curTime = time(NULL);
struct tm* t = localtime(&curTime);

void Delete_Save_Data(); // 모든 데이터 삭제
void Read_Save_Data(vector<member>& m); // 데이터 불러오기
void Save_Members_Data(vector<member>& m); // 데이터 저장
void Grading_Members(vector<member>& m); // 회원 등급 설정
void Time_Set_Members(vector<member>& m); // 회원 시간 정렬
void Time_Pass_Members(vector<member>& m); // 회원 남은 시간 설정
void Time_Dispaly_Members(vector<member>& m); // 회원 남은 시간 출력
void Time_Display_non_Members(vector<n_member>& n); // 비회원 남은 시간 출력
void Get_Message_to_Admin(); // 카운터로 온 메신저 확인하기
void Get_Message(string id); // 카운터에서 온 메신저 확인하기
void Send_Message_to_Admin(string id); // 카운터로 메신저 보내기
void Send_Message(vector<member>& m); // 카운터에서 메신저 보내기
void Display_menu(); // 메뉴판 출력
void Order_Foods(string id); // 음식 주문하기
void Get_Order(); // 주문 확인하기
void Check_Reservation(vector<member>& m); // 예약 확인하기
void Request_For_Reservation(string id, vector<member>& m); // 예약 신청하기
int Get_Current_Year(); // 현재 년도 불러오기
int Get_Current_Month(); // 현재 월 불러오기
int Get_Current_Day(); // 현재 일 불러오기
int Get_Current_Hour(); // 현재 시 불러오기
int Get_Current_Min(); // 현재 분 불러오기
int Get_Current_Sec(); // 현재 초 불러오기
vector<string> split(string str, char Delimiter); // 특정 문자 기준 string 나누기
member new_Member(); // 신규 회원
n_member new_Non_Member(); // 신규 비회원

int main() {

	vector<member> u;
	vector<n_member> n_u;

	Read_Save_Data(u);
	Grading_Members(u);

home:

	string id_input, pw_input;
	bool admin_login = 0;
	bool login = 0;
	int login_cnt = 0;
	int state = 0;

	cout << "---------- ΩOhm PC ----------" << endl;
	cout << "1. 로그인" << endl;
	cout << "2. 회원가입" << endl;
	cout << "3. 회원탈퇴" << endl;
	cout << "4. 비회원 이용" << endl;
	cout << "5. 프로그램 종료" << endl;
	cout << ">> ";
	cin >> state;

	/*
	state 1 == 로그인
	state 2 == 회원가입
	state 3 == 비회원 이용
	state 4 == 프로그램 종료
	else == 유효하지 않은 선택지
	*/
	if (state == 1) { // 로그인

		do {

			system("cls");

			cout << "---------- ΩOhm PC Login ----------" << endl;
			cout << "ID: ";
			cin >> id_input;
			cout << "PW: ";
			cin >> pw_input;

			if (id_input == admin_id && pw_input == admin_pw) { // 관리자인가?
				cout << "관리자 로그인 성공." << endl;
				login = 1;
				admin_login = 1;
			}
			else {

				if (u.size() == 0) { // 회원 정보의 수가 0일 때 그냥 로그인 실패

					cout << "로그인 실패." << endl;
					login_cnt += 1;
					Sleep(1000);
					system("cls");

				}
				else { // 그게 아니라면 탐색

					for (int i = 0; i < u.size(); i++) {

						if (id_input == u[i].GetId() && pw_input == u[i].GetPw()) { // 있으면 로그인 성공

							cout << "로그인 성공." << endl;
							login = 1;

						}
						else if (i == u.size()) { // 똑같은 유저 없으면 로그인 실패

							cout << "로그인 실패." << endl;
							login_cnt += 1;
							Sleep(1000);
							system("cls");

						}

					}

				}

			}

			if (login_cnt == 5) { // 로그인 5회 실패할 경우 프로그램 종료

				cout << "로그인 5회 실패." << endl;
				cout << "프로그램을 종료합니다." << endl;
				Sleep(500);
				return 0;

			}

		} while (login == 0);
	}
	else if (state == 2) { // 회원가입 

		u.push_back(new_Member());
		Save_Members_Data(u);
		system("cls");
		goto home;

	}
	else if (state == 3) {

		string name, id, pw, buffer;

		cout << "---------- 회원 탈퇴 ----------" << endl;
		cout << "이름: ";
		cin >> name;
		cout << "ID: ";
		cin >> id;
		cout << "PW: ";
		cin >> pw;
		cout << "탈퇴하시겠습니까? (\"확인\" 입력)" << endl << ">> ";
		cin >> buffer;

		if (buffer == "확인") {

			for (int i = 0; i < u.size(); i++) {

				if (u[i].GetName() == name && u[i].GetId() == id) {
					u.erase(u.begin() + i);
					break;
				}

			}

		}
		else {

			cout << "확인 입력 실패." << endl;
			cout << "회원 탈퇴 취소." << endl;
			state = 0;
			goto home;

		}

	}
	else if (state == 4) { // 비회원 사용

		n_u.push_back(new_Non_Member());

	}
	else if (state == 5) { // 프로그램 종료

		cout << "프로그램을 종료합니다." << endl;
		Save_Members_Data(u);
		return 0;

	}
	else { // 의도되지 않은 선택지

		cout << "해당 선택지는 존재하지 않습니다." << endl;
		Sleep(500);
		system("cls");
		goto home;

	}

	system("cls");

	login_cnt = 0;

	if (admin_login == 1) { // 관리자 로그인 화면

		do {

			int sel;

			cout << "---------- ΩOhm PC 관리 프로그램 ----------" << endl;
			cout << "1. 회원 남은 시간 확인" << endl;
			cout << "2. 메신저 확인" << endl;
			cout << "3. 메신저 보내기" << endl;
			cout << "4. 주문 확인" << endl;
			cout << "5. 예약석 확인" << endl;
			cout << "6. 로그아웃" << endl;
			cout << ">> ";
			cin >> sel;

			if (sel == 1) {

				Time_Pass_Members(u);
				Time_Dispaly_Members(u);

			}
			else if (sel == 2) {

				Get_Message_to_Admin();

			}
			else if (sel == 3) {

				Send_Message(u);

			}
			else if (sel == 4) {

				Get_Order();

			}
			else if(sel == 5){

				Check_Reservation(u);

			}
			else if(sel == 6){

				admin_login = -1;

			}
			else {

				cout << "해당 선택지가 존재하지 않습니다." << endl;

			}

		} while (admin_login == 1);

	}
	else if (state == 4) { // 비회원 사용 화면

		do {

			int sel;

			cout << "---------- ΩOhm PC 사용자 화면 ----------" << endl;
			cout << "※비회원 이용자는 음식 주문 및 제자리 결제, 자리 이동 및 외출 또는 예약기능, 카운터 문의(메신저) 기능을 사용하실 수 없습니다." << endl;
			cout << "1. 남은 시간 확인" << endl;
			cout << "2. 로그아웃" << endl;
			cout << ">> ";
			cin >> sel;

			if (sel == 1) {

			}
			else if (sel == 2) {

				state = 0;

			}
			else {

				cout << "해당 선택지가 존재하지 않습니다." << endl;

			}

		} while (state != 0);

	}
	else if(state == 1) { // 회원 사용 화면

			cout << "---------- ΩOhm PC 사용자 화면 ----------" << endl;

	}

	if (admin_login == -1) {

		goto home;

	}

	return 0;

}

void Read_Save_Data(vector<member>& m) {

	ifstream readData("Member_Data.txt");

	if (readData.is_open()) {

		string first_line;
		string date_time;
		getline(readData, first_line);
		int n = stoi(first_line);
		getline(readData, date_time);

		if (n != 0) {

			for (int i = 0; i < n; i++) {

				string str;
				getline(readData, str);

				vector<string> result = split(str, ' ');
				vector<string> left_time = split(result[9], ':');

				member temp(result[0], result[1], result[2], result[3], result[4], stoi(result[5]), result[6], stoi(result[7]), stoi(result[8]), stoi(left_time[0]), stoi(left_time[1]), stoi(left_time[2]));
				
				m.push_back(temp);

			}

		}
		else {

			cout << "There is no data." << endl;

		}

	}
	else {
		
		cout << "There is no data." << endl;

	}

}

void Delete_Save_Data() {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << 0 << endl;
	outfile << "Warning, Clear." << endl;

}

void Save_Members_Data(vector<member>& m) {

	ofstream outfile("Member_Data.txt", ios_base::out);

	outfile << m.size() << endl;
	outfile << "프로그램 종료 시각 >> " << Get_Current_Year() << ":" << Get_Current_Month() << ":" << Get_Current_Day() << ":" << Get_Current_Hour() << ":" << Get_Current_Min() << ":" << Get_Current_Sec() << endl;

	for (int i = 0; i < m.size(); i++) {

		string buffer = m[i].GetName();
		buffer += " ";
		buffer += m[i].GetId();
		buffer += " ";
		buffer += m[i].GetPw();
		buffer += " ";
		buffer += m[i].GetTel();
		buffer += " ";
		buffer += m[i].GetEmail();
		buffer += " ";
		buffer += to_string(m[i].GetAge());
		buffer += " ";
		buffer += m[i].GetGrade();
		buffer += " ";
		buffer += to_string(m[i].GetPoint());
		buffer += " ";
		buffer += to_string(m[i].GetPayCnt());
		buffer += " ";
		buffer += to_string(m[i].GetLTH());
		buffer += ":";
		buffer += to_string(m[i].GetLTM());
		buffer += ":";
		buffer += to_string(m[i].GetLTS());
		outfile << buffer << endl;

	}

}

void Grading_Members(vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {

		if (m[i].GetPayCnt() > 10) {
			m[i].SetGrade("Silver");
		}
		else if(m[i].GetPayCnt() > 50) {
			m[i].SetGrade("Gold");
		}
		else if (m[i].GetPayCnt() > 100) {
			m[i].SetGrade("Platinum");
		}
		else if (m[i].GetPayCnt() > 200) {
			m[i].SetGrade("Diamond");
		}
		else if (m[i].GetPayCnt() > 400) {
			m[i].SetGrade("Master");
		}
		else if (m[i].GetPayCnt() > 800) {
			m[i].SetGrade("Challenger");
		}

	}

}

void Time_Set_Members(vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {

		int hour = m[i].GetLTH();
		int min = m[i].GetLTM();
		int sec = m[i].GetLTS();

		if (sec / 60 >= 1) {
			min += sec / 60;
			sec %= 60;
		}

		if (min / 60 >= 1) {
			hour += min / 60;
			min %= 60;
		}

	}

}

void Time_Pass_Members(vector<member>& m) {

	for (int i = 0; i < m.size(); i++) {

		long long int pass_hour = Get_Current_Hour() - m[i].GetSTH();
		long long int pass_min = Get_Current_Min() - m[i].GetSTM();
		long long int pass_sec = Get_Current_Sec() - m[i].GetSTS();

		long long int left_time = (m[i].GetLTH() * 3600) + (m[i].GetLTM() * 60) + m[i].GetLTS();
		long long int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((m[i].GetSTH() * 3600) + (m[i].GetSTM() * 60) + m[i].GetSTS());

		if (pass_time >= left_time) {

			m[i].DelSTH();
			m[i].DelSTM();
			m[i].DelSTS();
			m[i].DelLTH();
			m[i].DelLTM();
			m[i].DelLTS();

			cout << m[i].GetName() << "(" << m[i].GetId() << ")님의 사용 시간이 종료되었습니다." << endl;

		}

	}

}

void Time_Dispaly_Members(vector<member>& m) {

	cout << "<남은 시간>" << endl;

	for (int i = 0; i < m.size(); i++) {

		int pass_hour = Get_Current_Hour() - m[i].GetSTH();
		int pass_min = Get_Current_Min() - m[i].GetSTM();
		int pass_sec = Get_Current_Sec() - m[i].GetSTS();

		long long int left_time = (m[i].GetLTH() * 3600) + (m[i].GetLTM() * 60) + m[i].GetLTS();
		long long int pass_time = ((Get_Current_Hour() * 3600) + (Get_Current_Min() * 60) + Get_Current_Sec()) - ((m[i].GetSTH() * 3600) + (m[i].GetSTM() * 60) + m[i].GetSTS());

		long long int time = left_time - pass_time;
		
		cout << "id: " << m[i].GetId() << "  " << time / 3600 << ":" << (time % 3600) / 60 << time % 60 << endl;

	}

}

void Time_Display_non_Members(vector<n_member>& n) {



}

void Get_Message_to_Admin() {

	ifstream to_admin("To_Admin.txt");

	if (to_admin.is_open()) {

		string text;

		while (getline(to_admin, text)) {

			cout << text;

		}

	}
	else {

		cout << "There is no data." << endl;

	}

	to_admin.close();

}

void Get_Message(string id) {

	ifstream from_admin("From_Admin.txt");

	if (from_admin.is_open()) {

		string text;

		while (getline(from_admin, text)) {

			vector<string> buffer = split(text, ' ');

			if (buffer[0] == id) {

				cout << "admin: " << buffer[1] << endl;

			}

		}

	}
	else {

		cout << "There is no data." << endl;

	}

	from_admin.close();

}

void Send_Message_to_Admin(string id) {

	ofstream to_admin("To_Admin.txt", ios_base::app);

	string buffer;

	cout << ">> ";
	cin >> buffer;
	to_admin << id << " " << buffer << endl;

	to_admin.close();

}

void Send_Message(vector<member>& m) {

	ofstream from_admin("From_Admin.txt", ios_base::app);

	string buffer;
	int select = 0;

	do {

		cout << "보낼 사용자의 아이디를 선택하세요. (종료는 -1)" << endl;
		for (int i = 0; i < m.size(); i++) {
			cout << i + 1 << ". " << m[i].GetId() << endl;
		}
		cout << ">> ";
		cin >> select;

		cout << "<메시지 입력>" << endl;
		cout << ">> ";
		cin >> buffer;

		from_admin << m[select - 1].GetId() << " " << buffer << endl;

	} while (select != -1);
	

	from_admin.close();

}

void Display_menu() {

	cout << "---------- 메뉴판 ----------" << endl;
	cout << "<라면>" << endl;
	cout << "진라면(순)  진라면(맵)  신라면  신라면블랙  삼양라면  열라면  짜파게티  너구리  불닭볶음면  까르보불닭볶음면  진짬뽕" << endl;
	cout << "<컵밥>" << endl;
	cout << "치킨마요  불닭마요  참치마요  스팸마요  스팸참치  치킨스팸  불닭스팸  치킨불닭스팸마요" << endl;
	cout << "<치킨>" << endl;
	cout << "한마리치킨  반마리치킨  반반치킨  닭강정  (양념: 후라이드, 양념, 까르보, 간장, 마늘)" << endl;
	cout << "<음료 - 주류는 카운터에서 신분증 확인 후 만 19세 이상부터 주문 가능합니다.>" << endl;
	cout << "코카콜라  펩시  칠성사이다  스프라이트  환타오렌지  환타파인에플  참이슬  처음처럼  카스  테라" << endl;

}

void Order_Foods(string id) {

	ofstream order("order.txt", ios_base::app);

	string buffer;

	Display_menu();

	cout << endl << "주문 내용을 적어주세요." << endl << ">> ";
	cin >> buffer;

	order << id << buffer << endl;

	order.close();

}

void Get_Order() {

	ifstream order("Order.txt");

	string buffer;

	while (getline(order, buffer)) {

		cout << buffer << endl;

	}

	order.close();

	ofstream clean("Order.txt", ios_base::out);

	string clear = "";

	clean << clear;

	clean.close();

}

void Check_Reservation(vector<member>& m) {

	ifstream reservation("Reservation.txt");

	string buffer;

	while (getline(reservation, buffer)) {

		int accept;
		cout << buffer << endl;
		cout << "예약 허가 하시겠습니까?(yes = 1, no = 0)" << endl << ">> ";
		cin >> accept;
		if (accept == 1) {
			vector<string> result = split(buffer, ' ');
			for (int i = 0; i < m.size(); i++) {

				if (m[i].GetName() == result[0] && m[i].GetId() == result[1]) {
					m[i].SetReservation(stoi(result[2]));
					cout << "예약이 완료되었습니다." << endl;
					break;
				}

			}
		}
		else {

			cout << "예약을 거부하였습니다." << endl;

		}

	}

	reservation.close();

	string clean = "";
	ofstream reservation_end("Reservation.txt", ios_base::out);
	reservation_end << clean;
	reservation_end.close();

}

void Request_For_Reservation(string id, vector<member>& m) {

	ofstream reservation("Reservation.txt", ios_base::out);

	string buffer = "";
	string name, num;

	cout << "신청자의 이름과 좌석 번호를 입력하시오." << endl;
	cout << "이름: ";
	cin >> name;
	cout << "좌석 번호: ";
	cin >> num;

	buffer += name;
	buffer += " ";
	buffer += num;

	reservation << buffer << endl;

	reservation.close();

}

member new_Member() {

	string name, id, pw, email, tel;
	int age;

	cout << "---------- 회원가입 ----------" << endl;
	cout << "ID: ";
	cin >> id;
	cout << "PW: ";
	cin >> pw;
	cout << "이름: ";
	cin >> name;
	cout << "나이: ";
	cin >> age;
	cout << "전화번호: ";
	cin >> tel;
	cout << "e-mail: ";
	cin >> email;

	member temp(name, id, pw, tel, email, age);

	cout << "회원가입에 성공했습니다." << endl;

	return temp;

}

n_member new_Non_Member() {

	string name, tel;
	int age;

	cout << "---------- 비회원 필수 정보 입력 ----------" << endl;
	cout << "이름: ";
	cin >> name;
	cout << "나이: ";
	cin >> age;
	cout << "전화번호: ";
	cin >> tel;

	n_member temp(name, tel, age);

	return temp;

}

vector<string> split(string str, char Delimiter) {
	istringstream iss(str);
	string buffer;

	vector<string> result;

	while (getline(iss, buffer, Delimiter)) {
		result.push_back(buffer);
	}

	return result;
}

int Get_Current_Year() {

	return (t->tm_year) + 1900;

}

int Get_Current_Month() {

	return (t->tm_mon) + 1;

}

int Get_Current_Day() {

	return t->tm_mday;

}

int Get_Current_Hour() {

	return t->tm_hour;

}

int Get_Current_Min() {

	return t->tm_min;

}

int Get_Current_Sec() {

	return t->tm_sec;

}
```

###### \<member.h\>
```c++
#pragma once

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class member {

	string name, id, pw, email, tel, grade;
	int age, point, pay_cnt;
	int left_time_hour, left_time_min, left_time_sec;
	int start_time_hour, start_time_min, start_time_sec;
	int reservation;

public:

	member() {}
	member(string _name, string _id, string _pw, string _tel, string _email, int _age, string _grade = "Bronze", int _point = 0, int _pay_cnt = 0, int _start_time_hour = -1, int _start_time_min = -1, int _start_time_sec = -1, int _left_time_hour = -1, int _left_time_min = -1, int _left_time_sec = -1, int _reservation = -1) {
		name = _name;
		tel = _tel;
		id = _id;
		pw = _pw;
		email = _email;
		age = _age;
		grade = _grade;
		point = _point;
		pay_cnt = _pay_cnt;
		start_time_hour = _start_time_hour;
		start_time_min = _start_time_min;
		start_time_sec = _start_time_sec;
		left_time_hour = _left_time_hour;
		left_time_min = _left_time_min;
		left_time_sec = _left_time_sec;
		reservation = _reservation;
	}
	member(const member& u) {
		name = u.name;
		tel = u.tel;
		id = u.id;
		pw = u.pw;
		email = u.email;
		age = u.age;
		grade = u.grade;
		point = u.point;
		pay_cnt = u.pay_cnt;
		start_time_hour = u.start_time_hour;
		start_time_min = u.start_time_min;
		start_time_sec = u.start_time_sec;
		left_time_hour = u.left_time_hour;
		left_time_min = u.left_time_min;
		left_time_sec = u.left_time_sec;
		reservation = u.reservation;
	}
	~member() {
		name.clear();
		tel.clear();
		id.clear();
		pw.clear();
		email.clear();
		grade.clear();
		start_time_hour = -1;
		start_time_min = -1;
		start_time_sec = -1;
		left_time_hour = -1;
		left_time_min = -1;
		left_time_sec = -1;
		reservation = -1;
		pay_cnt = 0;
		age = 0;
		point = 0;
	}

	void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "ID: " << id << endl;
		cout << "PW: " << pw << endl;
		cout << "회원 등급: " << grade << endl;
		cout << "적립 포인트: " << point << endl;
		cout << "Tel: " << tel << endl;
		cout << "E-mail: " << email << endl;
		cout << "남은 시간: " << left_time_hour << ":" << left_time_min << ":" << left_time_sec << endl;
	}

	string GetName() { return name; }
	string GetTel() { return tel; }
	string GetId() { return id; }
	string GetPw() { return pw; }
	string GetEmail() { return email; }
	string GetGrade() { return grade; }
	int GetAge() { return age; }
	int GetPoint() { return point; }
	int GetPayCnt() { return pay_cnt; }
	int GetSTH() { return start_time_hour; }
	int GetSTM() { return start_time_min; }
	int GetSTS() { return start_time_sec; }
	int GetLTH() { return left_time_hour; }
	int GetLTM() { return left_time_min; }
	int GetLTS() { return left_time_sec; }
	int GetReservation() { return reservation; }

	void SetId(string _id) { id = _id; }
	void SetPw(string _pw) { pw = _pw; }
	void SetEmail(string _email) { email = _email; }
	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetGrade(string _grade) { grade = _grade; }
	void SetAge(int _age) { age = _age; }
	void SetPoint(int _point) { point = _point; }
	void SetPayCnt(int _pay_cnt) { pay_cnt = _pay_cnt; }
	void SetSTH(int _start_time_hour) { start_time_hour = _start_time_hour; }
	void SetSTM(int _start_time_min) { start_time_min = _start_time_min; }
	void SetSTS(int _start_time_sec) { start_time_sec = _start_time_sec; }
	void SetLTH(int _left_time_hour) { left_time_hour = _left_time_hour; }
	void SetLTM(int _left_time_min) { left_time_min = _left_time_min; }
	void SetLTS(int _left_time_sec) { left_time_sec = _left_time_sec; }
	void SetReservation(int _reservation) { reservation = _reservation; }

	void DelId() { id.clear(); }
	void DelPw() { pw.clear(); }
	void DelEmail() { email.clear(); }
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelGrade() { grade.clear(); }
	void DelAge() { age = 0; }
	void DelPoint() { point = 0; }
	void DelPayCnt() { pay_cnt = 0; }
	void DelSTH() { start_time_hour = -1; }
	void DelSTM() { start_time_hour = -1; }
	void DelSTS() { start_time_sec = -1; }
	void DelLTH() { left_time_hour = -1; }
	void DelLTM() { left_time_min = -1; }
	void DelLTS() { left_time_sec = -1; }
	void DelReservation() { reservation = -1; }

};
```

###### \<non_member.h\>
```c++
#pragma once

#include <iostream>
#include <string>

using namespace std;

class n_member {

	string name, tel;
	int age;
	int left_time_hour, left_time_min, left_time_sec;
	int start_time_hour, start_time_min, start_time_sec;

public:

	n_member() {}
	n_member(string _name, string _tel, int _age) {
		name = _name;
		tel = _tel;
		age = _age;
	}
	n_member(const n_member& u) {
		name = u.name;
		tel = u.tel;
		age = u.age;
	}
	~n_member() {
		name.clear();
		tel.clear();
		start_time_hour = -1;
		start_time_min = -1;
		start_time_sec = -1;
		left_time_hour = -1;
		left_time_min = -1;
		left_time_sec = -1;
		age = 0;
	}

	virtual void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "Tel: " << tel << endl;
	}

	string GetName() { return name; }
	string GetTel() { return tel; }
	int GetAge() { return age; }
	int GetSTH() { return start_time_hour; }
	int GetSTM() { return start_time_min; }
	int GetSTS() { return start_time_sec; }
	int GetLTH() { return left_time_hour; }
	int GetLTM() { return left_time_min; }
	int GetLTS() { return left_time_sec; }

	void SetName(string _name) { name = _name; }
	void SetTel(string _tel) { tel = _tel; }
	void SetAge(int _age) { age = _age; }
	void SetSTH(int _start_time_hour) { start_time_hour = _start_time_hour; }
	void SetSTM(int _start_time_min) { start_time_min = _start_time_min; }
	void SetSTS(int _start_time_sec) { start_time_sec = _start_time_sec; }
	void SetLTH(int _left_time_hour) { left_time_hour = _left_time_hour; }
	void SetLTM(int _left_time_min) { left_time_min = _left_time_min; }
	void SetLTS(int _left_time_sec) { left_time_sec = _left_time_sec; }

	
	void DelName() { name.clear(); }
	void DelTel() { tel.clear(); }
	void DelAge() { age = 0; }
	void DelSTH() { start_time_hour = -1; }
	void DelSTM() { start_time_hour = -1; }
	void DelSTS() { start_time_sec = -1; }
	void DelLTH() { left_time_hour = -1; }
	void DelLTM() { left_time_min = -1; }
	void DelLTS() { left_time_sec = -1; }

};
```
