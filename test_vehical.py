# test_vehical.py

from vehical import vehical_details

def test_vehical_details():
    expected_output = (
        "vide: 101\n"
        "vname: car\n"
        "price: 50000\n"
        "yop:2024"
    )

    assert vehical_details(101, "car", 50000, 2024) == expected_output
