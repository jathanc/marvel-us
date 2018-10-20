if(isset($_FILES['image'])){//Checks if file is set
  $errors= array();
  $file_name = $_FILES['image']['name'];
  $file_size =$_FILES['image']['size'];
  $file_tmp =$_FILES['image']['tmp_name'];
  $file_type=$_FILES['image']['type'];
  $file_ext=strtolower(end(explode('.',$_FILES['image']['name'])));
  //(above) checks file extension by getting text after last dot

  $expensions= array("jpeg","jpg","png");//supported file types

  if(in_array($file_ext,$expensions)=== false){//is the extension in the supported types
     $errors[]="extension not allowed, please choose a JPEG or PNG file.";
  }

  if($file_size > 2097152){//PHP only supports files under 2MB
     $errors[]='File size must be excately 2 MB';
  }

  //If there's no error moves files to folder "images" in the root of this file, else prints all the errors
  if(empty($errors)==true){
     move_uploaded_file($file_tmp,"images/".$file_name);
     echo "Success";
  }else{
     print_r($errors);
  }
}
