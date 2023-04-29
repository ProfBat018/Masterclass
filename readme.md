# Proekti run elemek ucun: 
## Link ve port asagida html-de olacaq
```python
pip install -r requirements.txt
```
```python
python -m uvicorn user_routes:app --reload
```

# Proekti test elemek ucun: 
```html
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>
    <h1>User Registration</h1>
    <form action="http://127.0.0.1:8000/register" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
     <h1>User Login</h1>
    <form action="http://127.0.0.1:8000/login" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```


