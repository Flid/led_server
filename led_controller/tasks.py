from __future__ import unicode_literals, absolute_import

from multiprocessing.queues import Queue, Empty


_tasks_schedule = Queue()


def add_task(task):
    """
    Add a new task to the queue.
    :param task: a dict like {'name': <task_name>, ...}
    """
    task_class = TASK_BY_NAME[task['name']]

    task_class.validate_task_dict(task)

    _tasks_schedule.put(task)


def pop_task():
    try:
        return _tasks_schedule.get(timeout=1)
    except Empty:
        return None

TASK_BY_NAME = {}


def process_task(matrix, task_dict):
    task_class = TASK_BY_NAME[task_dict['name']]
    task_class.process(matrix, task_dict)


class TaskCollectionMeta(type):
    def __new__(cls, name, parents, dct):

        task_name = dct.get('NAME')
        assert task_name or name == 'TaskBase'

        result = super(TaskCollectionMeta, cls).__new__(cls, name, parents, dct)

        if name != 'TaskBase':
            TASK_BY_NAME[dct['NAME']] = result

        return result


class TaskBase(object):
    __metaclass__ = TaskCollectionMeta
    NAME = None
    REQUIRED_PARAMS = set()

    @classmethod
    def validate_task_dict(cls, task_dict):
        assert 'name' in task_dict
        assert task_dict['name'] in TASK_BY_NAME

        for key in cls.REQUIRED_PARAMS:
            assert key in task_dict

    @classmethod
    def process(cls, matrix, params):
        raise NotImplementedError()


class SetPixelTask(TaskBase):
    NAME = 'set_pixel'
    REQUIRED_PARAMS = {
        'coords',
        'color',
    }

    @classmethod
    def process(cls, matrix, params):
        matrix.SetPixel(
            params['coords'][0],
            params['coords'][1],
            params['color'][0],
            params['color'][1],
            params['color'][2],
        )
