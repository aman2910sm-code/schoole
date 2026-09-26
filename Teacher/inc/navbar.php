<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
$role = $_SESSION['role'] ?? '';
?>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="index.php">
            <img src="/school-management/image/logo1.png" width="30">
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0" id="navlinks">
                <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="index.php">Dashboard</a>
                </li>

                <?php if ($role === 'Teacher'): ?>

                    <li class="nav-item">
                        <a class="nav-link" href="classes.php">Classes</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="students_of_class.php">Students</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="student-grade.php">Students Grade</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="pass.php">Change Password</a>
                    </li>

                <?php elseif ($role === 'Admin'): ?>

                    <li class="nav-item">
                        <a class="nav-link" href="teacher.php">Teacher</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="student.php">Student</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="grade.php">Grade</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="section.php">Section</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="class.php">Class</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="registrar-Office.php">Registrar-Office</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="course.php">Course</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Settings</a>
                    </li>

                <?php endif; ?>

            </ul>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link" href="../logout.php">Logout</a>
                </li>
            </ul>
        </div>
    </div>
</nav>