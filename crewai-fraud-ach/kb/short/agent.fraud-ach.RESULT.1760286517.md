```json
{
  "id": "84ab1f04356039c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286517,
  "host_pid": "9e6742732c60:1",
  "hash": "b42ae5602dfc06d1e1b1dd053146c0752ea3de6b472c26c431da7f8b6c45eb01",
  "cid": "QmV1b42ae5602dfc06d1e1b1dd053146c0752ea3de6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286517,
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
      "evaluated_at": 1760286517
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
  "sig": "992516fee53c0b522a53c7e10cabed5afd0f4516b3f29033eb2e2a6cf6951c03"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034128514
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '342851cb36b9daae'}}}