뭉치 PC 관리 프로그램

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
#include <iostream>
#include "member.h"

using namespace std;

int main() {

	

	return 0;

}
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

public:

	n_member() {}
	n_member(string _name, string _tel, int _age) {
		name = _name;
		tel = _tel;
		age = _age;
	}
	n_member(n_member& u) {
		name = u.name;
		tel = u.tel;
		age = u.age;
	}
	~n_member() {
		name.clear();
		tel.clear();
		age = 0;
	}

	virtual void DispInfo() {
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "Tel: " << tel << endl;
	}

	virtual string GetName() { return name; }
	virtual string GetTel() { return tel; }
	virtual int GetAge() { return age; }

	virtual void SetName(string _name) { name = _name; }
	virtual void SetTel(string _tel) { tel = _tel; }
	virtual void SetAge(int _age) { age = _age; }

	virtual void DelName() { name.clear(); }
	virtual void DelTel() { tel.clear(); }
	virtual void DelAge() { age = 0; }

};
```

###### \<member.h\>
```c++
#pragma once

#include <iostream>
#include <string>
#include "non_member.h"

using namespace std;

class member : public n_member {

	n_member own;
	string id, pw, email;

public:

	member() {}
	member(string _name, string _id, string _pw, string _tel, string _email, int _age):own(_name, _tel, _age) {
		id = _id;
		pw = _pw;
		email = _email;
	}
	member(member& u) {
		own.SetName(u.GetName());
		own.SetTel(u.GetTel());
		own.SetAge(u.GetAge());
		id = u.id;
		pw = u.pw;
		email = u.email;
	}
	~member() {
		id.clear();
		pw.clear();
		email.clear();
	}

	void DispInfo() {
		cout << "이름: " << own.GetName() << endl;
		cout << "나이: " << own.GetAge() << endl;
		cout << "ID: " << id << endl;
		cout << "PW: " << pw << endl;
		cout << "Tel: " << own.GetTel() << endl;
		cout << "E-mail: " << email << endl;
	}

	string GetName() { return own.GetName(); }
	string GetTel() { return own.GetTel(); }
	string GetId() { return id; }
	string GetPw() { return pw; }
	string GetEmail() { return email; }
	int GetAge() { return own.GetAge(); }

	void SetId(string _id) { id = _id; }
	void SetPw(string _pw) { pw = _pw; }
	void SetEmail(string _email) { email = _email; }
	void SetName(string _name) { own.SetName(_name); }
	void SetTel(string _tel) { own.SetTel(_tel); }
	void SetAge(int _age) { own.SetAge(_age); }

	void DelId() { id.clear(); }
	void DelPw() { pw.clear(); }
	void DelEmail() { email.clear(); }
	void DelName() { own.DelName(); }
	void DelTel() { own.DelTel(); }
	void DelAge() { own.DelAge(); }

};
```
