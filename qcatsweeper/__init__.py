import qiskit


def qconfig():
    """
    Function to return the configuration dictionary containing API token and URL.
    """
    return {
        "APItoken": "qHxoENwF0FqqNFaBcfdfdSJYEoXZlAp7GrYqxtejKuvaaltadNlmVw9BxaSo6DUc",
        "url": "https://auth.quantum-computing.ibm.com/api/"
    }

# Obtain the configuration from the qconfig function
config = qconfig()

# Use the configuration to register with Qiskit
qiskit.register(config['APItoken'], config["url"])


