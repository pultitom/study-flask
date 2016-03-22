from logging import DEBUG

from app import app
app.run(debug=True)
app.logger.setLevel(DEBUG)
