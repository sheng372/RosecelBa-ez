from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Our "Database"
students = [
    {"id": 1, "name": "Your Name", "grade": 10, "section": "Zechariah"}
]

@app.route('/')
def home():
    return "Student Management API is Live!"

# 1. GET ALL STUDENTS
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# 2. GET A SINGLE STUDENT BY ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    # Find student by ID or return None
    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        abort(404, description="Student not found")
    return jsonify(student)

# 3. POST A NEW STUDENT
@app.route('/students', methods=['POST'])
def add_student():
    if not request.json or 'name' not in request.json:
        abort(400, description="Missing required field: 'name'")
    
    new_student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": request.json['name'],
        "grade": request.json.get('grade', 0),
        "section": request.json.get('section', "N/A")
    }
    students.append(new_student)
    return jsonify(new_student), 201

# 4. DELETE A STUDENT
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    # Filter the list to exclude the student with the matching ID
    student_exists = any(s for s in students if s["id"] == student_id)
    
    if not student_exists:
        abort(404, description="Cannot delete: Student not found")
        
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"result": True, "message": f"Student {student_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
