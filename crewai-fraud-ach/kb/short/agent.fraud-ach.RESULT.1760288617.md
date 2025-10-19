```json
{
  "id": "a7dc1312408f4152",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288617,
  "host_pid": "9e6742732c60:1",
  "hash": "736b33f595af0c20178e777069271640d9c56c9c51905ad87dea38013423b3eb",
  "cid": "QmV1736b33f595af0c20178e777069271640d9c56c9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288617,
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
      "evaluated_at": 1760288617
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
  "sig": "46321340f0cb32bb1ae1e114dcbacc6700d558e85aa2d0bc3f0538101a2f4256"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246372706
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 27779994, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': 'b5568fe52f6cf528'}}}