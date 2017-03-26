from flask import Flask, render_template,  request
from models.validation import Startwith, Exactly16, Digits,Group4, Consecutive
from models.forms import CredCarForm

app = Flask(__name__)
app.secret_key = 'LINUX@162'

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cred', methods=["GET","POST"])
def cred_card():

    form = CredCarForm()
    if request.method == 'POST':


        cardNumber = form.cardNumber.data
        options =  dict(form.options.choices).get(form.options.data)
        st = Startwith()
        Ex = Exactly16()
        Dg = Digits()
        G4 = Group4()
        Cs= Consecutive()
        Sp = Group4()
        print(options)
        resposta = ''

        if options == 'start with a 4, 5 or 6':
            resposta = st.validate(cardNumber)

        elif options == 'contain exactly 16 digits':
             resposta = Ex.validate(cardNumber)

        elif options == 'consist of digits (0-9)':
             resposta = Dg.validate(cardNumber)

        elif options == 'have digits in groups of 4, separated by one hyphen -':
            resposta = G4.validate(cardNumber)

        elif options == "NOT use any other separator like ' ' , '_'":
            resposta = Sp.validate(cardNumber)

        elif options == 'NOT have 4 or more consecutive repeated digit':
             resposta = Cs.validate(cardNumber)
        else:
            resposta='No opsion select'


        form.result.data = str(resposta)




    return render_template('credcard.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
