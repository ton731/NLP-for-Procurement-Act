#!/bin/bash
#SBATCH --job-name="??"
#SBATCH --partition=v100-32g
#SBATCH --ntasks=2
#SBATCH --gres=gpu:1
#SBATCH --time=10-0:0
#SBATCH --output=cout_multi.txt
#SBATCH --error=cerr_multi.txt
#SBATCH --chdir=.
###SBATCH --test-only

sbatch_pre.sh

python train_multiple_choice.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --train_file "./data/train_multi_id.json" \
  --validation_file "./data/valid_multi_id.json" \
  --context_file "./data/context.json" \
  --output_dir "outputs/multiple_choice" \
  --law_file "./data/law.json" \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 4 \
  --num_train_epochs 5 \
  --use_law \
  --with_tracking \

sbatch_post.sh
