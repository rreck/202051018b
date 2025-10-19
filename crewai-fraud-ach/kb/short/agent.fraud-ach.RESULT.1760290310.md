```json
{
  "id": "88ea01cb241a763b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290310,
  "host_pid": "9e6742732c60:1",
  "hash": "0f2e9a77b955ea5ddc4dea550070b976c7f0c5a3132773880bee7eba95868f8e",
  "cid": "QmV10f2e9a77b955ea5ddc4dea550070b976c7f0c5a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290310,
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
      "evaluated_at": 1760290310
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
  "sig": "68ea11a999a5cbc18effb8834aaf691d8139e5d700e0d0fe213ba1c7cb930903"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153135421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 56100492, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '4394c86a949e27d6'}}}maly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.68, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8942822}}}