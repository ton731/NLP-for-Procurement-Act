# 2022 ADL Final Project

## Environment
```shell
pip install -r requirements.txt
```


## Training, multilpe choice, w/o laws (採購法)
```shell
python train_multiple_choice.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --train_file "./data/train_multi_id.json" \
  --validation_file "./data/valid_multi_id.json" \
  --context_file "./data/context.json" \
  --output_dir "outputs/multiple_choice" \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 4 \
  --num_train_epochs 5 \
  --with_tracking \
```


### Training, multiple choice, with laws (採購法)
```shell
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
```