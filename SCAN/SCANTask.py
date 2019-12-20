from tasks import Task
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

possible_sub_tasks = {
    'simple': 'simple_split',
    'length': 'length_split',
    'addprim_turn_left': 'add_prim_split',
    'addprim_jump': 'add_prim_split',
}

class SCANTask(Task):

    def __init__(self, sub_task):
        if sub_task not in possible_sub_tasks:
            raise NotImplementedError('Sub task %s is not implemented' % (sub_task))

        data_dir = os.path.join(dir_path, possible_sub_tasks[sub_task])

        split_files = filter(lambda x: sub_task in x, os.listdir(data_dir))
        split_files = list(map(lambda x: x.split('.')[0], split_files))
        train_file = next(filter(lambda x: 'train' in x, split_files), None)
        valid_file = next(filter(lambda x: 'validation' in x, split_files), None)
        test_files = list(filter(lambda x: 'test' in x, split_files))

        super().__init__(
            'SCAN_%s' % (sub_task),
            data_dir,
            train_file,
            valid_file,
            test_files,
            default_params=None,
            extension='txt'
        )
