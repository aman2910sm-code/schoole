<?php

// All Students
function getALLStudents($conn){
    $sql = "SELECT * FROM student";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $student = $stmt->fetchAll();
        return $student;
    } else {
        return 0;
    }
}

// Student by Id
function getStudentById($student_id, $conn){
    $sql = "SELECT * FROM student
            WHERE student_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$student_id]);

    if ($stmt->rowCount() == 1) {
        $student = $stmt->fetch();
        return $student;
    } else {
        return 0;
    }
}

// Search Student
function searchStudent($key, $conn){
    $key = "%{$key}%";
    $sql = "SELECT * FROM student
            WHERE student_id LIKE ?
            OR fname LIKE ?
            OR lname LIKE ?
            OR username LIKE ?
            OR address LIKE ?
            OR email LIKE ?
            OR dob LIKE ?
            OR gender LIKE ?
            OR parent_fname LIKE ?
            OR parent_lname LIKE ?
            OR parent_phone LIKE ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$key, $key, $key, $key, $key, $key, $key, $key, $key, $key, $key]);

    if ($stmt->rowCount() >= 1) {
        $student = $stmt->fetchAll();
        return $student;
    } else {
        return 0;
    }
}

// Update Student
function updateStudent($student_id, $fname, $lname, $username, $address, $email, $dob, $gender, $grade_id, $section_id, $parent_fname, $parent_lname, $parent_phone, $conn){
    $sql = "UPDATE student
            SET fname=?, lname=?, username=?, address=?, email=?, dob=?, gender=?, grade=?, section=?, parent_fname=?, parent_lname=?, parent_phone=?
            WHERE student_id=?";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$fname, $lname, $username, $address, $email, $dob, $gender, $grade_id, $section_id, $parent_fname, $parent_lname, $parent_phone, $student_id]);
}

// Delete Student
function deleteStudent($student_id, $conn){
    $sql = "DELETE FROM student
            WHERE student_id=?";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$student_id]);
}
?>