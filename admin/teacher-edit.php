<?php
session_start();
if (isset($_SESSION['admin_id']) && isset($_SESSION['role'])) {
    if ($_SESSION['role'] == 'Admin') {

        include "../DB_connection.php";
        include "../data/teacher.php";
        include "../data/subject.php";
        include "../data/grade.php";
        include "../data/section.php";

        if (!isset($_GET['teacher_id']) || empty($_GET['teacher_id'])) {
            header("Location: teacher.php");
            exit;
        }

        $teacher_id = $_GET['teacher_id'];
        $teacher    = getTeacherById($teacher_id, $conn);

        if ($teacher == 0) {
            header("Location: teacher.php");
            exit;
        }

        $allSubjects = getALLSubjects($conn);
        $allgrades   = getALLGrades($conn);
        $allsections = getALLSections($conn);

        $selectedSubjects = !empty($teacher['subjets']) ? array_filter(array_map('trim', explode(',', trim($teacher['subjets'], ',')))) : [];
        $selectedGrades   = !empty($teacher['class'])  ? array_filter(array_map('trim', explode(',', trim($teacher['class'], ',')))) : [];
        $selectedSections = !empty($teacher['section']) ? array_filter(array_map('trim', explode(',', trim($teacher['section'], ',')))) : [];

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin - Edit Teacher</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/school-management/style.css">
    <link rel="icon" href="/school-management/image/logo1.png">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <?php include "../inc/navbar.php"; ?>

    <div class="container mt-5">
        <a href="teacher.php" class="btn btn-dark">Go Back</a>

        <!-- Main Details Form -->
        <form method="post"
              class="shadow p-3 mt-5 form-w"
              action="req/teacher-edit.php">

            <input type="hidden" name="teacher_id" value="<?= $teacher['teacher_id'] ?>">

            <h3>Edit Teacher</h3><hr>
           <?php if (isset($_GET['updated'])) { ?>
            <div class="alert alert-success" role="alert">
                Successfully updated!
            </div>
            <?php } ?>
           <?php if (isset($_GET['error'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['error']) ?>
            </div>
            <?php } ?>
  <div class="mb-3">
    <label class="form-label">First name</label>
    <input type="text" class="form-control" name="fname" value="<?= htmlspecialchars($teacher['fname']) ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Last name</label>
    <input type="text" class="form-control" name="lname" value="<?= htmlspecialchars($teacher['lname']) ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Username</label>
    <input type="text" class="form-control" name="Username" value="<?= htmlspecialchars($teacher['username']) ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Address</label>
    <input type="text" class="form-control" name="address" value="<?= htmlspecialchars($teacher['address'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Employee Number</label>
    <input type="text" class="form-control" name="employee_number" value="<?= htmlspecialchars($teacher['employee_number'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Date Of Birth</label>
    <input type="date" class="form-control" name="date_of_birth" value="<?= htmlspecialchars($teacher['date_of_birth'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Phone Number</label>
    <input type="text" class="form-control" name="phone_number" value="<?= htmlspecialchars($teacher['phone_number'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Qualification</label>
    <input type="text" class="form-control" name="qualification" value="<?= htmlspecialchars($teacher['qualification'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Email Address</label>
    <input type="text" class="form-control" name="email_address" value="<?= htmlspecialchars($teacher['email_address'] ?? '') ?>">
  </div>
  <div class="mb-3">
    <label class="form-label">Gender</label><br>
    <input type="radio" value="Male" name="gender"
           <?= (($teacher['gender'] ?? '') == 'Male') ? 'checked' : '' ?>> Male
     &nbsp; &nbsp; &nbsp;    &nbsp;
    <input type="radio" value="Female" name="gender"
           <?= (($teacher['gender'] ?? '') == 'Female') ? 'checked' : '' ?>> Female
  </div>
  <div class="mb-3">
    <label class="form-label">Subject</label>
    <div class="d-flex flex-wrap gap-3">
        <?php foreach ($allSubjects as $sub) { ?>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" name="subject_id[]"
                   value="<?= $sub['subject_id'] ?>" id="subject_<?= $sub['subject_id'] ?>"
                   <?= in_array($sub['subject_id'], $selectedSubjects) ? 'checked' : '' ?>>
            <label class="form-check-label" for="subject_<?= $sub['subject_id'] ?>">
                <?= $sub['subject'] ?>
            </label>
        </div>
        <?php } ?>
    </div>
  </div>
  <div class="mb-3">
    <label class="form-label">Grade</label>
    <div class="d-flex flex-wrap gap-3">
        <?php foreach ($allgrades as $grd) { ?>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" name="grade_id[]"
                   value="<?= $grd['grade_id'] ?>" id="grade_<?= $grd['grade_id'] ?>"
                   <?= in_array($grd['grade_id'], $selectedGrades) ? 'checked' : '' ?>>
            <label class="form-check-label" for="grade_<?= $grd['grade_id'] ?>">
                <?= $grd['grade_code'] ?>-<?= $grd['grade'] ?>
            </label>
        </div>
        <?php } ?>
    </div>
  </div>
  <div class="mb-3">
    <label class="form-label">Section</label>
    <div class="d-flex flex-wrap gap-3">
        <?php foreach ($allsections as $sec) { ?>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" name="section_id[]"
                   value="<?= $sec['section_id'] ?>" id="section_<?= $sec['section_id'] ?>"
                   <?= in_array($sec['section_id'], $selectedSections) ? 'checked' : '' ?>>
            <label class="form-check-label" for="section_<?= $sec['section_id'] ?>">
                <?= $sec['section'] ?>
            </label>
        </div>
        <?php } ?>
    </div>
  </div>

    <button type="submit" class="btn btn-primary">Update</button>

</form>

        <!-- Separate Change Password Form -->
        <form method="post"
              class="shadow p-3 my-4 form-w"
              action="req/teacher-change.php">

            <input type="hidden" name="teacher_id" value="<?= $teacher['teacher_id'] ?>">

            <h3>Change Password</h3><hr>
            <?php if (isset($_GET['pupdated'])) { ?>
            <div class="alert alert-success" role="alert">
                Password successfully changed!
            </div>
            <?php } ?>
            <?php if (isset($_GET['perror'])) { ?>
            <div class="alert alert-danger" role="alert">
                <?= htmlspecialchars($_GET['perror']) ?>
            </div>
            <?php } ?>
            <div class="mb-3">
                <div class="mb-3">
                <label class="form-label"> Admin password</label>
                    <input type="password" class="form-control" name="admin_pass2" >

            </div>
                <label class="form-label"> new pasword</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" name="new_pass" id="passInput">
                    <button class="btn btn-secondary" type="button" id="gBtn">Random</button>
                </div>
            </div>
            <div class="mb-3">
                <label class="form-label">Confirm new pasword</label>
                    <input type="text" class="form-control" name="c_new_pass2" id="passInput2">

            </div>
<button type="submit" class="btn btn-primary">Change</button>

        </form>

</div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        $(document).ready(function(){
            $("#navlinks li:nth-child(2) a").addClass('active');
        });
        function makePass(length) {
            var result = '';
            var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            for (var i = 0; i < length; i++) {
                result += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            document.getElementById('passInput').value = result;
            document.getElementById('passInput2').value = result;
        }
        document.getElementById('gBtn').addEventListener('click', function(e){
            e.preventDefault();
            makePass(5);
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