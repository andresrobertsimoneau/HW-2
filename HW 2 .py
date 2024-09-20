#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 
# *This is the answer CoPilot gave to explaining the code below:
# 
# *"This code simulates the Monty Hall problem, a famous probability puzzle. Here's a step-by-step explanation:
# 
# 1. **Initialization**:
#    - `all_door_options` is a tuple representing the three doors.
#    - `my_door_choice` is initially set to door 1.
#    - `i_won` keeps track of the number of times you win.
#    - `reps` is the number of repetitions for the simulation (100,000).
# 
# 2. **Simulation Loop**:
#    - The loop runs `reps` times to simulate the game multiple times.
# 
# 3. **Choosing the Winning Door**:
#    - `secret_winning_door` is randomly chosen from the three doors.
# 
# 4. **Removing Doors**:
#    - Convert `all_door_options` to a list for easier manipulation.
#    - Remove the `secret_winning_door` from the list.
#    - Try to remove `my_door_choice` from the list. If it's already removed (because it's the winning door), the `except` block handles it.
# 
# 5. **Revealing a Goat Door**:
#    - Randomly choose a door to reveal as a goat door from the remaining options.
#    - Remove this goat door from the list.
# 
# 6. **Restoring the Winning Door**:
#    - If the `secret_winning_door` is not the same as `my_door_choice`, add it back to the list.
# 
# 7. **Swapping Doors**:
#    - Change `my_door_choice` to the remaining door in the list.
# 
# 8. **Checking for a Win**:
#    - If `my_door_choice` matches the `secret_winning_door`, increment `i_won`.
# 
# 9. **Calculating Win Rate**:
#    - After the loop, `i_won/reps` gives the proportion of times you won by switching doors.
# 
# This simulation demonstrates that switching doors increases your chances of winning to about 2/3, compared to sticking with your initial choice, which has a 1/3 chance of winning. This aligns with the theoretical solution to the Monty Hall problem. If you have any questions or need further clarification, feel free to ask!"

# # Question 2 & 3

# In[6]:


import numpy as np
#prints tuple of doors
all_door_options = (1, 2, 3)
#the door choice chosen
my_door_choice = 1
#number of times won, we obviously start off with 0 wins
i_won = 0
#number of times we do the simulation
reps = 100000

for _ in range(reps):
    #the winning door is randomely chosen from the tuple
    secret_winning_door = np.random.choice(all_door_options)
    #creates a list of doors excluding doors chosen by the player and the winning door
    remaining_doors = [door for door in all_door_options if door != my_door_choice and door != secret_winning_door]
    #randomly chosen door in the remaining_doors list is chosen as goat door
    goat_door_reveal = np.random.choice(remaining_doors)
    #updates the player's door choice to be the remaning door that excludes their original choice & the goat 
    my_door_choice = next(door for door in all_door_options if door != my_door_choice and door != goat_door_reveal)
    
    if my_door_choice == secret_winning_door:
        i_won += 1

#calculates our win percentage
win_rate = i_won / reps
#prints our win percentage
print(win_rate)


# *Here is a summary of my session given by CoPilot:
# 
# *Sure! Here's a summary of our interactions:
# 
# 1. **Monty Hall Problem Code Explanation**:
#    - You shared a Python code snippet simulating the Monty Hall problem.
#    - I explained the code step-by-step, highlighting the purpose of each part of the code.
# 
# 2. **Tuple and Reps**:
#    - You asked about tuples and the term `reps`.
#    - I explained that a tuple is an immutable collection of items, and `reps` stands for repetitions, indicating the number of times the simulation runs.
# 
# 3. **Importing NumPy**:
#    - You inquired about the `import numpy` statement.
#    - I explained that it imports the NumPy library, which is used for numerical operations, and allows the use of its functions with the alias `np`.
# 
# 4. **Streamlined Code**:
#    - You requested a simpler version of the code for better readability.
#    - I provided a streamlined version of the Monty Hall simulation and explained the improvements in terms of readability and maintainability.
# 
# 5. **List Comprehension Explanation**:
#    - You asked for clarification on the list comprehension used in the streamlined code.
#    - I broke down the list comprehension syntax and explained how it filters out the initial choice and the winning door to reveal a goat door.
# 
# 6. **Summary Request**:
#    - You asked for a summary of our exchanges for your homework assignment.
#    - I provided this summary to encapsulate our discussion.
# 
# If you need any more details or further assistance, feel free to ask! Good luck with your homework!*

