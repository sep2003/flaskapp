from flask import Flask,request,render_template,redirect
import json_1 

app=Flask(__name__)

def update_student(sno,sname,sage,sdob,scourse,course_duration):
    data=json_1.read_json("data/stud_data.json")
    for stud in data["Student_Manager"]:
        if stud["sno"]==int(sno):
            stud["name"]=sname
            stud["age"]=sage
            stud["dob"]=sdob
            stud["course"]=scourse
            stud["duration"]=course_duration
    json_1.write_json("data/stud_data.json",data)
     
    

def register_student(std_name,std_age,std_dob,std_course,course_duration):
    data=json_1.read_json("data/stud_data.json")
    sno=len(data["Student_Manager"])+1
    std_dict={
        "sno":sno,
        "name":std_name,
        "age":std_age,
        "dob":std_dob,
        "course":std_course,
        "duration":course_duration,
        "status":"Improgress"
    }
    data["Student_Manager"].append(std_dict)
    json_1.write_json("data/stud_data.json",data)

@app.route("/home",methods=["POST","GET"])
def index():
    if request.method=="POST":
        register_student(request.form["studname"],request.form["studage"],request.form["dob"],request.form["course"],request.form["duration"])

    data=json_1.read_json("data/stud_data.json")
    return render_template("index.html",stud_data=data["Student_Manager"])
@app.route("/",methods=["POST","GET"])
def login():
    # msg=""
    # if request.method=="POST":

    #     if request.form["username"]=="priya" and request.form["password"]=="2003":
    #         return redirect("/home")
    #     else:
    #         msg="invalid credtials"        
    return redirect("/home")
@app.route("/update/<int:id>", methods=["POST","GET"])
def update_sno(id):
    data=json_1.read_json("data/stud_data.json")
    print(len(data["Student_Manager"]))
    for stud in data["Student_Manager"]:
        print(stud)
        if int(id)==stud["sno"]:
            return render_template("update.html",stud=stud)
    return "update"

@app.route("/delete/<int:sno>",methods=["POST","GET"])
def delete(sno):
    data=json_1.read_json("data/stud_data.json")
    for stud in data["Student_Manager"]:
        if int(sno)==stud["sno"]:
            data["Student_Manager"].remove(stud)
    sno=1
    for stud in data["Student_Manager"]:
        stud["sno"]=sno
        sno+=1    
    json_1.write_json("data/stud_data.json",data)
    return redirect("/")
    
@app.route("/update", methods=["POST","GET"])
def update():
    if request.method=="POST":
        update_student(request.form["sno"],request.form["studname"],request.form["studage"],request.form["dob"],request.form["course"],request.form["duration"])
        return redirect("/")
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")