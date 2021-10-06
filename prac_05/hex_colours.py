COLOR_TO_CODE = {"AliceBlue": "#f0f8ff","blue1": "#0000ff","black":"#000000","brown":"#a52a2a",
                 "coral": "#ff7f50","DarkGoldenrod": "#b8860b","DarkOrchid": "#9932cc","DarkSeaGreen": "#8fbc8f",
                 "DimGray": "#696969","firebrick": "#b22222"}
color = input("Enter the color's name: ")
while color != " ":
    if color in COLOR_TO_CODE:
        print(COLOR_TO_CODE[color])
    else:
        print("Invalid color's name")
    color = input("Enter the color's name: ")

