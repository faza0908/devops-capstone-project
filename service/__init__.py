"""
Package initialization for the Accounts Service.
"""
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service.common import log_handlers

# Create the Flask app
app = Flask(__name__)

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T S   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

######################################################################
# Configure Security Headers with Talisman
######################################################################
talisman = Talisman(app)

######################################################################
# Configure CORS Policies
######################################################################
CORS(app)

try:
    from service import routes  # noqa: F401, E402
    from service.common import error_handlers  # noqa: F401, E402
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    import sys
    sys.exit(4)

app.logger.info("Service initialized!")
