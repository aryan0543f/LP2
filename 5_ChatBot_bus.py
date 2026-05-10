
import re

def chatbot_response(user_input):
    # Normalize input: lowercase + remove extra whitespace
    user_input = user_input.lower().strip()

    # Dictionary of regex patterns mapped to responses
    # \b = word boundary ensures whole-word matching
    # |  = OR operator to match multiple keywords per intent
    responses = {
        r"\b(1|hello|hi|hey)\b":                    "Hello! Welcome to RedBus. How can I assist you today?",
        r"\b(2|how are you)\b":                     "I'm doing great! I'm here to help you book your bus tickets.",
        r"\b(3|book ticket|bus booking|book bus)\b":"Sure! Please provide your departure and destination cities.",
        r"\b(4|cancel ticket|cancellation)\b":      "You can cancel your ticket from 'My Bookings' section. Need help with it?",
        r"\b(5|refund status|refund)\b":            "Refunds are processed within 5-7 working days after cancellation.",
        r"\b(6|available buses|search buses)\b":    "Please provide your source, destination, and date of journey.",
        r"\b(7|ticket price|fare)\b":               "Ticket prices vary by route and bus type. Please specify your route.",
        r"\b(8|offers|discounts)\b":                "We have exciting discounts! Use code 'BUS10' to get 10% off on your first booking.",
        r"\b(9|payment options|payment methods)\b": "We accept UPI, credit/debit cards, net banking, and wallets.",
        r"\b(10|bus timings|departure time)\b":     "Please tell me the route so I can share available timings.",
        r"\b(11|customer care|support)\b":          "You can contact our customer care at 1800-123-1234.",
        r"\b(12|track bus|live location)\b":        "Tracking is available 1 hour before the scheduled departure.",
        r"\b(13|luggage policy|baggage)\b":         "Most buses allow up to 15kg of luggage per passenger.",
        r"\b(14|sleeper bus|ac bus|non ac bus)\b":  "Yes, we have AC, Non-AC, Sleeper, and Semi-Sleeper buses. Please specify your preference!",
        r"\b(15|rating|reviews)\b":                 "You can check bus ratings and customer reviews before booking.",
        r"\b(16|reschedule ticket|change journey)\b":"Some buses allow rescheduling. Would you like me to check for your ticket?",
        r"\b(17|popular routes)\b":                 "Popular routes include Mumbai-Pune, Bangalore-Chennai, Delhi-Jaipur, and more!",
        r"\b(18|bus operator|travel agency)\b":     "We partner with top bus operators like VRL, SRS, KSRTC, and more.",
        r"\b(19|bye|exit)\b":                       "Goodbye! Safe travels! 🚌"
    }

    # Check each pattern against user input
    for pattern, response in responses.items():
        if re.search(pattern, user_input):  # re.search finds match anywhere in string
            return response

    # Default fallback response if no pattern matches
    return "I'm sorry, I couldn't understand that. Could you please rephrase or ask something about RedBus services?"


# =============================================================================
# MAIN CHATBOT INTERACTION LOOP
# =============================================================================
print("Welcome to the RedBus Chatbot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:     # Exit condition
        print("Chatbot: Goodbye! Safe travels!")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)


# SAMPLE CONVERSATION:
# --------------------
# You: hello
# Chatbot: Hello! Welcome to RedBus. How can I assist you today?
#
# You: book ticket
# Chatbot: Sure! Please provide your departure and destination cities.
#
# You: refund
# Chatbot: Refunds are processed within 5-7 working days after cancellation.
#
# You: what is the weather
# Chatbot: I'm sorry, I couldn't understand that. Could you please rephrase...
#
# You: bye
# Chatbot: Goodbye! Safe travels!

