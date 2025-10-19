```json
{
  "id": "25ed683c26240af9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288913,
  "host_pid": "9e6742732c60:1",
  "hash": "9bd2ecbb8f9d6e4633632e908e0886e2c95db7d1c01a66d6f0a89ba004e69060",
  "cid": "QmV19bd2ecbb8f9d6e4633632e908e0886e2c95db7d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288913,
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
      "evaluated_at": 1760288913
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
  "sig": "d2b747ffc292b3bcb94ffcf0de88fc75492a7b26c3c15a20c66a5189cd68a832"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593273938
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 39343320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': '9925ef3004078e34'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}