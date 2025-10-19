```json
{
  "id": "37e794baa73da2f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287355,
  "host_pid": "9e6742732c60:1",
  "hash": "bfd7dede37d59c1772652298bb89d03201a35b9db253405b8cca6050c50ad436",
  "cid": "QmV1bfd7dede37d59c1772652298bb89d03201a35b9d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287355,
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
      "evaluated_at": 1760287355
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
  "sig": "a3181514e03bee408e4c052be742e64c9f6192282bf4e2c19b5619b27f347864"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 11382957, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}