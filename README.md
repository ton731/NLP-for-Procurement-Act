# 2022 ADL Final Project
Group 80, 江郁瑄、周遠同、馮意凡、黃琮煒、魏廷儒


### Environment
```shell
pip install -r requirements.txt
```


### MultipleChoice - Strategy 1: training without relevant laws
```shell
python train_multiple_choice.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext \
  --train_file "./data/train_multi_id.json" \
  --validation_file "./data/valid_multi_id.json" \
  --context_file "./data/context.json" \
  --output_dir "outputs/multiple_choice" \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 4 \
  --num_train_epochs 10 \
  --with_tracking \
```


### MultipleChoice - Strategy 2: training with relevant laws
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



### MultipleChoice - Strategy 4: summairzation formulation
```shell
python train_multiple_choice_summarization.py \
    --model_name_or_path google/mt5-small \
    --train_file ./data/mT5data/mT5traindata.jsonl \
    --validation_file ./data/mT5data/mT5validdata.jsonl \
    --text_column maintext \
    --summary_column title \
    --max_source_length 512 \
    --max_target_length 64 \
    --num_beams 3 \
    --num_train_epochs 10 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \

```
