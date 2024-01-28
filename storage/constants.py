# Failure mode negative rewards
STORE_FAILURE_REWARD = 0.0
CHALLENGE_FAILURE_REWARD = -0.01
MONITOR_FAILURE_REWARD = -0.01
RETRIEVAL_FAILURE_REWARD = -0.05

# Constants for storage limits in bytes
STORAGE_LIMIT_SUPER_SAIYAN = 1024**6 * 1  # 1 EB
STORAGE_LIMIT_DIAMOND = 1024**5 * 1  # 1 PB
STORAGE_LIMIT_GOLD = 1024**4 * 100  # 100 TB
STORAGE_LIMIT_SILVER = 1024**4 * 10  # 10 TB
STORAGE_LIMIT_BRONZE = 1024**4 * 1  # 1 TB

# Requirements for each tier. These must be maintained for a miner to remain in that tier.
SUPER_SAIYAN_STORE_SUCCESS_RATE = 0.999  # 1/1000 chance of failure
SUPER_SAIYAN_RETIREVAL_SUCCESS_RATE = 0.999  # 1/1000 chance of failure
SUPER_SAIYAN_CHALLENGE_SUCCESS_RATE = 0.999  # 1/1000 chance of failure

DIAMOND_STORE_SUCCESS_RATE = 0.99  # 1/100 chance of failure
DIAMOND_RETRIEVAL_SUCCESS_RATE = 0.99  # 1/100 chance of failure
DIAMOND_CHALLENGE_SUCCESS_RATE = 0.99  # 1/100 chance of failure

GOLD_STORE_SUCCESS_RATE = 0.975  # 1/50 chance of failure
GOLD_RETRIEVAL_SUCCESS_RATE = 0.975  # 1/50 chance of failure
GOLD_CHALLENGE_SUCCESS_RATE = 0.975  # 1/50 chance of failure

SILVER_STORE_SUCCESS_RATE = 0.95  # 1/20 chance of failure
SILVER_RETRIEVAL_SUCCESS_RATE = 0.90  # 1/20 chance of failure
SILVER_CHALLENGE_SUCCESS_RATE = 0.95  # 1/20 chance of failure

SUPER_SAIYAN_TIER_REWARD_FACTOR = 1.0  # Get 100% rewards
DIAMOND_TIER_REWARD_FACTOR = 0.888  # Get 88.8% rewards
GOLD_TIER_REWARD_FACTOR = 0.777  # Get 77.7% rewards
SILVER_TIER_REWARD_FACTOR = 0.555  # Get 55.5% rewards
BRONZE_TIER_REWARD_FACTOR = 0.444  # Get 44.4% rewards

SUPER_SAIYAN_TIER_TOTAL_SUCCESSES = 10**5  # 100,000
DIAMOND_TIER_TOTAL_SUCCESSES = 10**4 * 5  # 50,000
GOLD_TIER_TOTAL_SUCCESSES = 10**3 * 5  # 5,000
SILVER_TIER_TOTAL_SUCCESSES = 10**3  # 1,000

SUPER_SAIYAN_SUCCESS_RATE = 0.99  # 1/100 chance of failure
DIAMOND_SUCCESS_RATE = 0.975  # 1/50 chance of failure
GOLD_SUCCESS_RATE = 0.95  # 1/20 chance of failure
SILVER_SUCCESS_RATE = 0.90  # 1/10 chance of failure
