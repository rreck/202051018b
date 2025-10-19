```json
{
  "id": "70b197f3ba221683",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288153,
  "host_pid": "9e6742732c60:1",
  "hash": "2c4164122d701740c59eb3f3774aca9d23f6d35d83bac8db02ee449a8c1c7fec",
  "cid": "QmV12c4164122d701740c59eb3f3774aca9d23f6d35d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288153,
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
      "evaluated_at": 1760288153
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
  "sig": "dd30ea2e4c6c8e4a3c06dfd5dcaa30a8a7cab1a5701094ffaa08c4278fa5ba74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034581430
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 34063092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285764, 'matching_hash': '1e0cfdc13a2b6c27'}}}