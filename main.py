from api import app
import os

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))
    app.run()