# # Question 4

# In[8]:


# Markov Chains and Text Generation
from IPython.display import YouTubeVideo
YouTubeVideo('56mGTszb_iM', width = 550)


# *Here is an explanation given by CoPilot on how the Markovian Chatbox works:
# 
# *Your code looks like it sets up a Markov chain-based chatbot by reading a text document and generating text based on the Markov chain model. Here’s a brief overview of what each part does:
# 
# 1. **Imports and Argument Handling**:
#    - Imports necessary packages.
#    - Checks if the correct number of arguments are provided (text document and history size).
# 
# 2. **Reading and Processing the Text**:
#    - Reads the text document.
#    - Splits the text into words and sends them to a channel.
# 
# 3. **Building the Markov Chain**:
#    - Constructs the Markov chain using the words from the text document.
# 
# 4. **Generating Text**:
#    - Starts from a random state and generates text by transitioning through the Markov chain states.
# 
# 5. **Helper Functions**:
#    - `randomStart`: Selects a random starting state and transitions through the chain to find a more likely state.
#    - `randomTransition`: Chooses the next state based on transition probabilities.
# 
# If you have any specific questions or need help with a particular part of the code, feel free to ask!*

# # Question 5
# 
# *Part 1 & 2: 
# 
# Here was CoPilot's response to the extensions:
# 
# *Sure! Here's a summary of what each extension does:
# 
# ### First Extension
# This extension adds the core functionality for managing states and transitions in a Markov chain:
# - **State Interface**: Defines a comparable state.
# - **StateTransitions**: Stores transitions and probabilities for a given state.
# - **Chain**: Manages the collection of state transitions and provides methods to add entries, normalize probabilities, and look up transitions.
# 
# ### Second Extension
# This extension introduces testing for the `NewChainChan` function:
# - **testingState**: A simple implementation of the `State` interface for testing purposes.
# - **TestNewChainChan**: A test function that verifies the correctness of the `NewChainChan` function by comparing the actual output with expected state transitions and probabilities.
# 
# ### Third Extension
# This extension adds support for text-based states and transitions:
# - **TextState**: Represents a state as a list of words and provides a method to compare these states alphabetically.
# - **NewChainText**: Creates a Markov chain for text states, where each state consists of a sequence of words. It reads words from a channel and constructs states based on the previous `n` words.
# 
# Each extension builds on the previous one, enhancing the functionality and robustness of your Markov chain implementation. If you have any specific questions or need further assistance with any part of these extensions, feel free to ask!*
# 
# &
# 
# The extensions you provided earlier primarily focus on word-based Markov chains and testing those implementations. However, they do lay a solid foundation for implementing character-specific chains and bigrams. Here's how:
# 
# ### Character-Specific Chains
# - **TextState**: This can be adapted to handle sequences of characters instead of words. By changing the type from `[]string` to `[]rune`, you can create states based on characters.
# - **NewChainText**: This function can be modified to read characters from a channel and create states based on sequences of characters.
# 
# ### Bigrams
# - **TextState**: This can be adapted to handle pairs of words (bigrams). You can create a new type, such as `BigramState`, to represent pairs of words.
# - **NewChainText**: This function can be modified to create states based on pairs of words instead of single words.
# 
# Summary:
# 
# Absolutely! Here's a summary of our discussion:
# 
# ---
# 
# ### Summary of Markov Chain Extensions and Implementations
# 
# #### Initial Code
# - **Markovian Chatbot**: The initial code provided implements a basic Markov chain text generator using the `markovchain` package. It reads a text document, builds a Markov chain based on word sequences, and generates text.
# 
# #### First Extension
# - **Core Functionality**: Added the core structures and methods for managing states and transitions in a Markov chain.
#   - **State Interface**: Defines a comparable state.
#   - **StateTransitions**: Stores transitions and probabilities for a given state.
#   - **Chain**: Manages the collection of state transitions and provides methods to add entries, normalize probabilities, and look up transitions.
# 
# #### Second Extension
# - **Testing**: Introduced a test for the `NewChainChan` function using the `testing` package.
#   - **testingState**: A simple implementation of the `State` interface for testing.
#   - **TestNewChainChan**: Verifies the correctness of the `NewChainChan` function by comparing actual output with expected state transitions and probabilities.
# 
# #### Third Extension
# - **Text-Based States**: Added support for text-based states and transitions.
#   - **TextState**: Represents a state as a list of words and provides a method to compare these states alphabetically.
#   - **NewChainText**: Creates a Markov chain for text states, where each state consists of a sequence of words. It reads words from a channel and constructs states based on the previous `n` words.
# 
# #### Character-Specific Chains and Bigrams
# - **Character-Specific Chains**: Adapted the existing code to handle sequences of characters instead of words.
#   - **CharState**: Represents a state as a list of characters.
#   - **NewChainChar**: Creates a Markov chain for character states, reading characters from a channel and constructing states based on sequences of characters.
# - **Bigrams**: Adapted the existing code to handle pairs of words (bigrams).
#   - **BigramState**: Represents a state as a pair of words.
#   - **NewChainBigram**: Creates a Markov chain for bigram states, reading words from a channel and constructing states based on pairs of words.
# 
# ---
# 
# Feel free to use this summary for your homework. If you need any more details or further assistance, just let me know!

