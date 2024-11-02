from dotenv import load_dotenv
load_dotenv()

from portal import app

if __name__ == "__main__":
    app.run(host='0.0.0.0')
