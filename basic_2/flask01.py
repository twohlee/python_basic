from flask import Flask, render_template, request, redirect

import cx_Oracle as oci # pip install cx_oracle << 아나콘다 프롬포트3 켜서 이거 입력하고 엔터

#아이디/암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor = conn.cursor()

print(conn)

app = Flask(__name__)


# 페이지를 만듦 
@app.route("/")
def index():
    sql = "SELECT sum(MEMBER.AGE) FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(type(data))
    print(data)
    return "index page"


@app.route("/age")
def calAge():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall()
    sum = 0
    for i in data:
        a,b,c,d,e = i
        sum += d
    print(sum)
    return "Calculate Age"




    

# chrome 주소창에 /login 추가 입력 해줘야 실행됨
@app.route("/login", methods = ['GET']) # 여기서는 사용자 입장 
def login():
    return render_template('login.html') #login.html이라는 화면을 가져와서 보여달라는 의미 

@app.route("/login", methods = ['POST']) #여기서는 개발자 입장 
def login_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    #print("{}:{}:{}:{}".format(a,b,c,d))
    sql = 'INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)'


    
    cursor.execute(sql, id=a, pw=b, na=c, ag = d)
    conn.commit()


    # 오라클 DB접속

    # 추가하는 SQL문 작성 => INSERT, SELECT, UPDATE, DELETE 
    
    # SQL문 수행
     
    # DB에 값을 넣고
    print("login-post") # 여기서는 버튼 클릭해서 post하면, 콘솔 창에 login-post 라는 문구가 뜸 
    return redirect('/') # 127.0.0.1/ 크롬에서 입력한 것처럼 동작  


if __name__ == '__main__':
    app.run(debug=True)
 
