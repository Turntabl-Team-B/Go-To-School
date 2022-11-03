from datetime import datetime
from random import randint
from flask import request, jsonify, Blueprint
# from werkzeug.security import generate_password_hash, check_password_hash

from .LessonModel import Lesson
from Lecturers.LecturerModel import Lecturer
from Classes.ClassModel import Classi
from Rooms.RoomModel import Room
from Courses.CourseModel import Course

from flask_cors import CORS

lessons_route = Blueprint("lessons_route", __name__)
CORS(lessons_route)

# Get all lessons
@lessons_route.route("/lessons", methods=['GET'])
def getlessonss():
    from app import session
    try:
        lessons = session.query(Lesson).all()
        Json_lessons = []

        for lesson in lessons:
            lecturer = session.query(Lecturer).get(lesson.idLecturer)
            classO = session.query(Classi).get(lesson.idClass)
            room = session.query(Room).get(lesson.idRoom)
            course = session.query(Course).get(lesson.idCourse)

            Json_lessons.append({
                "msg": {

                "id_lecturer": lecturer.idLecturer,
                "course_name": course.courseName,
                "class_name": classO.className,
                "room_number": room.room_name,
                "start_time": lesson.timeStart,
                "end_time": lesson.timeEnd,
            },
            "status": True
            })
        return jsonify(Json_lessons), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Connection error: could not get students"
            }
        }), 400


# # Get all students
# @students_route.route("/students", methods=['GET'])
# def getStudents():
#     from app import session
#     try:
#         lecturer = session.query(Lecturer).get(id)
#         classO = session.query(Classi).get(id)
#         room = session.query(Room).get(id)
#         course = session.query(Course).get(id)


#         students = session.query(Student).all()
#         Json_students = [{

#             "msg": {
#                 "id_lecturer": student.idStudent,
#                 "d_class": student.first_name,
#                 "id_room": student.last_name,
#                 "time_start": student.user_email,
#                 "time_end": student.user_password,
#                 "id_course": student.date_of_birth,
#             },
#             "status": True

#         } for student in students]
#         return jsonify(Json_students), 200
#     except Exception as e:
#         return ({
#             'status': False,
#             'msg': {
#                 "dev_message": (f"{e}"),
#                 "message": "Connection error: could not get students"
#             }
#         }), 400

# Get lesson by ID
@lessons_route.route("/lessons/<id>", methods=['GET'])
def getLessonById(id):
    from app import session
    try:
        lesson = session.query(Lesson).get(id)

        return ({

            "msg": {

                "id_lecturer": lesson.idStudent,
                "d_class": lesson.first_name,
                "id_room": lesson.last_name,
                "time_start": lesson.user_email,
                "time_end": lesson.user_password,
                "id_course": lesson.date_of_birth,
            },
            "status": True

        }), 200
    except Exception as e:
        return ({
            'status': False,
            'msg': {
                "dev_message": (f"{e}"),
                "message": "Error: Student ID does not exist"
            }
        }), 400

