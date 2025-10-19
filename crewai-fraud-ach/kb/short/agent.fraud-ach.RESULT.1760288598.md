```json
{
  "id": "940425c1c436f9df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288598,
  "host_pid": "9e6742732c60:1",
  "hash": "11759b6960c1f749ff4dbbb6d0f2da5f59f58b8a8f98890f6bfdc49271e8a4a9",
  "cid": "QmV111759b6960c1f749ff4dbbb6d0f2da5f59f58b8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288598,
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
      "evaluated_at": 1760288598
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
  "sig": "313aede5ed6aafacd9a1dfe45e2279c6b01d738f29d6a4dcd664c81a62b35999"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241250323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': 'd18939bbbb7c2a14'}}}