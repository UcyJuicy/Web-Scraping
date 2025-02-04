import pandas as pd
import matplotlib.pyplot as plt


# Load cleaned CSV file
df = pd.read_csv("quotes_cleaned.csv")

# Count occurrences of each author
author_counts = df["Author"].value_counts().head(10)  # Top 10 authors

# Plot bar chart
plt.figure(figsize=(10,5))
author_counts.plot(kind="bar", color="skyblue")

# Add labels and title
plt.xlabel("Authors")
plt.ylabel("Number of Quotes")
plt.title("Top 10 Most Frequent Authors in Quotes")
plt.xticks(rotation=45)  # Rotate x labels
plt.show()

from wordcloud import WordCloud

# Combine all quotes into one large text
all_quotes = " ".join(df["Quote"])

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_quotes)

# Display word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Hide axis
plt.title("Most Common Words in Quotes")
plt.show()
