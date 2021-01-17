def delivery_report(day_number,file_name):
    """prints daily delivery report on the terminal"""

    # print day of delivery on the terminal
    print("Day", day_number) 
    # assigns variable 'the_file' to the contents of the file
    the_file = open(file_name)
    # loop through each line of the file
    for line in the_file:
        # remove any trailing characters
        line = line.rstrip()
        # splits the string into a list of melon name, count and amount
        words = line.split('|')
        # accesses items of the list and assigns corresponding variables
        melon = words[0]
        count = words[1]
        amount = words[2]
        # prints the message
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()
# calls the delivery_report function for each day of delivery
delivery_report(1, "um-deliveries-20140519.txt")
delivery_report(2, "um-deliveries-20140520.txt")
delivery_report(3, "um-deliveries-20140521.txt")


