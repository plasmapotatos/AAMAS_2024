#!/bin/bash
set -e
export OUTPUT_DIR=./
export EXAMPLE_FOLDER="/Users/wei/TravelPlanner_forward/evaluation/examples"
# export EXAMPLE_PLAN_NUMBER=1
# export TRIAL_NUMBER=2
# We support MODEL in ['gpt-3.5-turbo-X','gpt-4-1106-preview','gemini','mistral-7B-32K','mixtral']
export MODEL_NAME=gpt-4o-mini
#export OPENAI_API_KEY=YOUR_OPENAI_KEY already set in conda
# if you do not want to test google models, like gemini, just input "1".
export GOOGLE_API_KEY=1
# SET_TYPE in ['validation', 'test', 'train']
export SET_TYPE=validation
# STRATEGY in ['direct','cot','react','reflexion']
export STRATEGY=direct

python tools/planner/sole_planning.py  --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --example_folder $EXAMPLE_FOLDER --example_plan_number $EXAMPLE_PLAN_NUMBER

export OUTPUT_DIR=../evaluation
export TMP_DIR=.
export EVALUATION_DIR=../evaluation
export MODE=sole-planning
export SUBMISSION_FILE_DIR=./
export STRATEGY=direct

cd postprocess
python parsing.py  --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --tmp_dir $TMP_DIR --mode $MODE

python element_extraction.py  --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --tmp_dir $TMP_DIR --mode $MODE

python combination.py --set_type $SET_TYPE --output_dir $OUTPUT_DIR --model_name $MODEL_NAME --strategy $STRATEGY --submission_file_dir $SUBMISSION_FILE_DIR --mode $MODE

export EVALUATION_FILE_PATH=../postprocess/${SET_TYPE}_${MODEL_NAME}_direct_sole-planning_submission.jsonl

cd ../evaluation
python eval.py --set_type $SET_TYPE --evaluation_file_path $EVALUATION_FILE_PATH

#reorganize
cd ..
export OUTPUT_DIR=evaluation/examples_trials/example_${EXAMPLE_PLAN_NUMBER}/trial_${TRIAL_NUMBER}
mkdir -p $OUTPUT_DIR
mv evaluation/data_record.json evaluation/evaluated_scores.json evaluation/final_result.json $OUTPUT_DIR
mv postprocess/${SET_TYPE}_${MODEL_NAME}_direct_sole-planning_submission.jsonl postprocess/${SET_TYPE}_${MODEL_NAME}_direct_sole-planning.txt $OUTPUT_DIR
mv evaluation/${MODEL_NAME}_${SET_TYPE} $OUTPUT_DIR

