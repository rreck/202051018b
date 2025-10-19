```json
{
  "id": "165f6cfa8ce44c2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291204,
  "host_pid": "9e6742732c60:1",
  "hash": "d831266f897010381a8a6c6976ce35fcc816d6a5b6b0ec731c6b6017274ecd59",
  "cid": "QmV1d831266f897010381a8a6c6976ce35fcc816d6a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291204,
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
      "evaluated_at": 1760291204
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
  "sig": "c19c94b31ac7a7bc9e5a7b947dfa256dd419f21c808ff9b43b619b609f97f735"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}