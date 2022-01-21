# Test Shuffler
### Description
This is a python script that takes at least one text file as an input and creates a cycle of infinitely shuffling questions. Used to practice vocab for new classes.

### Input
It takes text files with the following formatting:
```
key - value
key - value
key - value
...
```

A more concrete example (say, a Spanish-English mapping with the topic of ):
```
el ajo - garlic
el atún - tuna
la cereza - cherry
...
```

(A more concrete example can be viewied in the 2_food_myLab.txt file provided in this repo)

Note: This means that there can be NO dashes in either the keys or the values.

### Features
- Allows the user to store different categories of questions. 
    - Ex: Let's assume a user is using this app to practice Spanish vocab. In a Spanish class, vocab is introduced chapter-by-chapter based on topic. To be concrete, let's say that the first chapter coveres food vocab and the second chapter covers animal vocab. This program allows you to insert separate text files and choose which categorie, ie chapter, to study for. 
- Allow user to inverse the key-value pairings without changing the text file. 
    - Ex: Say as a user, you've cycled through the Spanish->English mappings enough to comfortably translate a Spanish word to English. It is often more difficult to do the contrary (English->Spanish). Thus, it would make sense from a user's point of view to inverse the mappings to do so. 
- Editing categories: The program allows you to delete, rename, and edit the content inside categories.

### To Implmenet
For all my projects, I really like listing out potential features to add. Here are a few for this project:
- [ ] The ability to star questions
    - Often, when reviewing vocab, certain words are harder to remember 
    - Inter-categorical starring (for practicing for finals, for example)
- [ ] A path validator for the text file (see test.py add_cat function for more details)
- [ ] Mix and max categores (without starred words)
- [ ] Don't ask the same question
    - Maybe not twice in a row?
- [ ] Accept more than just a text file
    - Images
    - Word docs
    - Google Drive doc links
    - Maybe certain audio files