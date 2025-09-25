from bs4 import BeautifulSoup

def parse_html(file_path: str) -> str:
    """
    extracts visible text from an HTML file
    
    args:
        file_path (str): path to the HTML file
    
    returns:
        str: extracted text as a single string
    """
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    return text