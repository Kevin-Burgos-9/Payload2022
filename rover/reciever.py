import re

class reciever:
    def __init__ (self):
        pass

    def process_rf_message(self, call_sign : str) -> list[str]:
        """Process an incoming RF command"""

        # Check if there is an incoming RF message
        if self.rf.available():
            # Read the message
            msg : str = self.rf.recv()
            print(f"Received RF message: {msg}")

            msg = msg.strip()

            msg = msg.replace(call_sign, "")

            commands : list[str] = re.findall('..?', msg)

            return commands



            