# magical-thinking

This "magical thinking" repository is meant to show how a data science project can be set up to be reproducible, scalable, and easy for data scientists to use without having to reinvent the wheel and make the same decisions over and over again.

Instead of using real data science code and performing actual modeling activity, we can use "magical thinking" to write functions that make sense from a design perspective and worry about the implementation and testing later. The idea is to be able to really focus on the workflow ergonomics to design a better system rather than focusing on a specific application. 

Magical thinking asks the question "wouldn't it be nice if this function did X?" and then we can write a function and pretend it does X instead of spending our time on making it do X. This allows us to move on to the next function and come up with a completely designed system to evaluate and later flesh out the actual code.

## Defining and installing the environment

```bash
mamba env update --file env.yaml --prune
```

## Prefect

Prefect is a tool for task orchestration that allows for retries after failures in the DAG.

To run the flow, first define the flow in prefect_flow.py, then run the following command:

```python
python prefect_flow.py
```

To run the Prefect UI to inspect flows and flow runs, run the following command:

```bash
prefect server start
```

After the server is running, navigate to this URI in your browser to view the UI:

- http://127.0.0.1:4200

## Adapting Prefect workflow to MLflow Recipes

```mermaid
flowchart TD

    in[ingest]
    cl[clean]
    ft[featurize]
    sp[split]
    tf[transform]
    tr[train]
    pr[predict]
    ev[evaluate]
    rg[register]

    id{{ingested_data}}
    cld{{cleaned_data}}
    fd{{featurized_data}}
    trd{{train_data}}
    ted{{test_data}}
    vald{{validation_data}}
    tfd{{transformed_data}}
    prd{{predictions}}

    m[(model)]
    mlfm[(mlflow model registry)]

    in --> id
    id --> cl
    cl --> cld
    cld --> ft
    ft --> fd
    fd --> sp

    sp --> trd
    sp --> ted
    sp --> vald

    trd --> tf --> tfd
    tfd --> tr --> m --> rg
    rg --> mlfm
    
    m --> pr --> prd

    prd --> ev
    ted --> ev
    vald --> ev

```

## Workflow

```mermaid
graph TD
    subgraph Data Preparation
    DI[Data Ingestion] --> DM[Data Modeling]
    DM --> DC[Data Cleaning]
    end

    subgraph feature engineering
    DC --> FC[Feature Crossing]
    DC --> P[Polynomials]
    DC --> DFS[Deep Feature Synthesis]
    DC --> TF[Log Transformation]
    DC --> EN[Feature Encoding]
    DC --> BIN[Feature Binning]
    DC --> AGG[Window Aggregation]
    
    FC --> MI[Model Input]
    P --> MI
    DFS --> MI
    TF --> MI
    EN --> MI
    BIN --> MI
    AGG --> MI
    end

    subgraph Data Splitting
    MI --> TTS[Train Test Split]
    TTS --> TR[Train]
    TTS --> TE[Test]
    TTS --> VAL[Validation]
    end

    subgraph Data Transformation
    TR --> MDI[Missing Data Imputation]
    TR --> FS[Feature Scaling]
    MDI --> TD[Transformed Data]
    FS --> TD
    end
    
    subgraph Model Training
    TD --> E1[Experiment 1]
    E1 --> H1[Hyperparameter Tuning 1]
    TE --> H1
    H1 --> M1[Model 1]

    TD --> E2[Experiment 2]
    E2 --> H2[Hyperparameter Tuning 2]
    TE --> H2
    H2 --> M2[Model 2]
    end

    subgraph Model Evaluation
    M1 --> P1[Model 1 Performance]
    M2 --> P2[Model 2 Performance]
    VAL --> P1
    VAL --> P2
    end

    subgraph Model Selection
    P1 --> BM[Best Model]
    P2 --> BM
    end

    subgraph Model Inference
    BM --> PREDS[Predictions]
    end
```

## SKLearn Pipeline

![Pipeline](https://i.stack.imgur.com/uR1Wt.png)

## MLflow Recipes Classification Template

MLflow has something called [Recipes](https://mlflow.org/docs/latest/recipes.html) that provides a template for a DAG that can be used to train and evaluate a model. These steps happen in a sequence that helps to ensure there is no target leakage and assists with refactoring the data preparation and model training steps into a robust workflow.

The template is shown below:

![MLflow Recipes Classification Template](https://mlflow.org/docs/latest/_images/recipes_databricks_dag.png)
