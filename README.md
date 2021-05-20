# Cluwards - CLUCoin CLI Reward Tracker

Easily track a wallet's CLUCoin rewards.

If you'd like to donate, send some CLU here: 0x44f6498D1403321890F3f2917E00F22dBDE3577a

### Installation

**Requires Python 3.6+ Installed**

```
pip install cluwards
```

or 

```
git clone github.com/M4cs/cluwards
cd cluwards
python setup.py install
```

### Usage

```
cluwards ADDR
```

**Output in terminal:**
```
╭────────────────────────── CLUCoin Reward Summary: ───────────────────────────╮
│ Current Balance: 190,356,559.872826358                                       │
│ Total Rewards over last 3 minutes: 5,860.180806946                           │
│ Average Reward per Block over last 1 minute: 147.43492824695                 │
│ Average Reward per Block over last 3 minutes: 97.66968011576666666666666667  │
│ Total Rewards over last 3 minutes: 5,860.180806946                           │
│ Total Rewards Since Tracking Began: 5860.180806946                           │
╰──────────────────────────────────────────────────────────────────────────────╯
```

**This will update every 15 seconds.**