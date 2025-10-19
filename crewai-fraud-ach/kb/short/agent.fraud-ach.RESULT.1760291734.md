```json
{
  "id": "f2cacd097836a5f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291734,
  "host_pid": "9e6742732c60:1",
  "hash": "0b39b3699479726e0ab05b56e2db36ffc3fde029c556390283e7c0185e0ef017",
  "cid": "QmV10b39b3699479726e0ab05b56e2db36ffc3fde029",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291734,
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
      "evaluated_at": 1760291734
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
  "sig": "ed78bb9d7d6cc064213d2d8e685764acf9fdcb065b813bd839201df614a76548"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271295485
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 69415892, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '1c5bb12c0a4cbea7'}}}