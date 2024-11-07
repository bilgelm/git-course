# This R script reads in message.txt and converts each integer in this text file
# to the corresponding UTF-8 encoded character to reveal the secret message.
#
# The script, however, is buggy. It contains 3 typos (on lines 8, 12, and 15)
# that need to be fixed.

# read in message.txt and save to a variable called msg
msg <- scan(file.path("msge.txt"), sep = " ", quiet = TRUE) change 1

# convert msg from integers to UTF-8 characters
# save to a variable called decoded_msg
decoded_msg <- intToUtf8(mgs) change 2

# display decoded_msg using the "message" function
message(decoded_mgs)
