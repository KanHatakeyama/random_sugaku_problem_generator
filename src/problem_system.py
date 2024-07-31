from .chuichi_seifu import *
from .chuichi_futogo import generate_problem_and_answer_futogo
from .chuichi_futogo_multi import *

problem_generator_dict = {
    "seifu": generate_seifu_problem,
    "seisu_seki": generate_product_problem_and_answer_seki,
    "table_mean": generate_mean_problem_and_answer,
    "futogo": generate_problem_and_answer_futogo,
    "futogo_multi": generate_inequality_problem_and_answer,
    "futogo_suretsu": generate_sort_problem_and_answer,
    "futogo_suretsu2": generate_sort_problem_and_answer2,
    "n_th_largest": generate_nth_largest_problem_and_answer,
    "n_th_smallest": generate_nth_smallest_problem_and_answer,
    "max_suretsu": generate_largest_number_problem_and_answer,
    "min_suretsu": generate_smallest_number_problem_and_answer,
    "seisu_range": generate_range_problem_and_answer,
    "seisu_range_futoshiki": generate_inequality_problem_and_answer_futoshiki,

}