# =============================================================================
# PROGRAM: Rule-Based Chatbot — RedBus Customer Service
# =============================================================================
#
# THEORY:
# -------
# Chatbot:
#   - A software application designed to simulate human conversation.
#   - Can be text-based or voice-based.
#   - Types of Chatbots:
#       1. Rule-Based  : Uses predefined rules/patterns (THIS PROGRAM)
#       2. AI-Based    : Uses ML/NLP models (e.g., GPT, BERT)
#       3. Hybrid      : Combination of both
#
# Rule-Based Chatbot:
#   - Matches user input against predefined PATTERNS (regex).
#   - Returns a fixed RESPONSE for each matched pattern.
#   - Simple, fast, and predictable.
#   - Cannot handle queries outside predefined rules.
#
# Regular Expressions (Regex):
#   - A sequence of characters that defines a search pattern.
#   - Used here to match keywords in user input.
#   - \b  → word boundary (ensures whole word match)
#   - |   → OR operator (matches any of the alternatives)
#   - re.search() → scans the string for the first location where pattern matches
#
# HOW THIS CHATBOT WORKS:
#   1. User types a message.
#   2. Input is converted to lowercase and stripped of whitespace.
#   3. Each regex pattern in the dictionary is checked against the input.
#   4. First matching pattern → return its response.
#   5. No match → return default "I'm sorry" response.
#
# =============================================================================
# COMPLEXITY:
#   Time Complexity  : O(P × L) — P = number of patterns, L = length of input
#   Space Complexity : O(P)     — P = number of pattern-response pairs stored
# =============================================================================
#
# CHATBOT MENU (19 intents supported):
#   1.  Hello / Hi / Hey
#   2.  How are you
#   3.  Book ticket / Bus booking
#   4.  Cancel ticket / Cancellation
#   5.  Refund status
#   6.  Available buses / Search buses
#   7.  Ticket price / Fare
#   8.  Offers / Discounts
#   9.  Payment options
#   10. Bus timings / Departure time
#   11. Customer care / Support
#   12. Track bus / Live location
#   13. Luggage policy / Baggage
#   14. Sleeper bus / AC bus / Non-AC bus
#   15. Rating / Reviews
#   16. Reschedule ticket
#   17. Popular routes
#   18. Bus operator / Travel agency
#   19. Bye / Exit
#
# =============================================================================
# ORAL EXAM QUESTIONS & ANSWERS:
# =============================================================================
#
# Q1. What is a Chatbot?
# A1. A chatbot is a software program that simulates human conversation
#     through text or voice. It responds to user queries automatically
#     based on rules or AI models.
#
# Q2. What type of chatbot is this?
# A2. This is a RULE-BASED chatbot. It uses predefined regex patterns
#     to match user input and returns fixed responses.
#     It does NOT use machine learning or NLP.
#
# Q3. What is the difference between Rule-Based and AI-Based chatbots?
# A3. Rule-Based: Uses fixed patterns/rules. Fast, predictable, limited scope.
#                 Cannot handle unknown queries.
#     AI-Based:   Uses ML/NLP (e.g., GPT, BERT). Understands context,
#                 handles varied inputs, learns from data. More complex.
#
# Q4. What is a Regular Expression (Regex)?
# A4. A regex is a pattern used to match text strings.
#     In this program, regex patterns like r"\b(hello|hi|hey)\b" match
#     specific keywords in user input to identify the user's intent.
#
# Q5. What does \b mean in regex?
# A5. \b is a word boundary anchor. It ensures the pattern matches a
#     WHOLE WORD and not a substring.
#     Example: \bhello\b matches "hello" but NOT "helloworld".
#
# Q6. What does re.search() do?
# A6. re.search(pattern, string) scans through the string and returns
#     a match object if the pattern is found ANYWHERE in the string.
#     Returns None if no match is found.
#
# Q7. Why is user_input converted to lowercase?
# A7. To make the matching CASE-INSENSITIVE.
#     "Hello", "HELLO", and "hello" all become "hello" after .lower(),
#     ensuring the regex pattern matches regardless of how the user types.
#
# Q8. What does .strip() do?
# A8. .strip() removes leading and trailing whitespace from the string.
#     This prevents mismatches caused by accidental spaces in user input.
#
# Q9. What is an "intent" in a chatbot?
# A9. An intent is the PURPOSE or GOAL behind a user's message.
#     Example: "book ticket" → intent is BOOKING.
#     This chatbot has 19 predefined intents.
#
# Q10. What happens when no pattern matches the user input?
# A10. The function returns a default fallback response:
#      "I'm sorry, I couldn't understand that. Could you please rephrase..."
#      This handles all unrecognized inputs gracefully.
#
# Q11. What data structure stores the patterns and responses?
# A11. A Python DICTIONARY where:
#      Key   = regex pattern string
#      Value = response string
#      The dictionary is iterated to find the first matching pattern.
#
# Q12. What is the | operator in regex?
# A12. The | is the OR operator in regex.
#      r"\b(hello|hi|hey)\b" matches "hello" OR "hi" OR "hey".
#      It allows multiple keywords to map to the same response.
#
# Q13. What are the limitations of this rule-based chatbot?
# A13. - Cannot understand context or conversation history.
#      - Cannot handle typos or spelling mistakes.
#      - Only responds to predefined patterns — no flexibility.
#      - Cannot learn or improve from interactions.
#      - Fails on complex or multi-intent queries.
#
# Q14. How would you improve this chatbot?
# A14. - Add NLP (Natural Language Processing) for better understanding.
#      - Use ML models (intent classification, entity recognition).
#      - Add context/session management for multi-turn conversations.
#      - Integrate with a database for real-time bus data.
#      - Use fuzzy matching to handle typos.
#
# Q15. What is NLP and how does it relate to chatbots?
# A15. NLP (Natural Language Processing) is a branch of AI that enables
#      computers to understand and process human language.
#      AI chatbots use NLP for intent detection, entity extraction,
#      sentiment analysis, and generating natural responses.
#
# Q16. What is the time complexity of this chatbot?
# A16. O(P × L) where P = number of patterns (19 here) and
#      L = length of user input. Each pattern is checked against the input.
#
# Q17. What is the domain of this chatbot?
# A17. This is a DOMAIN-SPECIFIC chatbot for RedBus — an online bus
#      ticket booking platform. It only handles bus-related queries.
#
# Q18. What is the difference between re.search() and re.match()?
# A18. re.match()  → matches pattern only at the BEGINNING of the string.
#      re.search() → matches pattern ANYWHERE in the string.
#      re.search() is used here to find keywords anywhere in the input.
#
# =============================================================================
# QUICK FIRE ANSWERS:
#   Chatbot type?            → Rule-Based
#   Pattern matching tool?   → Regular Expressions (re module)
#   \b in regex?             → Word boundary
#   re.search() returns?     → Match object or None
#   .lower() purpose?        → Case-insensitive matching
#   .strip() purpose?        → Remove leading/trailing whitespace
#   Data structure used?     → Dictionary (pattern → response)
#   Number of intents?       → 19
#   Fallback response?       → "I'm sorry, I couldn't understand that..."
#   Can it learn?            → No, it's rule-based (no ML)
#   Time complexity?         → O(P × L)
# =============================================================================
