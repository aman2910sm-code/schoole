<?php

// Badha messages lavo (navo pehla)
function getAllMessages($conn) {
    $sql  = "SELECT * FROM message ORDER BY message_id DESC";
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    if ($stmt->rowCount() >= 1) {
        return $stmt->fetchAll();
    }
    return 0;
}