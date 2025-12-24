// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TrustAirdrop {
    enum RiskBucket { LOW, MEDIUM, HIGH }

    struct TrustRecord {
        RiskBucket bucket;
        bytes32 analysisHash;
        uint256 timestamp;
        bool exists;
    }

    mapping(address => TrustRecord) public trust;

    event RiskCommitted(
        address indexed user,
        RiskBucket bucket,
        bytes32 analysisHash,
        uint256 timestamp
    );

    function commitRisk(
        address user,
        uint8 bucket,
        bytes32 analysisHash
    ) external {
        require(bucket <= uint8(RiskBucket.HIGH), "Invalid bucket");

        trust[user] = TrustRecord({
            bucket: RiskBucket(bucket),
            analysisHash: analysisHash,
            timestamp: block.timestamp,
            exists: true
        });

        emit RiskCommitted(
            user,
            RiskBucket(bucket),
            analysisHash,
            block.timestamp
        );
    }

    function calculateReward(address user) external view returns (uint256) {
        require(trust[user].exists, "No trust record");

        if (trust[user].bucket == RiskBucket.LOW) return 100;
        if (trust[user].bucket == RiskBucket.MEDIUM) return 60;
        return 20; // HIGH risk
    }
}
