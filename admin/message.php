<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {

    if ($_SESSION['role'] == 'Admin') {
        include "../DB_connection.php";
        include "../data/message.php";

        $messages = getAllMessages($conn);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Message</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <h4 class="text-center p-3">Inbox</h4>

        <?php if ($messages != 0) { ?>
        <div class="accordion accordion-flush" id="accordionFlushExample">
            <?php foreach ($messages as $message) {
                $id = (int) $message['message_id'];
            ?>
            <div class="accordion-item">
                <h2 class="accordion-header" id="flush-heading<?= $id ?>">
                    <button class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse"
                            data-bs-target="#flush-collapse<?= $id ?>"
                            aria-expanded="false"
                            aria-controls="flush-collapse<?= $id ?>">
                        <?= htmlspecialchars($message['sender_full_name']) ?>
                    </button>
                </h2>
                <div id="flush-collapse<?= $id ?>" class="accordion-collapse collapse"
                     aria-labelledby="flush-heading<?= $id ?>"
                     data-bs-parent="#accordionFlushExample">
                    <div class="accordion-body">
                        <p class="mb-2">
                            <?= nl2br(htmlspecialchars($message['message'])) ?>
                        </p>
                        <div class="d-flex justify-content-between">
                            <span>
                                Email:
                                <a href="mailto:<?= htmlspecialchars($message['sender_email']) ?>">
                                    <b><?= htmlspecialchars($message['sender_email']) ?></b>
                                </a>
                            </span>
                            <span><?= htmlspecialchars($message['date_time'] ?? '') ?></span>
                        </div>
                    </div>
                </div>
            </div>
            <?php } ?>
        </div>
        <?php } else { ?>
            <div class="alert alert-info" role="alert">Empty!</div>
        <?php } ?>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(9) a").addClass('active');
        });
    </script>
</body>
</html>
<?php
    } else {
        header("Location: ../login.php");
        exit;
    }
} else {
    header("Location: ../login.php");
    exit;
}
?>