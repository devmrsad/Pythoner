try:
    passed_secs = int(input("Enter the number of seconds passed today: "))
except Exception as e:
    exit(f"An error occurred: {e}")

# wrong input detection
if(passed_secs > 86400 or passed_secs < 0):
    exit("Invalid input: The number of seconds must be between 0 and 86400 (inclusive).")

hours = passed_secs // 3600
remaining_secs = passed_secs % 3600
minutes = remaining_secs // 60
remaining_secs = remaining_secs % 60
seconds = remaining_secs

print(f"Time passed today: {hours} hours, {minutes} minutes, and {seconds} seconds.")
print(f"Total seconds passed today: {passed_secs} seconds.")