from rich.console import Console
from rich.table import Table
import csv

console = Console()

console.print("Data on TikTok Hashtags", style="bold cyan")

table = Table(title="TikTok Hashtags")

table.add_column("Hashtag", style="magenta")
table.add_column("Video title", style="cyan")
table.add_column("Likes", style="cyan")
table.add_column("Saves", justify="right")

original_data= [
    ["#booktok", "get to know me as a reader/booktoker!", "125.7K", "13.1"],
    ["#foodtok", "crispy honey chipotle chicken tacos 🍯🌶️✨", "484.6K", "151.1K"],
    ["#gymtok", "leg day wearing new @DFYNE origin 🤌🏼 ", "89.8K", "18.1K"],
    ["#studytok", "lock in twin", "30K", "4538"],
    ["#beautytok", "I have been wanting to try the new @Rare Beauty bodycare", "74.3K", "12.9K"]
]
for row in original_data:
    table.add_row(*row)
console.print(table)

new_entries = []

while True:
    console.print("Now I want you to enter some TikTok's from your feed!")

    hashtag = input("Enter the hashtag: ")
    video_title = input("Enter the video title: ")
    likes = input("Enter the number of likes: ")
    saves = input("Enter the number of saves: ")

    console.print("\nYou entered:", style="bold green")
    console.print(f"Hashtag: {hashtag}")
    console.print(f"Video title: {video_title}")
    console.print(f"Likes: {likes}")
    console.print(f"Saves: {saves}")
    confirm = input("Is this correct? (yes/no): ").lower()

    if confirm == "yes":
        new_entries.append([hashtag, video_title, likes, saves])
        console.print("Data has been saved.", style="bold blue")
    else:
        console.print("Restart to clear and re-enter the data.", style="bold red")

    again = input("Input another entry? (yes/no): ").lower()
    if again != "yes":
        break

for entry in new_entries:
    table.add_row(*entry)
   
console.print("\nUpdated Table with your entries:", style="bold cyan")
console.print(table)

filename = "tiktok_data.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Hashtag", "Video title", "Likes", "Saves"])

    for row in original_data + new_entries:
        writer.writerow(row)

console.print(f"\nYour data has been saved", style="bold blue")
