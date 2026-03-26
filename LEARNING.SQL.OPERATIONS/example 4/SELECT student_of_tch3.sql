SELECT students.name, students.id
FROM students
INNER JOIN students_teachers
ON students.id = students_teachers.student_id
WHERE students_teachers.teacher_id = 1
;
/*
this is an inner join 
its returns all the data from the left table  and the right table only if they have a mtaching relationships
*/
