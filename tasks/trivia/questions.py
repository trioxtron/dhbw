from Question import Question

question_list = [
    # Geography
    Question("What is the capital of France?", "Paris", ["London", "Paris", "Berlin", "Madrid"]),
    Question("What is the capital of Italy?", "Rome", ["London", "Paris", "Berlin", "Rome"]),
    Question("Which country has Tokyo as its capital?", "Japan", ["China", "South Korea", "Japan", "Vietnam"]),
    Question("Which continent is home to the Sahara Desert?", "Africa", ["Africa", "Asia", "Australia", "South America"]),
    Question("What is the tallest mountain in the world?", "Mount Everest", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"]),
    Question("Which river is the longest in the world?", "Nile", ["Amazon", "Yangtze", "Nile", "Mississippi"]),
    Question("What is the smallest country in the world?", "Vatican City", ["Monaco", "Vatican City", "San Marino", "Liechtenstein"]),
    Question("Which country is known as the Land of the Rising Sun?", "Japan", ["China", "Japan", "South Korea", "Thailand"]),
    Question("Which ocean is the largest?", "Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"]),
    Question("What is the capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Canberra", "Perth"]),
    
    # Science
    Question("What is the chemical symbol for gold?", "Au", ["Ag", "Au", "Pb", "Fe"]),
    Question("Which planet is the largest in our solar system?", "Jupiter", ["Saturn", "Earth", "Mars", "Jupiter"]),
    Question("What is the boiling point of water in Celsius?", "100", ["90", "100", "120", "80"]),
    Question("Which part of the cell contains the genetic material?", "Nucleus", ["Ribosome", "Nucleus", "Cytoplasm", "Mitochondria"]),
    Question("What is the hardest natural substance on Earth?", "Diamond", ["Gold", "Iron", "Diamond", "Quartz"]),
    Question("What type of blood type is known as the universal donor?", "O Negative", ["A Positive", "O Negative", "B Negative", "AB Positive"]),
    Question("What is the main gas found in the Earth's atmosphere?", "Nitrogen", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"]),
    Question("What does DNA stand for?", "Deoxyribonucleic Acid", ["Deoxyribonucleic Acid", "Deoxyribosomal Acid", "Nucleic Acid", "Ribonucleic Acid"]),
    Question("How many bones are in the adult human body?", "206", ["206", "208", "210", "200"]),
    Question("What is the process by which plants make their food?", "Photosynthesis", ["Respiration", "Photosynthesis", "Transpiration", "Fertilization"]),

    # History
    Question("Who was the first President of the United States?", "George Washington", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"]),
    Question("In what year did the Titanic sink?", "1912", ["1905", "1912", "1921", "1930"]),
    Question("Who discovered America?", "Christopher Columbus", ["Amerigo Vespucci", "Leif Erikson", "Christopher Columbus", "James Cook"]),
    Question("Which war was fought between the North and South regions in the United States?", "Civil War", ["World War I", "Civil War", "Revolutionary War", "Korean War"]),
    Question("Who wrote the Declaration of Independence?", "Thomas Jefferson", ["Benjamin Franklin", "Thomas Jefferson", "George Washington", "John Adams"]),
    Question("Which ancient civilization built the Colosseum?", "Romans", ["Greeks", "Egyptians", "Romans", "Persians"]),
    Question("What year did World War I begin?", "1914", ["1914", "1918", "1939", "1945"]),
    Question("Who was the first man to step on the moon?", "Neil Armstrong", ["Buzz Aldrin", "Neil Armstrong", "Michael Collins", "Yuri Gagarin"]),
    Question("What was the name of the first successful airplane?", "Wright Flyer", ["Wright Flyer", "Spirit of St. Louis", "Concorde", "Zeppelin"]),
    Question("What city was famously destroyed by Mount Vesuvius in AD 79?", "Pompeii", ["Pompeii", "Herculaneum", "Naples", "Rome"]),

    # Pop Culture
    Question("Who directed 'Titanic' and 'Avatar'?", "James Cameron", ["Steven Spielberg", "James Cameron", "Christopher Nolan", "Peter Jackson"]),
    Question("What is the name of Batman's butler?", "Alfred", ["Jarvis", "Alfred", "Bernard", "James"]),
    Question("Who wrote the Harry Potter series?", "J.K. Rowling", ["J.K. Rowling", "J.R.R. Tolkien", "George R.R. Martin", "Suzanne Collins"]),
    Question("What is the highest-grossing movie of all time (as of 2023)?", "Avatar", ["Titanic", "Avatar", "Avengers: Endgame", "The Lion King"]),
    Question("Who is known as the King of Pop?", "Michael Jackson", ["Elvis Presley", "Michael Jackson", "Prince", "David Bowie"]),
    Question("What video game franchise features a character named Link?", "The Legend of Zelda", ["Mario", "The Legend of Zelda", "Pokemon", "Final Fantasy"]),
    Question("Which superhero is also known as the Man of Steel?", "Superman", ["Batman", "Superman", "Iron Man", "Hulk"]),
    Question("What year was the first iPhone released?", "2007", ["2005", "2006", "2007", "2008"]),
    Question("What is the name of the main protagonist in 'Breaking Bad'?", "Walter White", ["Jesse Pinkman", "Walter White", "Gus Fring", "Hank Schrader"]),
    Question("Which musician famously performed at the Super Bowl in 2020?", "Shakira and Jennifer Lopez", ["Beyoncé", "Shakira and Jennifer Lopez", "Lady Gaga", "Rihanna"]),

    # Literature
    Question("Who wrote 'Romeo and Juliet'?", "William Shakespeare", ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"]),
    Question("What is the first book in the 'Lord of the Rings' series?", "The Fellowship of the Ring", ["The Hobbit", "The Fellowship of the Ring", "The Two Towers", "Return of the King"]),
    Question("Who wrote '1984'?", "George Orwell", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Isaac Asimov"]),
    Question("What is the name of Sherlock Holmes' assistant?", "Dr. Watson", ["Dr. Watson", "Inspector Lestrade", "Mycroft Holmes", "Irene Adler"]),
    Question("Who wrote 'Pride and Prejudice'?", "Jane Austen", ["Charlotte Bronte", "Jane Austen", "Emily Bronte", "Louisa May Alcott"]),
    Question("What is the setting of 'The Great Gatsby'?", "Long Island", ["Long Island", "New York City", "Boston", "Chicago"]),
    Question("Which character said, 'All the world’s a stage'?", "Jacques", ["Hamlet", "Jacques", "Macbeth", "Prospero"]),
    Question("Who wrote 'Moby Dick'?", "Herman Melville", ["Herman Melville", "Mark Twain", "Nathaniel Hawthorne", "Edgar Allan Poe"]),
    Question("What is the name of the boy in 'The Jungle Book'?", "Mowgli", ["Tarzan", "Mowgli", "Baloo", "Bagheera"]),
    Question("Who wrote 'The Catcher in the Rye'?", "J.D. Salinger", ["F. Scott Fitzgerald", "J.D. Salinger", "Ernest Hemingway", "John Steinbeck"]),

    # Miscellaneous
    Question("What is the currency of the United Kingdom?", "Pound Sterling", ["Euro", "Dollar", "Pound Sterling", "Yen"]),
    Question("How many colors are there in a rainbow?", "Seven", ["Five", "Six", "Seven", "Eight"]),
    Question("Which zodiac sign is represented by the scales?", "Libra", ["Virgo", "Libra", "Scorpio", "Aquarius"]),
    Question("What does WWW stand for in a web address?", "World Wide Web", ["Wide Web World", "World Wide Web", "Web Wide World", "Wide Wide Web"]),
    Question("Which chess piece can move in an 'L' shape?", "Knight", ["Knight", "Rook", "Bishop", "Pawn"]),
    Question("What is the capital of Canada?", "Ottawa", ["Toronto", "Vancouver", "Ottawa", "Montreal"]),
    Question("What is the largest planet in our solar system?", "Jupiter", ["Saturn", "Earth", "Mars", "Jupiter"]),
] 
