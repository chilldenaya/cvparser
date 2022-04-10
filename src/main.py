from glob import glob
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

from collections import defaultdict

script_dir = os.path.dirname(__file__)
dataset_relative_path = "../dataset.json"
abs_file_path = os.path.join(script_dir, dataset_relative_path)


def pop_annot(raw_line):
    in_line = defaultdict(list, **raw_line)
    if "annotation" in in_line:
        labels = in_line["annotation"]
        for c_lab in labels:
            if len(c_lab["label"]) > 0:
                in_line[c_lab["label"][0]] += c_lab["points"]
    return in_line


with open(abs_file_path, "r") as f:
    # data is jsonl and so we parse it line-by-line
    resume_data = [json.loads(f_line) for f_line in f.readlines()]
    resume_df = pd.DataFrame([pop_annot(line) for line in resume_data])

resume_df["length"] = resume_df["content"].map(len)
resume_df["length"].hist()
print(resume_df.sample(3))
