from vehical import vehical_details
def test_vehical_details():
    excepted_output=(
        "vid=101\n"
        "vname=car\n"
        "price=50000\n"
        "yop=2024"
    )
    assert vehical_details("vid","vname","price","yop")