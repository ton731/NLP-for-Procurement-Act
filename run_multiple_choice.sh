python train_multiple_choice.py \
  -- model_name_or_path hfl/chinese-roberta-wwm-ext \
  --train_file "./data/train_multi_id.json" \
  --validation_file "./data/valid_multi_id.json" \
  --context_file "./data/context.json" \
  --law_file "./data/law.json" \
  --per_device_train_batch_size 1 \
  --per_device_eval_batch_size 1 \
  --num_train_epochs 100 \
  --use_law \


