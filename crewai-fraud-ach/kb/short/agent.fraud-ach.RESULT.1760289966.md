```json
{
  "id": "e0000f7d1b929e95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289966,
  "host_pid": "9e6742732c60:1",
  "hash": "594ae675f2c2d2c4d009c3f5c52f2178c74acfba0fdbb3a69df687dd4fdb1965",
  "cid": "QmV1594ae675f2c2d2c4d009c3f5c52f2178c74acfba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289966,
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
      "evaluated_at": 1760289966
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
  "sig": "d4fa7c6ea8f85013a9b039ee66a11d6d3e640bb888d1c5f8dc86f2e102ee4ad4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022338434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 62087856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': '4c9dfd860457308a'}}}