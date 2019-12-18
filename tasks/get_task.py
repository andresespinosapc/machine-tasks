from LongLookupTables import LongLookupTask
from LookupTables import LookupTask
from SymbolRewriting import SymbolTask
from SCAN import SCANTask
from tasks import Task


def get_task(name,
             is_small=False,
             is_mini=False,
             longer_repeat=5):
    """Return the wanted tasks.

    Args:
        name (str): name of the task to get
            Implemented Options: 
                "symbol_rewriting" : classical symbol rewriting task
                "lookup" : classical lookup table task
                "long_lookup" :  Lookup tables with training up to 3 compositions
                "long_lookup_oneshot" : long lookup tables with a iniital training 
                                        file without t7 and t8 and then adding
                                        uncomposed t7 and t8 with all the rest
                "long_lookup_reverse" : reverse long lookup table (i.e right to left hard attention)
                "noisy_long_lookup_multi" : noisy long lookup table where between each
                                            "real" table there's one noisy one.
                                            The hard attention is thus a diagonal wich is less steep
                "noisy_long_lookup_single" : noisy long lookup table with a special start token saying
                                            when are the "real tables" starting. The hard attention
                                            is thus a diagonal that starts at some random position.
                "long_lookup_intermediate_noise" : noisy long lookup table where there are multiple
                                                start token and only the last one really counts
                "scan_simple": Random split with 80% of train data and 20% of test data
                "scan_length": Train of shorter sequences and test of longer sequences
                "scan_addprim_turn_left": Training set includes all of the compositional tasks that
                                            do not include "turn_left", as well as just the primitive "turn_left"
                                            command in isolation
                "scan_addprim_jump": Training set includes all of the compositional tasks that
                                            do not include "jump", as well as just the primitive "jump"
                                            command in isolation
                NotImplemented Option:
                "long lookup jump" : Lookup tables with training 1 2 and 4 compositions (i.e jumping 3)
                                    currently does not have appropriate generation.txt
        is_small (bool, optional): whether to run a smaller verson of the task.
            Used for getting less statistically significant results.
        is_mini (bool, optional): whether to run a smaller verson of the task.
            Used for testing purposes.
        longer_repeat (int, optional): number of longer test sets.

    Returns:
        task (tasks.tasks.Task): instantiated task.
    """
    name = name.lower()

    # classical lookup table
    if name == "lookup":
        return LookupTask(is_small=is_small, is_mini=is_mini)

    # Long lookup tasks - paser in get_long_lookup_tables can figure out which
    elif "lookup" in name:
        return LongLookupTask(
            name, is_small=is_small, is_mini=is_mini,
            longer_repeat=longer_repeat)

    # classical symbol rewriting task
    elif name == "symbol_rewriting":
        return SymbolTask(is_small=is_small, is_mini=is_mini)

    # classical scan
    elif "scan" in name:
        sub_task = name.replace('scan_', '')
        return SCANTask(sub_task=sub_task)

    else:
        raise ValueError("Unkown name : {}".format(name))
