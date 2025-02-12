import os

def add_hashtag_to_third_line(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            if len(lines) >= 3:
                lines[2] = lines[2].strip() + " #leetcode\n"
            
            with open(file_path, "w") as file:
                file.writelines(lines)

if __name__ == "__main__":
    directory = "04 - Resources/01_LeetCode"  # Change this to your target directory
    add_hashtag_to_third_line(directory)
