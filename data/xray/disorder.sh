#!/usr/bin/env bash
SRC_TRAIN_FILE="xray_diagnose_train.txt"
SRC_TEST_FILE="xray_diagnose_test.txt"
TMP1_FILE="tmp1.txt"
TMP2_FILE="tmp2.txt"
OUT_TRAIN_FILE="xray_diagnose_train_sort.txt"
OUT_TEST_FILE="xray_diagnose_test_sort.txt"

# sorting 3 times for train.txt
sort -R ${SRC_TRAIN_FILE} > ${TMP1_FILE}
sort -R ${TMP1_FILE} > ${TMP2_FILE}
sort -R ${TMP2_FILE} > ${TMP1_FILE}
cp ${TMP1_FILE} ${OUT_TRAIN_FILE}

# sorting 3 times for test.txt
sort -R ${SRC_TEST_FILE} > ${TMP1_FILE}
sort -R ${TMP1_FILE} > ${TMP2_FILE}
sort -R ${TMP2_FILE} > ${TMP1_FILE}
cp ${TMP1_FILE} ${OUT_TEST_FILE}


# remove temporary file
rm ${TMP1_FILE}
rm ${TMP2_FILE}
