# Karina Chorna
# Chapter 2: Exercise 2
# The purpose of this code is to calculate the likelihood that the message a user enters is spam.

# List of spam keywords/phrases
SPAM_KEYWORDS = [
    "free", "buy now", "click here", "subscribe", "limited time",
    "winner", "you have been selected", "act now", "earn money", "risk-free",
    "guarantee", "urgent", "100% free", "no cost", "order now",
    "special promotion", "exclusive deal", "apply now", "congratulations", "cheap",
    "work from home", "miracle", "million dollars", "instant", "offer",
    "money back", "discount", "credit card", "expires", "trial"
]

# calculate the spam score
def calculate_spam_score(message):
    message = message.lower()
    spam_score = 0
    spam_keywords = []

    # add each spam word to the spam score
    for keyword in SPAM_KEYWORDS:
        if keyword in message:
            spam_score += 1
            spam_keywords.append(keyword)

    return spam_score, spam_keywords

# calculate the likelihood that the message is spam
def spam_likelihood(spam_score):
    if spam_score == 0:
        return "Not spam."
    elif spam_score <= 3:
        return "Could be spam."
    elif spam_score <= 5:
        return "Most likely spam."
    else:
        return "Almost certainly spam."

def main():
    # prompt the user to enter a message to test for spam keywords
    user_message = input("Enter your email:\n")

    spam_score, keywords = calculate_spam_score(user_message)
    likelihood = spam_likelihood(spam_score)

    # display the spam check results
    print("\n--- Spam Check Results ---")
    print("Spam Score:", spam_score)
    print("Likelihood:", likelihood)
    if keywords:
        print("Spammy keywords/phrases:")
        for word in keywords:
            print(word)
    else:
        print("No spam keywords detected.")

if __name__ == "__main__":
    main()