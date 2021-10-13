roy={"conversation":"talk","ABNORMAL":"not normal, average, typical, or usual; deviating from a standard:","Mahabharata":"an epic poem of India dealing mainly with the conflict between the Pandavas and the Kauravas, with many digressions: includes the Bhagavad-Gita.","dance":"to move one's feet or body, or both, rhythmically in a pattern of steps, especially to the accompaniment of music."}
print("search your word here :" )
word = input()
roy.get(word)
print("meaning of this word is",roy[word])