```json
{
  "id": "535dbc5bac76bd34",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290612,
  "host_pid": "9e6742732c60:1",
  "hash": "7a05b5d36e5222646695beb1a25e2e53167699d22f797b12ae9dd551a0bab231",
  "cid": "QmV17a05b5d36e5222646695beb1a25e2e53167699d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290612,
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
      "evaluated_at": 1760290612
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
  "sig": "7a0a13abfab8c92b1b0ed852956d57d26f9c16106b0901d5f7b2eb578a75b6ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271879965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 32875345, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}