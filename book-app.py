# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the book dataset from CSV
books_data = pd.read_csv('books.csv')

# Streamlit app
def main():
    st.title('Book Recommendation System')

    # User input
    selected_genre = st.selectbox('Select Genre', books_data['genre'].unique())
    selected_author = st.selectbox('Select Author', books_data['author'].unique())

    # Filtering books based on user input
    filtered_books = filter_books(selected_genre, selected_author)

    # Displaying recommended books
    if not filtered_books.empty:
        st.subheader('Recommended Books:')
        st.dataframe(filtered_books[['title', 'author']])
    else:
        st.info('No books found matching the criteria.')

def filter_books(genre, author):
    # Filtering books based on genre and author
    filtered_books = books_data[(books_data['genre'] == genre) & (books_data['author'] == author)]

    # If no books found, recommend all books of the selected genre
    if filtered_books.empty:
        filtered_books = books_data[books_data['genre'] == genre]

    return filtered_books

if __name__ == '__main__':
    main()