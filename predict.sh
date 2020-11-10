rm res
test_file=$1
ALLENNLP_PATH=/Users/ruolinsu/anaconda3/envs/dstqa/bin/allennlp
for i in 0 4; do #500 497 494 491 488
python ${ALLENNLP_PATH} predict --cuda-device -1 --predictor dstqa --include-package dstqa --weights-file model/model_state_epoch_${i}.th model/model.tar.gz ${test_file} > ${i}
python formulate_pred_belief_state.py ${i} >> res
done