# *part 3 CoPilot answer:
# 
# Absolutely! Let's evaluate how your code can be adapted to handle character-specific Markov chains and bigrams.
# 
# ### Character-Specific Markov Chains
# 
# To create a character-specific Markov chain, you need to modify the input processing to work with individual characters instead of words. The current implementation processes words from a text file, but you can adapt it to process characters.
# 
# Here's how you can modify the `NewChainText` function to handle characters:
# 
# ```go
# func NewChainChar(text string, n int) *Chain {
# 	charChan := make(chan State, len(text))
# 	go func() {
# 		for i := 0; i < len(text)-n+1; i++ {
# 			charState := TextState(strings.Split(text[i:i+n], ""))
# 			charChan <- charState
# 		}
# 		close(charChan)
# 	}()
# 	return NewChainChan(charChan)
# }
# ```
# 
# In this version, `NewChainChar` takes a string of text and a history size `n`. It creates states based on sequences of `n` characters and feeds them into the Markov chain.
# 
# ### Bigrams
# 
# For bigrams, you need to ensure that the states represent pairs of words. You can modify the `NewChainText` function to create states based on pairs of words:
# 
# ```go
# func NewChainBigrams(words <-chan string) *Chain {
# 	stateChan := make(chan State)
# 	go func() {
# 		var prevWord string
# 		for word := range words {
# 			if prevWord != "" {
# 				stateChan <- TextState{prevWord, word}
# 			}
# 			prevWord = word
# 		}
# 		close(stateChan)
# 	}()
# 	return NewChainChan(stateChan)
# }
# ```
# 
# In this version, `NewChainBigrams` takes a channel of words and creates states based on consecutive pairs of words (bigrams).
# 
# ### Example Usage
# 
# #### Character-Specific Markov Chain
# 
# ```go
# text := "your input text here"
# chain := NewChainChar(text, 3) // 3-character history
# 
# state := chain.Lookup(TextState{"y", "o", "u"})
# for i := 0; i < 100; i++ {
# 	if state == nil {
# 		break
# 	}
# 	fmt.Print(state.State.(TextState)[2]) // Print the last character of the state
# 	state = chain.Lookup(state.Sample())
# }
# fmt.Println()
# ```
# 
# #### Bigrams
# 
# ```go
# words := strings.Fields("your input text here")
# wordChan := make(chan string, len(words))
# go func() {
# 	for _, word := range words {
# 		wordChan <- word
# 	}
# 	close(wordChan)
# }()
# chain := NewChainBigrams(wordChan)
# 
# state := chain.Lookup(TextState{"your", "input"})
# for i := 0; i < 10; i++ {
# 	if state == nil {
# 		break
# 	}
# 	fmt.Print(state.State.(TextState)[1], " ") // Print the second word of the bigram
# 	state = chain.Lookup(state.Sample())
# }
# fmt.Println()
# ```
# 
# ### Summary
# 
# - **Character-Specific Markov Chains**: By processing individual characters and creating states based on sequences of characters, you can adapt your code to handle character-specific Markov chains.
# - **Bigrams**: By creating states based on pairs of words, you can adapt your code to handle bigrams.
# 
# These modifications should allow your Markov chain implementation to handle both character-specific chains and bigrams effectively. Let me know if you have any questions or need further assistance!
# 
# 

