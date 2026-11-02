from sqlalchemy import create_engine, Column, INTEGER, Float,String, ForeignKey, event
from sqlalchemy.orm import declarative_base, sessionmaker,relationship

engine = create_engine('sqlite:///CourseData_Relation.db', echo=False)

#کد فعال‌سازی کلید خارجی
@event.listens_for(engine, 'connect')
def enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')   #به SQLite  محدودیت‌های کلید خارجی رو برای این اتصال فعال کنه
    cursor.close()

engine.connect()

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    id = Column(INTEGER,primary_key=True)
    name = Column(String, nullable=False)

    owner = relationship('Course',back_populates='student',cascade='all, delete',passive_deletes=True)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(INTEGER, primary_key=True)
    title = Column(String, nullable=False)
    unit = Column(INTEGER)

    student_id = Column(INTEGER, ForeignKey('students.id',ondelete='CASCADE'), nullable=False)

    student = relationship('Students',back_populates='owner')

Base.metadata.create_all(engine)
########################################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()

###########################################################
# student1 = Students(name = 'Narges Mousavi')
# student2 = Students(name = 'Sara Karimi')
# student3 = Students(name = 'Nima Mohammadi')
# student4 = Students(name = 'Elmira Hashemi')
# student5 = Students(name = 'Ali Afshari')

# sessionLocal.add_all([student1,student2,student3,student4,student5])
# sessionLocal.commit()

# *********************************************
# course2 = Course(title = 'Physics', unit = 2,student_id = 3)
# course3 = Course(title = 'Database', unit = 4,student_id= 5)
# course4 = Course(title = 'Programming', unit = 4, student_id = 1)
# course5 = Course(title = 'Web Development', unit = 3, student_id = 4)
# course6 = Course(title = 'Chemistry', unit = 2,student_id = 4)
# course7 = Course(title = 'Computer Networks', unit = 3,student_id =2)
# course8 = Course(title = 'Mathematics', unit = 2,student_id = 3)

# sessionLocal.add_all([course1,course2,course3,course4,course5,
#                       course6,course7,course8])
# sessionLocal.commit()
###############################################################
# student1 = Students(name='Test Student')

# student1.owner = [Course(title='Python', unit=3),Course(title='Database', unit=4)]

# sessionLocal.add(student1)
# sessionLocal.commit()

# print('Student ID:', student1.id)
# print('Student Name:', student1.name)
# print('Courses:', [course.title for course in student1.owner])

# student_id = student1.id

# sessionLocal.delete(student1)
# sessionLocal.commit()
################################################################
# DELETE:

student_temp = sessionLocal.query(Students).filter_by(id = 4).first()
print(student_temp.owner)
# if student_temp != None:
#     sessionLocal.delete(student_temp)
#     sessionLocal.commit()

##################################################################
# student_id_input = 999

# student_temp = sessionLocal.query(Students).filter_by(id=student_id_input).first()

# if student_temp != None:
#     course_test = Course(title='Artificial Intelligence',unit=3,student_id=student_id_input)

#     sessionLocal.add(course_test)
#     sessionLocal.commit()

#     print('Course added successfully!')

# else:
#     print('Error: This student does not exist!')

if student_temp:
    print(student_temp.name)
    for course in student_temp.owner:
        print(course.title, course.unit)