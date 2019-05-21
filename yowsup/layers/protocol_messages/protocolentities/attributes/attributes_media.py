from yowsup.layers.protocol_messages.protocolentities.attributes.attributes_context_info import ContextInfoAttributes


class MediaAttributes(object):
    def __init__(self, context_info=None):
        """
        :type context_info: ContextInfo | None
        """
        if context_info:
            self.context_info = context_info  # type: ContextInfoAttributes | None

    @property
    def context_info(self):
        return self._context_info

    @context_info.setter
    def context_info(self, value):
        assert type(value) is ContextInfoAttributes, type(value)
        self._context_info = value
