<?php

// All r_user 
function getALLR_users($conn){
    $sql = "SELECT * FROM registrar_office";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        return $stmt->fetchAll();
    } else {
        return 0;
    }
}

// r_user by Id
function getR_usersById($r_user_id, $conn){
    $sql = "SELECT * FROM registrar_office WHERE r_user_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$r_user_id]);

    if ($stmt->rowCount() == 1) {
        return $stmt->fetch();
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
        return $stmt->fetchAll();
    } else {
        return 0;
    }
}

// All Subjects
function getALLSubjects($conn){
    $sql = "SELECT * FROM subjects";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        return $stmt->fetchAll();
    } else {
        return 0;
    }
}

// Subject by Id
function getSubjectsById($subject_id, $conn){
    $sql = "SELECT * FROM subjects WHERE subject_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$subject_id]);

    if ($stmt->rowCount() == 1) {
        return $stmt->fetch();
    } else {
        return 0;
    }
}

// Class by Id
function getClassById($class_id, $conn){
    $sql = "SELECT * FROM class WHERE class_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$class_id]);

    if ($stmt->rowCount() == 1) {
        return $stmt->fetch();
    } else {
        return 0;
    }
}

// Grade by Id
function getGradeById($grade_id, $conn){
    $sql = "SELECT * FROM grades WHERE grade_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$grade_id]);

    if ($stmt->rowCount() == 1) {
        return $stmt->fetch();
    } else {
        return 0;
    }
}