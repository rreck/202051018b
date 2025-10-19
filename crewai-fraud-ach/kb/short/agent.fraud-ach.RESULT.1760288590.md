```json
{
  "id": "b6dcef59b15adfb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288590,
  "host_pid": "9e6742732c60:1",
  "hash": "53e0ed706b7791bc5114433b25288106fec53e217ed65fb6fae673a0ebffce3f",
  "cid": "QmV153e0ed706b7791bc5114433b25288106fec53e21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288590,
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
      "evaluated_at": 1760288590
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
  "sig": "18f52417febdbcd7da44fde46b1eef0a029f8772067485acb142bbca2a0219b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276534342
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 30591778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '3bb091557ce86ea6'}}}aly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.51, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6888614}}}