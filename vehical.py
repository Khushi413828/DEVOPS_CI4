def vehical_details(vid,vname,price,yop):
    result=(
        f"vid={vid}"
        f"vname={vname}"
        f"price={price}"
        f"yop={yop}"
    )
    return result
if __name__="__main__":
    vid=101
    vname="car"
    price=50000
    ypo=2024
    print(vehical_details("vid","vname","price","yop"))
