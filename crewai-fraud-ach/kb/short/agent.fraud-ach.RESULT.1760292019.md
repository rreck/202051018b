```json
{
  "id": "e5576ca215de62f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292019,
  "host_pid": "9e6742732c60:1",
  "hash": "9c02570a1c427f55ef89900a8b4dd297d14419ec6410a5c08136813f91804b6e",
  "cid": "QmV19c02570a1c427f55ef89900a8b4dd297d14419ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292019,
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
      "evaluated_at": 1760292019
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
  "sig": "9eca5f29ad6260b9338abd8e660dc49064898b785c97089c8baa52f81638cc26"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 43001992, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'c5ade7cea17f41fa'}}}