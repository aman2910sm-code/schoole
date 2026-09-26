<?php
// All Subjects
function getALLSubjects($conn){
    $sql = "SELECT * FROM Subjects";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $Subjects = $stmt->fetchAll();
        return $Subjects;
    } else {
        return 0;
    }
}

// Subject by Id
function getSubjectsById($subject_id, $conn){
    $sql = "SELECT * FROM Subjects
            WHERE subject_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$subject_id]);

    if ($stmt->rowCount() == 1) {
        $Subject = $stmt->fetch();
        return $Subject;
    } else {
        return 0;
    }
}
// Subject by Id
function getSubjectsByGrade($grade, $conn){
    $sql = "SELECT * FROM Subjects
            WHERE grade=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$grade]);

    if ($stmt->rowCount() > 0) {
        $Subject = $stmt->fetch();
        return $Subject;
    } else {
        return 0;
    }
}
?>
