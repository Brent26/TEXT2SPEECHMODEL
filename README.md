 GradeBook System
        ----------------
        
        The GradeBook system is a simple, command-line-based student management program that allows users to:
        
        - Add subjects
        - Add students and assign grades for each subject
        - View, update, and remove student records
        - Display all students' grades and overall summaries
        - Sort and search students by name or by average grade
        
        Menu Options:
        1. Add a Subject - Adds a new subject to the system.
        2. Add a Student - Creates a new student record with grades.
        3. Search for a Student by Name - Searches and displays a student's record.
        4. Update a Student's Grades - Allows updating a student's grades.
        5. Remove a Student - Deletes a student record from the system.
        6. Display All Students - Shows all student names, grades, and averages.
        7. Display Grade Summary - Shows the highest and lowest grades per subject.
        8. View Grades by Subject - Displays grades of all students in a subject.
        9. Sort Students by Name - Sorts students alphabetically by name.
        10. Sort Students by Average Grade - Sorts students by their average grade.
        11. View README - Displays this guide.
        12. Exit - Exits the GradeBook system.
        
        How to Use
Start the Program:

Run the program file, and you'll be presented with a menu to interact with the system.
Menu Options:

1. Add a Subject
Adds a new subject to the system. All students will be able to receive grades for this subject.
Input: Enter the subject name (e.g., "IDA", "DDD").
Note: Subjects cannot be empty or duplicated.

2. Add a Student
Creates a new student record.
Input: Enter the student's name, then input their grades for each subject.
Note: The grades must be numeric values between 0 and 100.

3. Search for a Student by Name
Searches for a student in the system by name and displays their details (subjects and grades).
Input: Enter the student's name.

4. Update a Student's Grades
Allows updating the grades of an existing student.
Input: Enter the student's name, followed by updated grades for each subject.

5. Remove a Student
Deletes a student record from the system.
Input: Enter the student's name to remove them.

6. Display All Students
Displays all student names, subjects, grades, and average grades.
Note: Students without grades will show "N/A" as their average grade.

7. Display Grade Summary
Shows the highest and lowest grades per subject across all students.

8. View Grades by Subject
Displays all student grades for a specific subject.
Input: Enter the subject name to see the list of grades by student.

9. Sort Students by Name
Sorts and displays students alphabetically by name.

10. Sort Students by Average Grade
Sorts and displays students by their average grade in descending order.
Note: Students without grades will appear at the bottom with "N/A" as their average grade.

11. Exit
Exits the program.
Example Usage
Adding a Subject:

Choose option 1 and add a subject like "IPP".
Adding a Student:

Choose option 2, add the student's name, and provide grades for each subject.
Searching for a Student:

Choose option 3 and enter the student's name. The system will display all grades and the average grade.
Updating a Student's Grades:

Choose option 4, enter the student’s name, and update their grades for each subject.
Viewing Sorted Students:

Choose options 9 or 10 to sort students by name or by average grade.
System Structure
Student Class:

add_grade: Adds a grade for a specified subject.
calculate_average: Calculates the student's average grade.
get_subject_average: Gets the average grade for a specified subject.
print_details: Displays the student’s grades and average.
GradeBook Class:

add_subject: Adds a new subject to the list of subjects.
add_student: Creates and adds a student with grades for each subject.
linear_search_student: Searches for a student by name.
update_student_grades: Updates grades for an existing student.
remove_student: Removes a student record.
display_all_students: Shows all student details.
display_grade_summary: Shows the highest and lowest grades by subject.
view_grades_by_subject: Shows grades of all students for a specified subject.
bubble_sort_by_name: Sorts students alphabetically by name.
bubble_sort_by_average: Sorts students by their average grade.
Notes
Grades should be between 0 and 100.
Each student must have a unique name.
Adding subjects first is necessary before adding students to assign grades.
Sorting by average grade places students with no grades at the bottom with "N/A" as their average.


Error Handling
Input validation is provided to ensure names and grades are correctly entered.
Grades outside the valid range (0-100) will be rejected.
The system will inform users when they attempt to search for or update a student who is not in the system.
