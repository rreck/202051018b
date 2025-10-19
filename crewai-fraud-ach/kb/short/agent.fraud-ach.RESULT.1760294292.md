```json
{
  "id": "5a96fdb7e7624549",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294292,
  "host_pid": "9e6742732c60:1",
  "hash": "335127b34955f55f2894aa2574bfb37bf6a08ed5310d6d38209ddf6bf3218243",
  "cid": "QmV1335127b34955f55f2894aa2574bfb37bf6a08ed5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294292,
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
      "evaluated_at": 1760294292
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
  "sig": "7d820f79ab33f8a79759aba03d3d3c2c222a8f373dff5657683c681d5350adcc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023367694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 98557825, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '23afc27b7b9a7115'}}}