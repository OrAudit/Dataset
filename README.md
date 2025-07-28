# Dataset
Evaluation Dataset of [OrAudit](https://github.com/OrAudit/OrAudit)

## Introduction

### Script Description:
- **get_address.py** analyzes a specified HTML file to batch retrieve contract addresses, contract names, release dates, and transaction counts, then saves the data to a CSV file.

- **dedup.py** removes duplicates based on contract addresses from the specified CSV file and generates a new CSV file.

- **analyze.py** invokes three Oracle Contract Consumer Vulnerability (OCCV) detectors to analyze the source code of contract addresses in the specified CSV file.

### Analyzed Data Description:
- **OracleAttacks.xlsx** contains the analysis of oracle-related attacks from 2019 to the present. These attacks are recorded by [SlowMist](https://hacked.slowmist.io/). By analyzing the attack vetors and root causes of these attacks, we can gain a more systematic understanding of the security risks currently faced by oracle ecosystem.

- **EvaluationResults.xlsx** presents the vulnerability detection results of OrAudit on the collected oracle consumer contracts. To assess the precision and recall of OrAudit, we manually analyzed 20 contracts from each category of oracle services (or all available contracts if fewer than 20).

### Source Data Description:
The four folders — chainlink, pyth, chronicle, and redstone — contain the collected contract data and vulnerability detection results for each category of oracle services. The oracle services supported by OrAudit are as follows:

Index | Provider | Service | Dependency
--- | --- | --- | ---
1|Chainlink|[Data Feed](https://docs.chain.link/data-feeds)| AggregatorV3Interface, AccessControlledOffchainAggregator
2|Chainlink|[Data Stream](https://docs.chain.link/data-streams)|StreamsLookupCompatibleInterface
3|Chainlink|[Any API](https://docs.chain.link/any-api/introduction)|ChainlinkClient
4|Chainlink|[Functions](https://docs.chain.link/chainlink-functions)|FunctionsClient
5|Chainlink|[VRF](https://docs.chain.link/vrf)|VRFConsumerBaseV2, VRFV2WrapperConsumerBase, VRFConsumerBaseV2Plus, VRFV2PlusWrapperConsumerBase
6|Pyth|[Data Feed](https://docs.pyth.network/price-feeds)|IPyth
7|Pyth|[Data Stream](https://docs.pyth.network/lazer)|PythLazer
8|Pyth|[VRF](https://docs.pyth.network/entropy)|IEntropyConsumer
9|Chronicle|[Data Feed](https://docs.chroniclelabs.org/Developers/start)|IChronicle
10|Redstone|[Data Feed](https://docs.redstone.finance/docs/dapps/redstone-pull/)|RedstoneConsumerBase

In each folder, the HTML files include data retrieved from Etherscan (as of June 28) using dependency as keywords. The contracts.csv files contain extracted contract information such as addresses and transaction volumes. The output files include the vulnerability detection results for all contracts collected in each respective category.

## Experiment Replication

First, please follow the instructions in the [README](https://github.com/OrAudit/OrAudit) to install OrAudit and set up the necessary dependencies.

Next, run the following command to perform OCCV detection on the specified set of contracts (In analyze.py, replace the file path in line 9 with the path to your target CSV file, and substitute "YOUR_API_KEY" in line 21 with a [valid apikey](https://etherscan.io/apidashboard) before running the script.):

```
python3 analyze.py
```
The detection results will be saved in the output file in the current directory.
