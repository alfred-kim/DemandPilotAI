# DemandPilot AI — EDA and Baseline Forecast Results

## 1. Dataset overview

- Dataset: M5 Walmart sales forecasting
- Product-store series: 30,490
- Unique products: 3,049
- Stores: 10
- Validation sales observations: d_1 through d_1913
- Evaluation sales observations: d_1 through d_1941
- Calendar range: 2011-01-29 to 2016-06-19

## 2. Evaluation design

- Sample size: 100 product-store series
- Reproducible sampling seed: 42
- Historical window: d_1907 through d_1913
- Forecast horizon: 28 days
- Forecast dates: 2016-04-25 to 2016-05-22
- Actual sales: matching 28 days from sales_train_evaluation.csv

## 3. Baseline comparison

| Method | MAE | WAPE | Forecast total |
|---|---:|---:|---:|
| Weekly seasonal-naive | 1.1614 | 83.04% | 4,252 |
| Seven-day mean-demand | 1.0227 | 73.12% | 4,252 |

Actual units sold: 3,916.

The seven-day mean-demand baseline reduced MAE and WAPE by
approximately 11.9% relative to the weekly seasonal-naive baseline.

## 4. Category-level seasonal-naive results

| Category | Series | Actual units | Forecast units | Mean series MAE | WAPE |
|---|---:|---:|---:|---:|---:|
| FOODS | 47 | 2,617 | 2,960 | 1.42 | 71.34% |
| HOBBIES | 25 | 572 | 640 | 0.99 | 120.98% |
| HOUSEHOLD | 28 | 727 | 652 | 0.88 | 95.32% |

HOBBIES had the highest WAPE in this sample. Category results are
descriptive and may vary with the selected products.

## 5. Interpretation and limitations

- The seven-day mean-demand method is the provisional benchmark.
- The experiment covers only 100 of 30,490 product-store series.
- The models use only the final seven historical days.
- Results do not establish performance across all products or seasons.
- Calendar events, prices, promotions, trends, and longer history have
  not yet been incorporated.
- Missing values were checked in inspected samples; full-dataset
  quality checks remain future work.

## 6. Next steps

1. Validate the baseline using additional historical windows.
2. Preserve time-based separation between training and evaluation.
3. Develop a stronger forecasting model and compare it with this benchmark.
4. Record model configuration, metrics, and experiment results.
