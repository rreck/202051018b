```json
{
  "id": "11ca97a745b93985",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286243,
  "host_pid": "9e6742732c60:1",
  "hash": "67e582d8ec0d506c8e819295bcc36b240f972da43e66fda1419ed62167c6fda6",
  "cid": "QmV167e582d8ec0d506c8e819295bcc36b240f972da4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286243,
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
      "evaluated_at": 1760286243
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
  "sig": "65fa5dc7df4633eaa8aaa2009728a48ffc7a9d351a97c3716fe7e5ae582253df"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000021173532
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': 'a0cc7134a86fdd26'}}}