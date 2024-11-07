from flask import Flask, render_template  
from flask import render_template, request
import random
  
app = Flask(__name__, template_folder='templates')  
  
@app.route("/")  
def web():  
    return render_template('index.html')  

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form.get('choice')
    bot_choice = random.choice(['Камень', 'Бумага', 'Ножницы'])
    
    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == 'Камень' and bot_choice == 'Ножницы') or \
         (user_choice == 'Ножницы' and bot_choice == 'Бумага') or \
         (user_choice == 'Бумага' and bot_choice == 'Камень'):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"
    
    return render_template('result.html', user_choice=user_choice, bot_choice=bot_choice, result=result)


if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port='80')  