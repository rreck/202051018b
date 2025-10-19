```json
{
  "id": "64ad8de964d7d55e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293959,
  "host_pid": "9e6742732c60:1",
  "hash": "6fe6879e44d811ce284b08c610328248a93591ef6ab451fe31347ccd33f5e65d",
  "cid": "QmV16fe6879e44d811ce284b08c610328248a93591ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293959,
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
      "evaluated_at": 1760293959
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
  "sig": "2b4e419fa9a62bfb3be16c5e6c67ce21f38b49510d8e8b2d2f7d345ea2c7e944"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243028505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 23613106, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '47e30fe250bb416c'}}}