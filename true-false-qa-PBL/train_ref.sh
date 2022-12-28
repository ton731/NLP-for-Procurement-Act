#!/bin/bash
#SBATCH --job-name="t2"
#SBATCH --partition=v100-32g
#SBATCH --gres=gpu:1
#SBATCH --ntasks=1
#SBATCH --time=24:59:59
#SBATCH --chdir=.
#SBATCH --output=precls_out.txt
#SBATCH --error=precls_err.txt
###SBATCH --test-only

sbatch_pre.sh
module load python/3.9.13-gpu



python3 trainQA.py \
    --train_data "./data/true-false-qa-TRAIN.json" \
    --test_data  "./data/true-false-qa-TEST.json" \
    --model_name_or_path hfl/chinese-roberta-wwm-ext \
    --num_epoch 200 \
    --batch_size 32 \
    --lr 1.0e-4 \
    --with_plotting \
    --use_law \
    --law_file "./data/law.json"

sbatch_post.sh
