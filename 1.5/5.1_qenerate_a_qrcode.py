import qrcode 
name =input("Enter your name: ")
phone_number = input("Enter your phone number: ")
user =(f"name:{name} phone number:{phone_number}")
image = qrcode.make(user)
image.save("my_qr_code.png")
