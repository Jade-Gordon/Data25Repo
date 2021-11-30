# # open a file that doesn't exist
# # "open" portal
# #file = open("order.txt") # -> FileNotFoundError
#
# # What if someone deletes a file?
# # Try except block:
# # PEP 8 Except -> don't just have except:
# # .... have except (Error message given when tested):
# # see below!
# # use "as" to give an alias so that the original error msg can also be seen
def open_and_print_file(file):
    try:
        with open(file, "r") as opened_file:
            file_line_list = opened_file.readlines()

            for line in file_line_list:
                # remove the extra space (refer to written notes and recording)
                print(line.replace("\n", ""))
            # # close the portal
            # opened_file.close()
            # don't need to include the above line as "with" closes the file for us

    except FileNotFoundError as errmsg:
        print("There's no file...PANIC!", errmsg)
        # prints "[Errno 2] No such file or directory: 'order.txt'
        # what if you want the error to appear again
        # raise -> not needed with finally
    finally:
        print("Execution Complete :)")
# open_and_print_file("order.txt") -> reads the txt file
#
def write_to_file(file, order_item):
    try:
        with open(file, "a") as file_to_write:
            file_to_write.write(order_item+"\n")
    except FileNotFoundError:
        print("File doesn't exist")

write_to_file("order.txt", "Fried Chicken")
open_and_print_file("order.txt")