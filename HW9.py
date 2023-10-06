# with open('homework.txt', 'w') as test_file:
#     test_file.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings "
#                     "and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end "
#                     "them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand "
#                     "natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep"
#                     )
with open("homework.txt", "w") as test_file:
    test_file.write(
        "To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows "
        "of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to "
        "sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is "
        "heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep"
    )

with open("homework.txt", "r") as test_file:
    textcopy=test_file.read().rstrip("\n")
# print(textcopy.split())

punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for element in textcopy:
    if element in punctuation:
        textcopy=textcopy.replace(element,"")
textcopy=textcopy.split()

Word_length_list=[len(i) for i in textcopy]
# print(Word_length_list)
with open("7 letter words.txt", "w") as text:
    for i in range(len(Word_length_list)):
        if Word_length_list[i]==7:
            text.write(textcopy[i])
            text.write(" ")

#2nd task
word_count=len(textcopy)
print(word_count)

#3rd task
with open("homework.txt","r") as test_file:
    newtext=test_file.read()
    replace_count=newtext.count("die")
    newtext=newtext.replace("die","***")

print(f"Count of replaced words: {replace_count}\nNew text: {newtext}")


