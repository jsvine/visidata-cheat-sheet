# Based on https://gist.github.com/pypt/94d747fe5180851196eb
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode
from yaml import SafeLoader

class UniqueKeyLoader(SafeLoader):
    def construct_mapping(self, node, deep=False):
        if not isinstance(node, MappingNode):
            raise ConstructorError(None, None,
                    "expected a mapping node, but found %s" % node.id,
                    node.start_mark)
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                hash(key)
            except TypeError as exc:
                raise ConstructorError("while constructing a mapping", node.start_mark,
                       "found unacceptable key (%s)" % exc, key_node.start_mark)
            # check for duplicate keys
            if key in mapping:
                raise ConstructorError("while constructing a mapping", node.start_mark,
                       "found duplicate key", key_node.start_mark)
            value = self.construct_object(value_node, deep=deep)
            mapping[key] = value
        return mapping
