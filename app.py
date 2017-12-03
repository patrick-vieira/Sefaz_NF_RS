import os

from commons import nf_crawler as nf_crawler, html_builder as html

from flask import Flask, render_template, request

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/')
def landing():
    return render_template("/landing.html")


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('results.html', name=user)


@app.route('/nf_sefaz_rs', methods=['GET', 'POST'])
def teste_request():

    url = "'https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx" \
           "?chNFe=43171192665611010130650010003475031829326215" \
           "&nVersao=100" \
           "&tpAmb=1" \
           "&cDest=00709044054" \
           "&dhEmi=323031372d31312d31375432323a32303a33392d30323a3030" \
           "&vNF=51.93" \
           "&vICMS=0.00" \
           "&digVal=6237455657592b536b796964503742596a68514677694a414d6e553d&" \
           "cIdToken=000001&cHashQRCode=7D7C47D3873949E3E3B3512DC0DBE9F1748F3111'"

    url1 = "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx" \
          "?chNFe=43171107718633001665650070003074121007074121" \
          "&nVersao=100" \
          "&tpAmb=1" \
          "&dhEmi=323031372d31312d32355431363a35313a32362d30323a3030" \
          "&vNF=112.77" \
          "&vICMS=0.55" \
          "&digVal=6f466f466c316b432f6e4f454b72453959434a4d7a5a51726941493d" \
          "&cIdToken=000001" \
          "&cHashQRCode=09AE0A5F19114F491F406DDDD96F13D33434AA5B"

    req = request.get_json(silent=True, force=True)

    if request.method == "GET":
        response = nf_crawler.get_data(url)

    if request.method == "POST":
        sefaz_url = "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?"

        url = request.form['qrcode']
        psw = request.form['passwordQR']

        # if psw == 123:
        response = nf_crawler.get_data(url)

    return html.get_products(response)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
