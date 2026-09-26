<?php
// All Classes (joined with grade and section for display)
function getALLClasses($conn){
    $sql = "SELECT c.class_id, c.grade, c.section,
                   g.grade_code, g.grade AS grade_num,
                   s.section AS section_name
            FROM class c
            JOIN grades g  ON c.grade = g.grade_id
            JOIN section s ON c.section = s.section_id";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        $classes = $stmt->fetchAll();
        return $classes;
    } else {
        return 0;
    }
}

// Get Class by Id (raw, IDs only)
function getClassById($class_id, $conn){
    $sql = "SELECT * FROM class
            WHERE class_id=?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$class_id]);

    if ($stmt->rowCount() == 1) {
        $class = $stmt->fetch();
        return $class;
    } else {
        return 0;
    }
}

// Get Class by Id WITH grade_code, grade_num, section_name joined in (for display labels)
function getClassWithDetailsById($class_id, $conn){
    $sql = "SELECT c.class_id, c.grade, c.section,
                   g.grade_code, g.grade AS grade_num,
                   s.section AS section_name
            FROM class c
            JOIN grades g  ON c.grade = g.grade_id
            JOIN section s ON c.section = s.section_id
            WHERE c.class_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$class_id]);

    if ($stmt->rowCount() == 1) {
        return $stmt->fetch();
    } else {
        return 0;
    }
}

// Check if a class with this grade+section already exists
function classExists($grade_id, $section_id, $conn){
    $sql = "SELECT * FROM class WHERE grade = ? AND section = ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$grade_id, $section_id]);
    return $stmt->rowCount() > 0;
}

// Check if a class with this grade+section already exists, excluding a given class_id (for edit)
function classExistsExcluding($grade_id, $section_id, $exclude_class_id, $conn){
    $sql = "SELECT * FROM class WHERE grade = ? AND section = ? AND class_id != ?";
    $stmt = $conn->prepare($sql);
    $stmt->execute([$grade_id, $section_id, $exclude_class_id]);
    return $stmt->rowCount() > 0;
}

// Add Class
function addClass($grade_id, $section_id, $conn){
    $sql = "INSERT INTO class (grade, section) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$grade_id, $section_id]);
}

// Update Class
function updateClass($class_id, $grade_id, $section_id, $conn){
    $sql = "UPDATE class SET grade = ?, section = ? WHERE class_id = ?";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$grade_id, $section_id, $class_id]);
}

// Delete Class
function deleteClass($class_id, $conn){
    $sql = "DELETE FROM class WHERE class_id = ?";
    $stmt = $conn->prepare($sql);
    return $stmt->execute([$class_id]);
}
?>