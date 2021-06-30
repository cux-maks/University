## <js에서 파이썬 호출 및 연동>

### 1. 기본 사용법
### 2. 파이썬 파일 실행
### 3. 파이썬 함수 실행
### 4. 파이썬 함수에 인수 전달



#### <기본 사용법>
```js
# 1. child_process모듈의 spawn 취득
# 2. spawn 을 통해 “python 파이썬파일.py”명령어 실행
# 3. stdout의 ‘data’이벤트리스너로 실행결과를 받는다.
# 4. 에러 발생 시 stderr의 ‘data’이벤트리스너로 실행 결과를 받는다.
const spawn = require(‘child_process’).spawn;

const result = spawn(‘python’, [‘파이썬파일.py’], 매개변수1, 매개변수2, ...);

result.stdout.on(‘data’, function(data){ console.log(data.toString()); });

result.stderr.on(‘data’, function(data){ consoe.log(data.toString()); )};
```

```js
const result = spawn(‘python’, [‘파이썬파일명.py’, 매개변수1, 매개변수2, ....]);
```
- -> 이 코드는 파이썬 코드를 실행하는 것과 동일하게 동한다.









#### <파이썬 파일 실행>

```python
# print.py
print(‘Hello World!’)
```
```js
const spawn = require(‘child_process;).spawn;

const result = spawn(‘python’, [‘print.py’]);

result.stdout.on(‘data’, function(data) { console.log(data.toString()); });

result stderr.on(‘data’, function(data) { console.log(data.toString()); });
```
- -> toString()이 없다면 Buffer 형태로 출력됨.

#### <파이썬 함수 실행>

```python
# function_print.py 파일 
def getValue(): 
	print ("value") 
if __name__ == '__main__':
	getValue()
```

```js
const spawn = require('child_process').spawn;

const result_01 = spawn('python', ['function_print.py'], );

result_01.stdout.on('data', (result)=>{ console.log(result.toString()); });
```
