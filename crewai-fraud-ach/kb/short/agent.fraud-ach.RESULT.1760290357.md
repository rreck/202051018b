```json
{
  "id": "3598327bde498700",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290357,
  "host_pid": "9e6742732c60:1",
  "hash": "918f20264af00a8e010b4a6deb845443504772b13bc1cb4df0c1f7c1e0f195a2",
  "cid": "QmV1918f20264af00a8e010b4a6deb845443504772b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290357,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760290357
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "ac5125ec2800419d2de0bf839d9416c4b7feefdae9aa4e936e1d9af36237fd83"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 21817272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}