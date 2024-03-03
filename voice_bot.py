from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
from rasa.core.channels.socketio import SocketIOInput

# Load the trained NLU model
interpreter = RasaNLUInterpreter("models/nlu/")

# Define the action endpoint URL
action_endpoint = EndpointConfig(url="http://localhost:5000/webhook")

# Load the trained dialogue model
agent = Agent.load("models/dialogue/", interpreter=interpreter, action_endpoint=action_endpoint)

# Initialize SocketIO input channel
input_channel = SocketIOInput(
    # Define the channel name
    user_message_evt="user_uttered",
    # Define the namespace
    namespace="/chat",
    # Define the socket.io server URL
    socketio_path="/socket.io/",
    # Define the credentials if authentication is required
    # credentials={"username": "rasa", "password": "password"},
)

# Start the Rasa server with the configured input channel
agent.handle_channels([input_channel], http_port=5005)
