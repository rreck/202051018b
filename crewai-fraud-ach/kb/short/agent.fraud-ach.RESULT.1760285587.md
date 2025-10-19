```json
{
  "id": "fb007e9c6d176b01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285587,
  "host_pid": "9e6742732c60:1",
  "hash": "5676781bd412e12bf791b559c8b3e9c08a344da9b6d5d5beb53be1e6f1824f0a",
  "cid": "QmV15676781bd412e12bf791b559c8b3e9c08a344da9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285587,
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
      "evaluated_at": 1760285587
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "ecb16e9b462ba3df58ab5fdac8b8b05db72b1df19a862d1fe5e83ade483afc9e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 25283640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}