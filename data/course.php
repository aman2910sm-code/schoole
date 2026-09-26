<?php
// All Courses (with grade label like "G-2" or "KG-1")
function getALLCourses($conn){
    $sql = "SELECT courses.*,
                   CONCAT(courses.grade_code, '-', courses.grade) AS grade_name
            FROM courses";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $courses = $stmt->fetchAll();
        return $courses;
    } else {
        return 0;
    }
}

// Get course by Id (with grade label)
function getCoursesById($course_id, $conn){
    $sql = "SELECT courses.*,
                   CONCAT(courses.grade_code, '-', courses.grade) AS grade_name
            FROM courses
            WHERE courses.course_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$course_id]);

    if ($stmt->rowCount() == 1) {
        $course = $stmt->fetch();
        return $course;
    } else {
        return 0;
    }
}

// Grades for the Add/Edit Course dropdown (e.g. "KG-1", "KG-2", "G-1", "G-2")
function getAllGradesForDropdown($conn){
    $sql = "SELECT grade_code, grade,
                   CONCAT(grade_code, '-', grade) AS grade_label
            FROM grades
            WHERE grade_code IN ('KG', 'G')
            ORDER BY
                FIELD(grade_code, 'KG', 'G'),
                grade ASC";
    $stmt = $conn->prepare($sql);
    $stmt->execute();
    return $stmt->fetchAll();
}

// Check if a course with the same name + grade already exists
function courseExists($conn, $course_name, $grade_code, $grade){
    $sql = "SELECT course_id FROM courses
            WHERE course_name = ? AND grade_code = ? AND grade = ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$course_name, $grade_code, $grade]);
    return $stmt->rowCount() > 0;
}

// Insert a new course (now stores grade_code too, e.g. 'KG' or 'G')
function addCourse($conn, $course_name, $course_code, $grade_code, $grade){
    $sql = "INSERT INTO courses (course_name, course_code, grade_code, grade)
            VALUES (?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$course_name, $course_code, $grade_code, $grade]);
}

// Check if ANOTHER course (different id) already has this name + grade (used when editing)
function courseExistsExceptId($conn, $course_name, $grade_code, $grade, $course_id){
    $sql = "SELECT course_id FROM courses
            WHERE course_name = ? AND grade_code = ? AND grade = ? AND course_id != ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$course_name, $grade_code, $grade, $course_id]);
    return $stmt->rowCount() > 0;
}

// Update an existing course
function updateCourse($conn, $course_id, $course_name, $course_code, $grade_code, $grade){
    $sql = "UPDATE courses
            SET course_name = ?, course_code = ?, grade_code = ?, grade = ?
            WHERE course_id = ?";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$course_name, $course_code, $grade_code, $grade, $course_id]);
}

// Delete a course by id
function deleteCourse($conn, $course_id){
    $sql = "DELETE FROM courses WHERE course_id = ?";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$course_id]);
}
?>