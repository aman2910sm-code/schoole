<?php
// All Students
function getALLStudents($conn){
    $sql = "SELECT * FROM student";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $students = $stmt->fetchAll();
        return $students;
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
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
        return normalizeStudentRow($row);
    } else {
        return 0;
    }
}

// DB ma column nu naam game pan hoy, edit/view form ne joiti keys sathe map kare chhe
function normalizeStudentRow($original) {
    $map = [
        'email'         => ['email', 'email_address'],
        'dob'           => ['dob', 'date_of_birth'],
        'parent_phone'  => ['parent_phone', 'parent_phone_number'],
        'address'       => ['address'],
        'gender'        => ['gender'],
        'parent_fname'  => ['parent_fname'],
        'parent_lname'  => ['parent_lname'],
        'fname'         => ['fname'],
        'lname'         => ['lname'],
        'username'      => ['username'],
        'grade'         => ['grade', 'grade_id'],
        'section'       => ['section'],
        'student_id'    => ['student_id'],
    ];

    $row = $original;

    foreach ($map as $expectedKey => $possibleColumns) {
        $value = '';
        foreach ($possibleColumns as $col) {
            if (isset($original[$col]) && $original[$col] !== '') {
                $value = $original[$col];
                break;
            }
        }
        $row[$expectedKey] = $value;
    }

    return $row;
}
?>