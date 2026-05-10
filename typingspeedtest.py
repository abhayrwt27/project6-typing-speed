import time

sentence="Python is a powerful programming language"

print("Typing Speed Tester")
print("\nType this sentence exactly.")
print(sentence)

ready = input("\nPress Enter when ready")

# Start timer
start_time = time.time()

# User typing
typed_text = input("\nStart typing: ")

# End timer 
end_time = time.time()

#Time taken
time_taken = end_time - start_time

# calculate words per min 
word_count = len(sentence.split())

wpm = (word_count / time_taken) * 60

#Accuracy check
if typed_text == sentence:
    accuracy = 100
else:
    correct_chars = 0

    for i in range(min(len(sentence)), len(typed_text)):
        if sentence[i] == typed_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(sentence)) * 100

# Output
print("\nResult")
print(f"Time taken: {round(time_taken, 2)} seconds")
print(f"Typing speed: {round(wpm, 2)} WPM")
print(f"Accuracy: {round(accuracy, 2)} %")