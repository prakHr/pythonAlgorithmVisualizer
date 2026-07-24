import os
os.environ["OMP_NUM_THREADS"] = "1"
import multiprocessing 
from mpire import WorkerPool
from pprint import pprint
num_cores = max(multiprocessing.cpu_count()//2,1)
from pprint import pprint
from multiprocessing import Manager
import importlib
import io
import contextlib
import importlib
import io
import contextlib

import os
os.environ["OMP_NUM_THREADS"] = "1"

import multiprocessing
from mpire import WorkerPool
from pprint import pprint
import importlib
import io
import contextlib

num_cores = max(multiprocessing.cpu_count() // 2, 1)


def create_visualization(
    algorithm_name,
    constructor_args,
    operations,
    algorithm_to_save,
    fps,
    save_type="gif",
):
    """
    Generic visualization creator.

    constructor_args : list
        Arguments passed to the constructor.

    operations : list of dict
        Example:
        [
            {"method":"insert","args":[50]},
            {"method":"search","args":[40]},
            {"method":"delete","args":[20]}
        ]
    """

    class_name = "".join(word.title() for word in algorithm_name.split("_"))
    if class_name=="Bst":
        class_name="BST"

    module = importlib.import_module(f"vizods.{algorithm_name}")
    cls = getattr(module, class_name)

    # Instantiate object
    obj = cls(*constructor_args)

    # Execute all requested operations
    for operation in operations:
        method = getattr(obj, operation["method"])
        method(
            *operation.get("args", []),
            **operation.get("kwargs", {})
        )

    # Silence save_gif/save_video prints
    with contextlib.redirect_stdout(io.StringIO()):
        if save_type.lower() == "gif":
            obj.save_gif(algorithm_to_save, fps=fps)
        else:
            obj.save_video(algorithm_to_save, fps=fps)

    return f"{algorithm_name} : Success"

def create_multiple_visualizations(algorithms_name,constructor_argss,algorithms_operations,algorithms_to_save,fpss):
    # for ll in (algorithms_name,constructor_argss,algorithms_operations,algorithms_to_save,fpss):
    #         print(len(ll))
    
    results = [
        {
            "algorithm_name":algorithm_name,
            "constructor_args":constructor_args,
            "operations":algorithm_operation,
            "algorithm_to_save":algorithm_to_save,
            "fps":fps
        } for algorithm_name,constructor_args,algorithm_operation,algorithm_to_save,fps in zip(
            algorithms_name,constructor_argss,algorithms_operations,algorithms_to_save,fpss
        )
    ]
    # pprint(results)
    with WorkerPool(n_jobs=1,daemon=False) as pool:
        results = pool.map(create_visualization, results, progress_bar=True)
    return results

if __name__=="__main__":
    algorithms_name = []
    constructor_argss = []
    algorithms_operations = []
    algorithms_to_save = []
    fpss = []

    ####################################################
    # Bubble Sort
    ####################################################
    algorithm_name = "bubble_sort"
    constructor_args = [[64, 34, 25, 12, 22, 11, 90]]
    operations = [{"method": "sort"}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\bubble_sort.gif"
    fps = 8

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Selection Sort
    ####################################################
    algorithm_name = "selection_sort"
    constructor_args = [[64, 25, 12, 22, 11]]
    operations = [{"method": "sort"}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\selection_sort.gif"
    fps = 8

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Insertion Sort
    ####################################################
    algorithm_name = "insertion_sort"
    constructor_args = [[12, 11, 13, 5, 6]]
    operations = [{"method": "sort"}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\insertion_sort.gif"
    fps = 8

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Merge Sort
    ####################################################
    algorithm_name = "merge_sort"
    constructor_args = [[38, 27, 43, 3, 9, 82, 10]]
    operations = [{"method": "sort"}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\merge_sort.gif"
    fps = 8

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Quick Sort
    ####################################################
    algorithm_name = "quick_sort"
    constructor_args = [[10, 7, 8, 9, 1, 5]]
    operations = [{"method": "sort"}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\quick_sort.gif"
    fps = 8

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    
    ####################################################
    # Linear Search
    ####################################################
    algorithm_name = "linear_search"
    constructor_args = [[10, 50, 30, 70, 80, 60, 20, 90, 40]]
    operations = [{"method": "search", "args": [70]}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\linear_search.gif"
    fps = 10

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Binary Search
    ####################################################
    algorithm_name = "binary_search"
    constructor_args = [[10, 20, 30, 40, 50, 60, 70, 80]]
    operations = [{"method": "search", "args": [60]}]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\binary_search.gif"
    fps = 10

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Linked List
    ####################################################
    algorithm_name = "linked_list"
    constructor_args = []
    operations = [
        {"method": "add_node", "args": [10]},
        {"method": "add_node", "args": [20]},
        {"method": "add_node", "args": [30]},
        {"method": "add_node", "args": [40]},
        {"method": "add_node", "args": [50]},
        {"method": "delete_node", "args": [30]},
    ]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\linked_list.gif"
    fps = 2

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Stack
    ####################################################
    algorithm_name = "stack"
    constructor_args = []
    operations = [
        {"method": "push", "args": [10]},
        {"method": "push", "args": [20]},
        {"method": "push", "args": [30]},
        {"method": "pop"},
    ]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\stack.gif"
    fps = 2

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Queue
    ####################################################
    algorithm_name = "queue"
    constructor_args = []
    operations = [
        {"method": "enqueue", "args": [10]},
        {"method": "enqueue", "args": [20]},
        {"method": "enqueue", "args": [30]},
        {"method": "dequeue"},
    ]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\queue.gif"
    fps = 2

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Binary Search Tree
    ####################################################
    algorithm_name = "bst"
    constructor_args = []
    operations = [
        {"method": "insert", "args": [50]},
        {"method": "insert", "args": [30]},
        {"method": "insert", "args": [70]},
        {"method": "insert", "args": [20]},
        {"method": "insert", "args": [40]},
        {"method": "insert", "args": [60]},
        {"method": "insert", "args": [80]},
        {"method": "search", "args": [40]},
        {"method": "delete", "args": [20]},
    ]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\bst.gif"
    fps = 2

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################
    # Dijkstra
    ####################################################
    algorithm_name = "dijkstra"
    constructor_args = []
    operations = [
        {"method": "add_edge", "args": ["A", "B", 4]},
        {"method": "add_edge", "args": ["A", "C", 2]},
        {"method": "add_edge", "args": ["B", "C", 1]},
        {"method": "add_edge", "args": ["B", "D", 5]},
        {"method": "add_edge", "args": ["C", "D", 8]},
        {"method": "add_edge", "args": ["D", "E", 2]},
        {
            "method": "visualize_search",
            "kwargs": {
                "start_node": "A",
                "target_node": "E",
            },
        },
    ]
    algorithm_to_save = r"C:\Users\prakhar.a.gandhi\Downloads\pythonApps\dijkstra.gif"
    fps = 2

    algorithms_name.append(algorithm_name)
    constructor_argss.append(constructor_args)
    algorithms_operations.append(operations)
    algorithms_to_save.append(algorithm_to_save)
    fpss.append(fps)

    ####################################################

    results = create_multiple_visualizations(
        algorithms_name,
        constructor_argss,
        algorithms_operations,
        algorithms_to_save,
        fpss,
    )