from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

sentence1 = "Elon Musk says he needs $1 trillion to control Tesla’s ‘robot army’"
sentence2 = "Tesla stock surged 10% after amazing earnings report."
sentence3 = "The new Cybertruck design is questionable and divisive."
sentence4 = "That was a good movie."

print(f"Analyzing: '{sentence1}'")
scores1 = analyzer.polarity_scores(sentence1)
print(scores1)

print(f"Analyzing: '{sentence2}'")
scores2 = analyzer.polarity_scores(sentence2)
print(scores2)

print(f"Analyzing: '{sentence3}'")
scores3 = analyzer.polarity_scores(sentence3)
print(scores3)

print(f"Analyzing: '{sentence4}'")
scores4 = analyzer.polarity_scores(sentence4)
print(scores4)