```json
{
  "id": "f34452c83d286b1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288331,
  "host_pid": "9e6742732c60:1",
  "hash": "7eec0a195759a4226b9928eaf1dbf49a22b8142a2726b444bbc4255f1bdb3b35",
  "cid": "QmV17eec0a195759a4226b9928eaf1dbf49a22b8142a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288331,
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
      "evaluated_at": 1760288331
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
  "sig": "27679c9caf492a0e7596330bcf03d9a21cfd077264dc5450fe8d93ce4ce6b4c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270910087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 36370980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285763, 'matching_hash': '020bc3c8298f3eb9'}}}