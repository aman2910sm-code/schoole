<?php
// All student_score
function getALLScores($conn){
    $sql = "SELECT * FROM student_score";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $student_score = $stmt->fetchAll();
        return $student_score;
    } else {
        return 0;
    }
}

// student_score by Id
function getScoresById($id, $conn){
    $sql = "SELECT * FROM student_score
            WHERE id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$id]);

    if ($stmt->rowCount() == 1) {
        $student_score = $stmt->fetch();
        return $student_score;
    } else {
        return 0;
    }
}
?>