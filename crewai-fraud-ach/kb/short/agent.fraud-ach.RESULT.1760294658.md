```json
{
  "id": "6b014f72fc35e4e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294658,
  "host_pid": "9e6742732c60:1",
  "hash": "5f7cd3650e5b80953ad141be6520cbe6076719ece14950a6aab5e3f3c68f0b81",
  "cid": "QmV15f7cd3650e5b80953ad141be6520cbe6076719ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294658,
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
      "evaluated_at": 1760294658
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
  "sig": "b27328a136b7eefde71499cafe7a3e0a16ef216b1b480861e114314598093203"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022233458
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 68438568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '02c54d650b9e4b50'}}}}aly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6178432}}}