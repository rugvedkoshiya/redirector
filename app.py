from dotenv import load_dotenv
load_dotenv()


from swaggerConfig import app
from config import Config as SETTING
import os
import routes.main_route


if __name__ == "__main__":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    app.run(host=SETTING.HOST, port=SETTING.PORT, debug=SETTING.DEBUG)
