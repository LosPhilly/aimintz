import base64
from flask import Flask, render_template, request
import config
import aicontent
from PIL import Image
import io
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
import os
import json

import secrets


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)

# this is the entry point
application = app

app.config.from_object(config.config['production'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    ai_data = io.BytesIO()
    data_logo = io.BytesIO()
    data_qr = io.BytesIO()

    im1 = Image.open("favicon.png")
    im1.save(data_logo, 'PNG')
    encoded_img_data_logo = base64.b64encode(data_logo.getvalue())

    ## QR Image
    qr = Image.open("QRCode.jpg")
    qr.save(data_qr, 'PNG')
    encoded_img_data_qr = base64.b64encode(data_qr.getvalue())

    sdk = ThirdwebSDK("mumbai")
    # contract = sdk.get_contract("0xc40929b4a5539f8B095e02C1A0F6c9937994D60B")
    # dataURI = contract.call("contractURI")
    # tokenId = contract.call("tokenURI", _tokenId)
    # approval = contract.call("approve", sdk.get_address(web3.eth.accounts), tokenId)

    RPC_URL = "https://matic-mumbai.chainstacklabs.com"
    sdk = ThirdwebSDK(RPC_URL)
    # This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
    PRIVATE_KEY = config.PRIVATE_KEY

    # This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.
    # PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

    # Now you can create a new instance of the SDK with your private key
    sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, "mumbai")

    # Instantiate a new NFT Collection contract as described above.
    NFT_COLLECTION_ADDRESS = "0xc40929b4a5539f8B095e02C1A0F6c9937994D60B"
    nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)

    if request.method == 'POST':
        queryImg = request.form['imageGenerate']
        imgDescription = request.form['imageDescription']
        addressMintTo = request.form['addressLocation']
        # Properties
        prop1 = request.form['imageProp1']
        prop2 = request.form['imageProp2']
        prop3 = request.form['imageProp3']

        # print(query)

        prompt = 'Your AI Image for Title: {}'.format(queryImg)
        openAIImgAnswer = aicontent.imageDescription(imgDescription)
        img = os.path.abspath("aiImg.png")



        imgPrompt = 'Ai Generated Image for: {}'.format(queryImg)

        # Now you can use any of the SDK contract functions including write functions
        # Note that you can customize this metadata however you like
        metadata = NFTMetadataInput.from_json({
            "name": queryImg,
            "description": imgDescription,
            "image": open("aiImg.png", "rb"),
            "properties": {"Art Style": prop1, "Date Minted": prop2, "Artist": prop3}
        })

        nft_collection.mint_to(addressMintTo, metadata)

    ai_img = Image.open("aiImg.png")
    ai_img.save(ai_data, 'PNG')
    encoded_img_ai_data = base64.b64encode(ai_data.getvalue())




    return render_template('index.html', img_ai_data=encoded_img_ai_data.decode('utf-8'), img_data_logo=encoded_img_data_logo.decode('utf-8'), img_data_qr = encoded_img_data_qr.decode('utf-8'), **locals())




if __name__ == '__main__':
    app.run()
