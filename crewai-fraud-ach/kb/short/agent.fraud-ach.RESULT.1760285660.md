```json
{
  "id": "afe59a3b5e243cfa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285660,
  "host_pid": "9e6742732c60:1",
  "hash": "6b0426a11d880a6ea3bd9295f119dc21a834d571b1f04c4e1c8a908d7c282591",
  "cid": "QmV16b0426a11d880a6ea3bd9295f119dc21a834d571",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285660,
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
      "evaluated_at": 1760285660
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
  "sig": "2570b9add0a7fdcd78824c69aefb55f6b44a4627847229bbe2c3045d6cb6a577"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 28233398, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}