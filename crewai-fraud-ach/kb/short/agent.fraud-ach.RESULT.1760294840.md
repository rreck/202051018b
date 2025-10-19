```json
{
  "id": "fd936cfe3f57bf47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294840,
  "host_pid": "9e6742732c60:1",
  "hash": "a62eab74cdaabcd9009cfe7bd008f981208d67f6d7b38093169c493376a490d8",
  "cid": "QmV1a62eab74cdaabcd9009cfe7bd008f981208d67f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294840,
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
      "evaluated_at": 1760294840
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
  "sig": "4549a92256896b1546b2fad32c5b68c9a9c99638ecbbe0c0ad30cddc451b20de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034581430
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 99350685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '1e0cfdc13a2b6c27'}}}