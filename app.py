from sqlalchemy import create_engine, Column, INTEGER, Float,String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///StudentData.db', echo=False)
engine.connect()

Base = declarative_base()

class Students(Base):
    __tablename__ = 'Student'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    score = Column(Float)

Base.metadata.create_all(engine)
########################################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()

###################################################
# Create:

# student1 = Students(name = 'Narges Mousavi', score = 15.5)
# student2 = Students(name = 'Sara Karimi',  score = 18)
# student3 = Students(name = 'Ayda Mohammadi',  score = 20)
# student4 = Students(name = 'Elmira Hashemi',  score = 12)

# sessionLocal.add_all([student1,student2,student3,student4])
# sessionLocal.commit()

################################################################
# Read:

# student_obj = sessionLocal.query(Students).all() 

# for item in student_obj:
#     print(item.name)
#     print(item.score)   
#     print('--'*30)
# ################################################################
# Update:
st_temp = sessionLocal.query(Students).filter_by(id =1).first()

print(st_temp.name)
print(st_temp.score)

st_temp.name = 'Aysoda Ahmadi'
st_temp.score = 19
sessionLocal.commit()
##################################################################
# Delete:

# if st_temp != None:
#     sessionLocal.delete(st_temp)
#     sessionLocal.commit()

