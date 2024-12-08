import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS 
import numpy as np
from PIL import Image

# Read the input text
text = open(r'C:\Users\dell\Desktop\Text.txt', mode='r', encoding='utf-8').read() 

# Path to the custom font
path = r'C:\Users\dell\Desktop\LastChristmas_PERSONAL_USE_ONLY.otf'

# Load the image mask
mask = np.array(Image.open(r'C:\Users\dell\Desktop\Ifti.png'))

# Create the WordCloud object with an outline
wc = WordCloud(
    stopwords=STOPWORDS, 
    font_path=path,
    mask=mask, 
    background_color="black",
    max_words=2000, 
    max_font_size=500,
    random_state=42, 
    width=mask.shape[1],
    height=mask.shape[0]
)

# Generate the word cloud
wc.generate(text) 

# Display the word cloud
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')  # Turn off x and y axes
plt.show()