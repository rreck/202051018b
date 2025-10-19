```json
{
  "id": "1170c758526dd322",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294124,
  "host_pid": "9e6742732c60:1",
  "hash": "8f7895cb86b8e44589599b013098f5abd12e47e294834e88308e80c2c4f2a74b",
  "cid": "QmV18f7895cb86b8e44589599b013098f5abd12e47e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294124,
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
      "evaluated_at": 1760294124
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
  "sig": "6aaf2870f2a320a53841eac5f822384d07c27b2eedb20a4e09d3f22be46d235a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026531578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 106492176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'f6751e9d8f5fd136'}}}