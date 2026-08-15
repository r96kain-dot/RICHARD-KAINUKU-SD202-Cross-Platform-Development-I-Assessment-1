#RICHARD KAINUKU 
#Student ID: 270565532

#Task 2: Sports emojis

#Emoji dictionary
emoji_map = {
    "Soccer": "⚽",
    "Cricket": "🏏",
    "Rugby": "🏉",
    "Golf": "⛳",
    "Volleyball": "🏐",
    "Hockey": "🏒",
    "Squash": "🎾",
    "Bowling": "🎳",
    "Table-tennis": "🏓",
    "Handball": "🤾",
    "Basketball": "🏀",
    "Boxing": "🥊"}

#Validate input
#Both error messages provided by the assessment.
def validate_input(keywords):
    if len(keywords) != 5:
        return "Error. Number of keywords is less than 5. Re-enter keywords"

    if len(keywords) != len(set(keywords)):
        return "Error. Repeating keywords are not allowed. Re-enter keywords"

    return None

#Convert keywords to emojis
def convert_to_emojis(keywords):
    emojis = []

    for keyword in keywords:
        emojis.append(emoji_map.get(keyword, "❓"))

    return emojis

#Handle user input and retries
while True:
    user_input = input("Enter 5 sports separated by commas: ")
    #To accept spaces after commas when entering keywords
    keywords = [keyword.strip() for keyword in user_input.split(",")]

    error = validate_input(keywords)

    if error:
        print(error)
        continue

    emojis = convert_to_emojis(keywords)
    print(emojis)