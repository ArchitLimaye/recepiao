from flask import Flask, render_template, request
app = Flask(__name__)
recipes = [
    {
        'title': 'Spaghetti Fillipino',
        'ingredients': ["2 lbs. Spaghetti noodles", "1 lb. ground pork", "6 ounces luncheon meat, minced", "4 pieces hotdogs or beef franks", "35 ounces Filipino Style Spaghetti Sauce", "1/2 cup shredded cheddar cheese", "1 1/2 cups beef broth", "1 medium onion, minced", "1 teaspoon minced garlic", "Salt and pepper to taste", "3 tablespoons cooking oil"],
        'instructions': '1. Cook spaghetti until al dente...'
    },
    {
        'title': 'Chocolate Chip Cookies',
        'ingredients': ['Flour', 'Sugar', 'Butter', 'Chocolate Chips', 'Egg', 'Vanilla Extract'],
        'instructions': '1. Preheat oven to 350°F...'
    }
]

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/submit_recipe', methods=['GET', 'POST'])
def submit_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients'].split(',')
        instructions = request.form['instructions']
        new_recipe = {'title': title, 'ingredients': ingredients, 'instructions': instructions}
        recipes.append(new_recipe)
        return render_template('submission_success.html')
    return render_template('submit_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
