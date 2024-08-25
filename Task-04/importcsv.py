import csv
import requests



def get_books_data(query, max_results=40):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'maxResults': max_results
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def parse_books_data(data):
    books = []
    for item in data.get('items', []):
        volume_info = item.get('volumeInfo', {})
        book = {
            'Title': volume_info.get('title'),
            'Authors': ', '.join(volume_info.get('authors', [])),
            'Publisher': volume_info.get('publisher'),
            'Published Date': volume_info.get('publishedDate'),
            'Description': volume_info.get('description'),
            'Page Count': volume_info.get('pageCount'),
            'Genre': ', '.join(volume_info.get('categories', [])) if volume_info.get('categories') else 'N/A',
            'Language': volume_info.get('language'),
            'Preview Link': volume_info.get('previewLink')
        }
        books.append(book)
    return books

def save_books_to_csv(books):
    with open("book.csv", 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=books[0].keys())
        writer.writeheader()
        for book in books:
            writer.writerow(book)
    print(f"Data saved to book.csv")

if __name__ == "__main__":
    genre = "Money"
    data = get_books_data(genre)
    
    if data:
        books = parse_books_data(data)
        save_books_to_csv(books)
