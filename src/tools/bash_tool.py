import logging
import subprocess
from typing import Annotated
from langchain_core.tools import tool
from .decorators import log_io

# Initialize logger
logger = logging.getLogger(__name__)


@tool
@log_io
def bash_tool(
    cmd: Annotated[str, "The bash command to be executed."],
):
    """Use this to execute bash command and do necessary operations."""
    logger.info(f"Executing Bash Command: {cmd}")
    try:
        # Execute the command and capture output
        # Using ["/bin/bash", "-c", cmd] with shell=False is more secure than shell=True
        # as it explicitly specifies the shell to be used and avoids implicit shell parsing.
        result = subprocess.run(
            ["/bin/bash", "-c", cmd],
            shell=False,
            check=True,
            text=True,
            capture_output=True,
        )
        # Return stdout as the result
        return result.stdout
    except subprocess.CalledProcessError as e:
        # If command fails, return error information
        error_message = f"Command failed with exit code {e.returncode}.\nStdout: {e.stdout}\nStderr: {e.stderr}"
        logger.error(error_message)
        return error_message
    except Exception as e:
        # Catch any other exceptions
        error_message = f"Error executing command: {str(e)}"
        logger.error(error_message)
        return error_message


if __name__ == "__main__":
    print(bash_tool.invoke("ls -all"))
