```json
{
  "id": "ce10eff7764249aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291908,
  "host_pid": "9e6742732c60:1",
  "hash": "a66ccb724cf1b69f99245d002dfde867a60355a7bb18e07b69f316d8b21c4238",
  "cid": "QmV1a66ccb724cf1b69f99245d002dfde867a60355a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291908,
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
      "evaluated_at": 1760291908
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
  "sig": "08435290ea9046feb5b2428b3e2164a139a7e3ee5ce3d8490c560073c93d815c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027962561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}een': 1760285763, 'matching_hash': '521bb7eb391c7339'}}}