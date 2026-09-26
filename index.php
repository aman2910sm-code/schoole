<?php
include "DB_connection.php";
include "data/setting.php";

$setting = getsetting($conn);
$current_year = ($setting != 0 && !empty($setting['current_year']))
    ? $setting['current_year']
    : date('Y');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Raino School</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="logo1.png">
</head>
<body class="main-container">
    <div class="black-fill"><br /><br />
        <div class="container">
            <nav class="navbar navbar-expand-lg bg-body-tertiary" 
            id="homeNav">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="image/logo1.png" width="30">

        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#about">About</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#contact">Contact</a>
                </li>
            </ul>
            <ul>
                <li class="nav-item">
                    <a class="nav-link" href="login.php">login</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<section class="welcome-text d-flex justify-content-center align-item-center flex-column" >
    <img src="image/logo1.png">
    <h4>Welcome to Raino School </h4>
    <p> Learn Today, Lead Tomorrow. </p> 

</section> 

<section class="welcome-text d-flex justify-content-center align-item-center" id="about" >
    <div class="card mb-3" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="image/logo1.png" class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">About Us</h5>
        <p class="card-text">We are a school committed to providing quality education in a safe,
             caring, and inspiring environment. Our aim is to help every student discover their potential, 
             develop confidence, and become a responsible individual.</p>
        <p class="card-text"><small class="text-body-secondary">R school</small></p>
      </div>
    </div>
  </div>
</div>

</section> 
<section class="welcome-text d-flex justify-content-center 
align-item-center" id="contact" >
   <form 
   method="post"
   action="req/contact.php">
    <h3>Contact Us</h3>
    <?php if (isset($_GET['error'])) { ?>
<div class="alert alert-danger" role="alert">
    <?= htmlspecialchars($_GET['error']) ?>
</div>
<?php } ?>
<?php if (isset($_GET['success'])) { ?>
<div class="alert alert-success" role="alert">
    <?= htmlspecialchars($_GET['success']) ?>
</div>
<?php } ?>

  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" name="email" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label class="form-label">Full Name</label>
    <input type="text" name="full_name" class="form-control">
  </div>
   <div class="mb-3">
    <label class="form-label">Message</label>
    <textarea  class="form-control"  name="message" rows="4"></textarea>
  </div>
  
  <button type="submit" class="btn btn-primary">Send</button>
</form>

</section> 
<div class="text-center text-light">
    Copyright &copy; <?= htmlspecialchars($current_year) ?> Raino School. All right reserved.
</div>

        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>