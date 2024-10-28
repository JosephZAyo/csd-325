# Joseph Ayo, October 27th, 2024. Module 1.3 Assignment
# The purpose of this program is to recieve user input about how many
# bottles of beer they own, and then display the lyrics to the 99 bottles song,
# based on the given input.
# Sources: CSC205 Slideshows
def countdown_bottles(num_bottles):
    while num_bottles > 0:
        if num_bottles > 1:
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
            num_bottles -= 1
            print(f"Take one down and pass it around, {num_bottles} bottles of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            num_bottles -= 1
            print(f"Take one down and pass it around, {num_bottles} bottles of beer on the wall.\n")

    print("Time to buy more bottles of beer.")
    exit(0)
def main():
    try:
        bottles = int(input("Enter number of bottles:"))
        if bottles < 0:
            print("Please enter a positive number.")
        else:
            countdown_bottles(bottles)
            print("Remember to buy more beer!")

    except ValueError:
        print("Please enter a valid number.")

main()