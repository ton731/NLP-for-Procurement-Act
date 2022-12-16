#!/bin/bash
#SBATCH --job-name="gg"
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


python3 run_swag_no_trainer.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --train_file "./data/train_muti_id.json" \
  --validation_file "./data/val_muti_id.json" \
  --context_file "./data/context.json" \
  --output_dir "./wwm" \
  --num_train_epochs 20 \
  --with_tracking

  sbatch_post.sh

