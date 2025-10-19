```json
{
  "id": "98790920d3c8f6a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290439,
  "host_pid": "9e6742732c60:1",
  "hash": "96ef933a662e3c45b12e558633918bdc428f3c627e1f01c049a0ccc921cf2959",
  "cid": "QmV196ef933a662e3c45b12e558633918bdc428f3c62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290439,
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
      "evaluated_at": 1760290439
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
  "sig": "d14b40b29ecfe6c1cbb99ec181f277e45442ae5fdde7168e8e3018288bb3afc0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597956116
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 55090500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285764, 'matching_hash': '37dac3adff3764b9'}}}