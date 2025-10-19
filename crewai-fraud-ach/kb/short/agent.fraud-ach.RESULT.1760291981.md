```json
{
  "id": "aca17aabec9b1ad7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291981,
  "host_pid": "9e6742732c60:1",
  "hash": "c96d7238ccb297cd00ad7e37a0786198193690e4c6ef07ccb8e988902c74af71",
  "cid": "QmV1c96d7238ccb297cd00ad7e37a0786198193690e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291981,
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
      "evaluated_at": 1760291981
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
  "sig": "7788f81a0d953f5d6bea27bef1a9dfd270bbcef5db8aaf239ca1e49937bd0f59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 48667124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}