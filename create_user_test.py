import sender_stand_request
import data

# Function to change the value of the firstName parameter in the request body
def get_user_body(first_name):
    # Copy the request body dictionary from the data file
    current_body = data.user_body.copy()
    # Change the value of the firstName parameter
    current_body["firstName"] = first_name
    # Return the new dictionary with the required firstName value
    return current_body

# Positive test function
def positive_assert(first_name):
    # The updated request body is stored in the user_body variable
    user_body = get_user_body(first_name)
    # The result of the request to create a new user is stored in the user_response variable
    user_response = sender_stand_request.post_new_user(user_body)

    # Check if the status code is 201
    assert user_response.status_code == 201
    # Check that the authToken field is in the response and contains a value
    assert user_response.json()["authToken"] != ""

    # Check that the result of the request is stored in users_table_response
    users_table_response = sender_stand_request.get_users_table()

    # String that should appear in the response body
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Check whether the user exists and is unique
    assert users_table_response.text.count(str_user) == 1

# Negative test function for cases where the request fails due to invalid characters
def negative_assert_symbol(first_name):
    # The updated request body is stored in the user_body variable
    user_body = get_user_body(first_name)

    # The result is stored in the response variable
    response = sender_stand_request.post_new_user(user_body)

    # Check if the status code is 400
    assert response.status_code == 400

    # Check that the code attribute in the response body is 400
    assert response.json()["code"] == 400
    # Check the message attribute in the response body
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, " \
                                         "la longitud debe ser de 2 a 15 caracteres."

# Negative test function when the error is "Not all required parameters were sent"
def negative_assert_no_firstname(user_body):
    # The result is stored in the response variable
    response = sender_stand_request.post_new_user(user_body)

    # Check if the status code is 400
    assert response.status_code == 400

    # Check that the code attribute in the response body is 400
    assert response.json()["code"] == 400
    # Check the message attribute in the response body
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# Test 1. User created successfully. The firstName parameter contains 2 characters
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Test 2. User created successfully. The firstName parameter contains 15 characters
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Test 3. Error. The firstName parameter contains 1 character
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Test 4. Error. The firstName parameter contains 16 characters
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Test 5. User created successfully. The firstName parameter contains Latin letters
def test_create_user_english_letter_in_first_name_get_success_response():
    positive_assert("QWErty")

# Test 6. Error. The firstName parameter contains spaces
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

# Test 7. Error. The firstName parameter contains special characters
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

# Test 8. Error. The firstName parameter contains digits
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# Test 9. Error. The firstName
def test_create_user_no_first_name_get_error_response():
    # Copy the request body dictionary from the "data" file into user_body
    user_body = data.user_body.copy()
    # Remove the "firstName" parameter from the request
    user_body.pop("firstName")
    # Validate the response
    negative_assert_no_firstname(user_body)

# Test 10. Error. The parameter contains an empty string
def test_create_user_empty_first_name_get_error_response():
    # The updated request body is stored in the user_body variable
    user_body = get_user_body("")
    # Validate the response
    negative_assert_no_firstname(user_body)

# Test 11. Error. The type of the firstName parameter is a number
def test_create_user_number_type_first_name_get_error_response():
    # The updated request body is stored in the user_body variable
    user_body = get_user_body(12)
    # The result of the request to create a new user is stored in the response variable
    response = sender_stand_request.post_new_user(user_body)

    # Check the response status code
    assert response.status_code == 400