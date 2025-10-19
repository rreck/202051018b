```json
{
  "id": "f826bf9976a8aab6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288858,
  "host_pid": "9e6742732c60:1",
  "hash": "19b1a6fa960195f18d49b7d2fc7a3284ffde8858775b9cf81f500943ac899394",
  "cid": "QmV119b1a6fa960195f18d49b7d2fc7a3284ffde8858",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288858,
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
      "evaluated_at": 1760288858
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
  "sig": "8157d0d5206ff5e2fbd181a17539fda5a1fcc5844b98650dc37417ffc79b9361"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030798175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 21674744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760284979, 'matching_hash': 'fdbb68f6e232305a'}}}