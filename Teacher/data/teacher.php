<?php

// All Teacher
function getALLTeacher($conn){
    $sql = "SELECT * FROM teacher";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $teacher = $stmt->fetchAll();
        return $teacher;
    } else {
        return 0;
    }
}

// Teacher by Id
function getTeacherById($teacher_id, $conn){
    $sql = "SELECT * FROM teacher
            WHERE teacher_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$teacher_id]);

    if ($stmt->rowCount() == 1) {
        $teacher = $stmt->fetch();
        return $teacher;
    } else {
        return 0;
    }
}

// Search Teacher
function searchTeacher($key, $conn){
    $key = "%{$key}%";
    $sql = "SELECT * FROM teacher
            WHERE teacher_id LIKE ?
            OR fname LIKE ?
            OR lname LIKE ?
            OR username LIKE ?
            OR employee_number LIKE ?
            OR date_of_birth LIKE ?
            OR phone_number LIKE ?
            OR qualification LIKE ?
            OR gender LIKE ?
            OR email_address LIKE ?
            OR address LIKE ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$key, $key, $key, $key, $key, $key, $key, $key, $key, $key, $key]);

    if ($stmt->rowCount() >= 1) {
        $teacher = $stmt->fetchAll();
        return $teacher;
    } else {
        return 0;
    }
}