# # Question 6
# 
# Part 1 = ChatBot was helpful regarding the Monty Hall problems for 1, 2, & 3. The Chatbot was able to easily analyze the code given during the tutorials and refine it to make it more efficient. If I had difficulty with understanding a section of the code given, Chatbot was able to simplify it in a way that made it easier to understand. However, it was not as helpful with the Markov questions. This is not necessarily because Chatbot was per-se “not useful” but simply because the questions were more complex and more difficult for me to understand. 
# 
# Part 2 = The Chatbot was frustrating to work with regarding the Markov questions. I felt as if it didn’t necessarily do what I wanted, simply based upon the fact that I did not know how to phrase the analysis question due to the complexity of the code given. However, I believe this would not have been an issue had I understood the code better & understood how to frame the questions.  
# 
# Part 3 = I believe Chatbot is an excellent resource to understand code. It’s able to instantly analyze & explain coding in a way that is easy to understand for inexperienced users such as myself. I also believe it’s a more efficient way of learning code compared to resources such as textbooks or YouTube. However, it can be harder to use when analyzing more complex topics. 
# 

# # Question 7
# 
# Question: *Reflect on your experience interacting with ChatBot and describe how your perception of AI-driven assistance tools in the context of learning coding, statistics, and data science has been evolving (or not) since joining the course*
# 
# Written answer: Prior to taking this course, I had never used Python or had any prior experience with coding. It is safe to assume, that prior to AI's takeoff, coding was traditionally taught with either a textbook or an online resource such as YouTube. I personally believe that AI is significantly more helpful with learning code compared to these other resources. Not only does it give instant explanations that would take minutes or hours to find on YouTube or a textbook, you can reframe or change the explanation infinite times until you understand the material. AI can also instantly fix your code & explain errors that you made along the way (which for a starter like myself, is extremely useful). You cannot do this with other resources and is quite revolutionary in regards to education. Furthermore, the biggest bonus that AI has for me is that it can generate examples or visuals to explain a concept. These factors are extremely important as coding & statistics at times can be quite heavy, and having a conceptual and visual understanding of the core concept is extremely helpful with understanding the logic. 
# 
# The funny thing is that prior to this class, I only used AI to generate fake articles about silly hypothetical events I would randomly think about. It's actually interesting to see that it has a very useful application in education.

# # Question 9
# 
# If I am going to be brutally honest, no I have not. I simply procrasinate a lot and need to improve on this.  

# In[ ]:




