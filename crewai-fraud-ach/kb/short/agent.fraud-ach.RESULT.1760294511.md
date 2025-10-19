```json
{
  "id": "9231372b8da754b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294511,
  "host_pid": "9e6742732c60:1",
  "hash": "6a37906de6b6823734c5796641acf44aae03447c6418cf633ee3198b11719508",
  "cid": "QmV16a37906de6b6823734c5796641acf44aae03447c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294511,
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
      "evaluated_at": 1760294511
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
  "sig": "b0938280b20aca5470a78a38f3e06270bda3ee84bbab2a71532d808d13a51ff5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278681806
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 112396920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': '5ddc61c49d89e409'}}}