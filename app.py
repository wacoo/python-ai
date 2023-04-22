# Start with an empty dictionary to hold user inputs and responses
responses = {}

# Loop forever until the user enters 'quit'
while True:
    # Get user input and clean it up by converting to lowercase and removing extraneous whitespace
    user_input = input('You: ').strip().lower()

    # If the user enters 'quit', exit the program
    if user_input == 'quit':
        break

    # If the user has entered input before, retrieve the corresponding response
    if user_input in responses:
        bot_response = responses[user_input]
    # If this is a new input, ask the user what the response should be and store it in our dictionary
    else:
        bot_response = input('Bot: What should I say in response? ')
        responses[user_input] = bot_response

    # Display the bot's response to the user
    print('Bot:', bot_response)