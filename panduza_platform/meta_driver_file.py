import json
from loguru import logger
from .meta_driver import MetaDriver


class MetaDriverFile(MetaDriver):
    """Abstract Driver with helper class to manage file interface
    """

    def push_content(self, content, mime):
        """To publish content
        """
        payload_dict = {
            "data": content, "mime": mime
        }
        self.push_attribute("content", json.dumps(payload_dict), retain=True)

