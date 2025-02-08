import allure
from pydantic import ValidationError
from core.models.booking import BookingResponse


@allure.feature('Test - create booking')
@allure.story('Positive: create booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_client.create_booking(booking_data)
    try:
        # validation - in place of validate(response, SCHEME)
        BookingResponse(**response)
    except ValidationError as e:
        raise ValueError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates'] == booking_data['bookingdates']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test - create booking')
@allure.story('Positive: create booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)

    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValueError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == generate_random_booking_data['firstname']
    assert response['booking']['lastname'] == generate_random_booking_data['lastname']
    assert response['booking']['totalprice'] == generate_random_booking_data['totalprice']
    assert response['booking']['depositpaid'] == generate_random_booking_data['depositpaid']
    assert response['booking']['bookingdates'] == generate_random_booking_data['bookingdates']
    assert response['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == generate_random_booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == generate_random_booking_data['additionalneeds']

def test_create_booking_without_firstname(api_client, generate_random_booking_data_without_firstname):

    response = api_client.create_booking(generate_random_booking_data_without_firstname)
    print(response)