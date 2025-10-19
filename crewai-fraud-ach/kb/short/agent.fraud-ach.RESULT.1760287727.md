```json
{
  "id": "d150cca832ea1aae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287727,
  "host_pid": "9e6742732c60:1",
  "hash": "ac4b8efaafeb11de165ae18bba81822d0e0046be8c2c1e2efe1fba786ac4ba12",
  "cid": "QmV1ac4b8efaafeb11de165ae18bba81822d0e0046be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287727,
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
      "evaluated_at": 1760287727
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
  "sig": "3f3f0274e1c4b8e82ac24c63d624795b7a1ef55e604efbdd9f0bcef400bda4eb"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 34935390, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}