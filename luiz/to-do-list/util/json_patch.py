"""Module of interpretation jsonPatch."""
import json


class PatchException(Exception):
    """Exception of interpretation patch."""

    def __init__(self, msg=None):
        """Constructor of class."""
        super(PatchException, self).__init__(msg or "Invalid patch")


def _assert(condition, msg):
    if condition:
        raise PatchException(msg)


def createEntity(entity_class, properties_values):
    """Create new entity of class specified."""
    entity = entity_class()

    for propertie in properties_values:
        setattr(entity, propertie, properties_values[propertie])
    return entity


def verify_entity(func):
    """Decorator for verify if value passed is dict."""
    def params(self, value, entity_class, *args):
        """Receive params of function."""
        if isinstance(value, dict):
            value = createEntity(entity_class, value)
        return func(self, value, entity_class, *args)
    return params


class JsonPatch(object):
    """Class of interpretation and application of jsonPatch."""

    @staticmethod
    def load(json1, obj, entity_class):
        """It loads jsonPatch and applies all operations contained therein."""
        list_patchs = json.loads(json1, encoding="utf-8")

        for dict_patch in list_patchs:
            if dict_patch['op'] == 'test':
                JsonPatch.decode_patch(dict_patch, obj, entity_class)

        for dict_patch in list_patchs:
            if dict_patch['op'] != 'test':
                JsonPatch.decode_patch(dict_patch, obj, entity_class)

    @staticmethod
    def decode_patch(dict_patch, obj, entity_class):
        """Decode the received patch operation."""
        op = dict_patch['op']

        _assert(not hasattr(JsonPatch, op), "Operation %s invalid" % op)
        operation = getattr(JsonPatch, op)()
        operation.aply_patch(
            dict_patch['path'],
            obj,
            entity_class,
            dict_patch.get('value') or None
        )

    @staticmethod
    def add():
        """Return an instance of class operation Add."""
        return Add()

    @staticmethod
    def remove():
        """Return an instance of class operation Remove."""
        return Remove()

    @staticmethod
    def replace():
        """Return an instance of class operation Replace."""
        return Replace()

    @staticmethod
    def test():
        """Return an instance of class operation Test."""
        return Test()


class Operation(object):
    """Class of operations in patch."""

    def __init__(self, sub_class):
        """Constructor of class Operation. Receives sub class entity."""
        self.__subclass = sub_class

    def aply_patch(self, path, obj, entity_class, value=None):
        """Applie operation to received path."""
        path_list = path[1:].split('/')
        final_path = path_list.pop(-1)
        obj = Operation.go_through_path(self, obj, path_list)

        if final_path == "-":
            final_path = "-1"

        if final_path.lstrip("-+").isdigit():
            self.__subclass.operation_in_list(
                self,
                value,
                entity_class,
                obj,
                int(final_path),
            )
        else:
            self.__subclass.operation_in_atribute(
                self,
                value,
                entity_class,
                obj,
                final_path,
            )

    def go_through_path(self, obj, path_list):
        """Traverse the paths and returns the last accessed object."""
        if len(path_list) == 0:
            return obj

        atribute_path = path_list.pop(0)
        _assert(
            not hasattr(obj, atribute_path),
            "Atribute %s not found" % atribute_path
        )
        atribute = getattr(obj, atribute_path)

        return Operation.go_through_path(self, atribute, path_list)

    def operation_in_list(self, value, entity_class, atribute_list, index):
        """Execute operation in list."""
        raise PatchException("Operation not implemented")

    def operation_in_atribute(self, value, entity_class, obj, atribute):
        """Execute Operation in attribute."""
        raise PatchException("Operation not implemented")


class Add(Operation):
    """Class of operation add."""

    def __init__(self):
        """Constructor of class Add."""
        Operation.__init__(self, Add)

    @verify_entity
    def operation_in_list(self, value, entity_class, atribute_list, index):
        """Execute operation add in list."""
        atribute_list.insert(index, value)

    @verify_entity
    def operation_in_atribute(self, value, entity_class, obj, atribute):
        """Execute Operation add in list."""
        obj.__setattr__(atribute, value)


class Remove(Operation):
    """Class of operation remove."""

    def __init__(self):
        """Constructor of class Remove."""
        Operation.__init__(self, Remove)

    def operation_in_list(self, value, entity_class, atribute_list, index):
        """Execute operation remove in list."""
        atribute_list.pop(index)

    def operation_in_atribute(self, value, entity_class, obj, atribute):
        """Execute Operation remove in list."""
        _assert(not hasattr(obj, atribute), "Atribute %s not found" % atribute)
        obj.__delattr__(atribute)


class Replace(Operation):
    """Class of operation replace."""

    def __init__(self):
        """Constructor of class Replace."""
        Operation.__init__(self, Replace)

    @verify_entity
    def operation_in_list(self, value, entity_class, atribute_list, index):
        """Execute operation replace in list."""
        # TODO vetificar problema de remocao do ultimo indice
        atribute_list.insert(index, value)
        atribute_list.pop(index)

    @verify_entity
    def operation_in_atribute(self, value, entity_class, obj, atribute):
        """Execute Operation replace in list."""
        _assert(not hasattr(obj, atribute), "Atribute %s not found" % atribute)
        obj.__setattr__(atribute, value)


class Test(Operation):
    """Class of operation test."""

    def __init__(self):
        """Constructor of class Test."""
        Operation.__init__(self, Test)

    @verify_entity
    def operation_in_list(self, value, entity_class, atribute_list, index):
        """Execute operation test in list."""
        _assert(atribute_list[index] != value, "Test fail, object %s "
                "does not correspond to what was passed %s"
                % (atribute_list[index], value))

    @verify_entity
    def operation_in_atribute(self, value, entity_class, obj, atribute):
        """Execute Operation test in list."""
        _assert(getattr(obj, atribute) != value, "Test fail, object "
                "%s does not correspond to what was passed %s" % (getattr(obj, atribute), value))