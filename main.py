import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("amazon.csv")
df.drop_duplicates()

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df['discounted_price'] = df['discounted_price'].str.replace("₹", "").str.replace(",", "").astype(float)
df['actual_price'] = df['actual_price'].str.replace("₹", "").str.replace(",", "").astype(float)
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)

# print(df['rating'].value_counts())
# print(df.query('rating == "|"'))
df["rating"] = df["rating"].replace("|", pd.NA).astype(float)
df["rating"] = df["rating"].fillna(df["rating"].mean())
# print(df['rating'].describe())
# print(df["rating"].value_counts())
df["rating_count"] = df["rating_count"].str.replace(",", "").str.strip().astype(float)
df["rating_count"] = df["rating_count"].fillna(df["rating_count"].mean())


# Q1: What is the average rating for each product category?

average_rating = df.groupby("category")["rating"].mean()
print(average_rating)

# Q2: What are the top rating_count products by category??
top_rated_products = df.groupby("category").apply(lambda x: x.nlargest(5, "rating_count"))
print(top_rated_products)

# Q3: What is the distribution of discounted prices vs. actual prices??
# Create histograms
df["discounted_price"].hist(label="Discounted Price")
df["actual_price"].hist(label="Actual Price")

# Calculate and analyze discount percentages
df["discount_percentage"] = (df["actual_price"] - df["discounted_price"]) / df["actual_price"] * 100
df["discount_percentage"].describe()
df["discount_percentage"].hist(label="Discount Percentage")
# plt.show()


# Q4: How does the average discount percentage vary across categories?

# average_discount_percentage = df.groupby("category")["discount_percentage"].mean()
# sns.histplot(x=average_discount_percentage.index, y=average_discount_percentage.values)
# plt.xlabel("Category")
# plt.ylabel("Average Discount Percentage")
# plt.title("Average Discount Percentage by Category")
# plt.show()

# Q5: What are the most popular product name?
most_popular_product_names = df["product_name"].value_counts().head(10)
print(most_popular_product_names.sort_values(ascending=False))

    

# Q6: What are the most popular product keywords?
def extract_keywords(product_name):
  """Extracts keywords from a product name, handling potential numbers."""
  if isinstance(product_name, str):  # Check if it's a string
    keywords = product_name.lower().split()  # Split into words and lowercase
    keywords = [word for word in keywords if word.isalpha()]  # Remove non-alphabetical characters
  else:
    keywords = []  # Handle non-string values (e.g., integers) by returning an empty list
  return keywords

# Apply the function to extract keywords
df["keywords"] = df["product_name"].apply(extract_keywords)

# Flatten the list of keywords
all_keywords = [keyword for keywords in df["keywords"] for keyword in keywords]

# Count keyword occurrences
keyword_counts = pd.Series(all_keywords).value_counts()

# Display the top 10 most popular keywords
print(keyword_counts.head(10))




# Q7: What are the most popular product reviews?
# most_popular_reviews = df["review_content"].value_counts().head(10)
# print(most_popular_reviews)


# Q8: What is the correlation between discounted_price and rating?
correlation = df["discounted_price"].corr(df["rating"])
print(f"Correlation between discounted price and rating: {correlation}")


# Q9: What are the Top 5 categories based with highest ratings?
top_categories = df.groupby("category")["rating"].mean().nlargest(5)
print(top_categories)

    
