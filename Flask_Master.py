from flask import Flask,render_template
app = Flask(__name__)
def hello():
    main_data = {
        'Город':'чебоксары',
        'Район':'Московский',
        'Компания':'iserv'
    }
    context = {
      'name':'Kostya',
      'age':'26',
       'spes':'dev'

    }
    spisok = ('список')
    return render_template(template_name_or_list='index.html',main_data=main_data,context=context)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/сontacts/")
def contacts():
    developer_name = 'Ilon Mask'
    developer_phone = '88005553535'
    developer_adress = ('Улица Карла Маркса 52 Чебоксары Чувашская Республика')
    return render_template(template_name_or_list='contacts.html',name = developer_name)
@app.route("/results/")
def results():
    data = ''
    return render_template(template_name_or_list='results.html',data=data)

if __name__ == "__main__":
    app.run(debug= True)
