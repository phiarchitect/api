"""
run the main app
"""
from .phiarchitect_api import Phiarchitect_api


def run() -> None:
    reply = Phiarchitect_api().run()
    print(reply)
