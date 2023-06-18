# Project Description
A digital platform for document distribution business, allowing users to remotely access and download various documents such as wedding cards and admission forms.


<h2>Setup & Run</h2>
To run the application, please follow the guidlines below
<p>
1. Requirements
 <ul>
  <li>Python3</li>
  <li>Django</li>

</ul></p>
<p>2. Install python3</p>

<p>3. Please setup as indicated below:</p>

 
  ### Clone this repository into the directory of your choice
  ```
  git clone https://github.com/claraborlu/file-server.git
  ```
  
  ### Move into project folder
   ```
   cd file-server
   ```
  
  ### install dependencies from requirments.txt
  ```
  pip install -r requirements.txt
  ```
  
  ### Migrate models
  ```
  python manage.py migrate
  ```

  ### Access the Feed page at
  ```
  http://127.0.0.1:8000/
  ```
  ### Access the upload files at
  ```
  http://127.0.0.1:8000/upload/
  ```
  ### login at
  ```
  http://127.0.0.1:8000/accounts/login/
  ```
  ### Signup at
  ```
  http://127.0.0.1:8000/accounts/signup/
  ```
  ### Reset Password at
  ```
  http://127.0.0.1:8000/accounts/password_reset/
  ```