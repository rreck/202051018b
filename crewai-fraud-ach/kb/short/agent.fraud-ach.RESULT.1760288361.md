```json
{
  "id": "b44d2a55895ae48f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288361,
  "host_pid": "9e6742732c60:1",
  "hash": "f004fbc6ffb7aee60a7b31fe1a08bca880f719268baef27cc70ce71c725531f2",
  "cid": "QmV1f004fbc6ffb7aee60a7b31fe1a08bca880f71926",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288361,
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
      "evaluated_at": 1760288361
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
  "sig": "f1f7f5c76606471345042d2ed08796ee64d5084968e0733835a373fc28ff08cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020641018
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 14715792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': '9cb08faa1a3d5c0e'}}}