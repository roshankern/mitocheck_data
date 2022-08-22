# 2. Format Training Data

In this module, we associate features extracted from labeled frames with their Mitocheck-assigned phenotypic class label.
After extracting the features from these labeled frames with `idrstream`, we associate the bounding boxes of cells from [features/](../mitocheck_metadata/features) with their `idrstream`-derived coordinates to assign cells their phenotypic class (as assigned by Mitocheck).

**Note:** `Shape1` and `Shape3` are replaced with binuclear and polylobed respectively, as these their correspoonding classes.
See [#16](https://github.com/WayScience/mitocheck_data/issues/16) for more details.

## Step 1: Format Training Data

Use the commands below to format the training data:

```sh
# Make sure you are located in 0.locate_data
cd 2.format_training_data

# Activate mitocheck_data conda environment
conda activate mitocheck_data

# Format data
bash format_training_data.sh
```