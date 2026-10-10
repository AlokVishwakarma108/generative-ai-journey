byy_greet = ["Byy", "byy", "by", "By", "Bye", "bye"]
contact = {}

def input_text(text):
  return input(f"{text} :")
  
while True:
  cmd = input("Type, 'Add','Search','Show' or 'Quit'")

  if cmd == "Add":
    name = input_text("Name")
    phone = input_text("Phone")
    contact[name] = phone
    print("Saved!")
    
  elif cmd == "Search":
    name = input_text("Name")
    if name in contact:
      print(f"{contact[name]}")
    else:
      print(f"{name} not found!")

  elif cmd == "Show":
    for name, contact in contact.items():
      print(f"{name} : {contact}\n")

  elif cmd in byy_greet:
    print("Have a Good Day! Byy")
    break

  else:
    print("Invalid Input")
    