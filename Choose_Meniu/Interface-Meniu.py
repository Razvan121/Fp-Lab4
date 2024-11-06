from Main.Main import meniu
from new_UI.Interface1 import  run_batch_mode

print("1.Normal Mode")
print("2.Batch Mode")

command = input("Choose:")

if command == "1":
    print("Normal Mode")
    meniu()
elif command == "2":
    run_batch_mode()
    print("Batch Mode")
else:
    print("Invalid Input")

