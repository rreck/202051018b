```json
{
  "id": "0863d31e5563b477",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286189,
  "host_pid": "9e6742732c60:1",
  "hash": "14aed5f1c131453d80e1451ad0b6a0800c08fddab5535a0205af144cee4c378d",
  "cid": "QmV114aed5f1c131453d80e1451ad0b6a0800c08fdda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286189,
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
      "evaluated_at": 1760286189
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
  "sig": "7924ef780969862f0f2ee73ec90d9de172b46a719aad9fc2aaf34b22560f3c4d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000246033311
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285764, 'matching_hash': 'd9b4b01f0add79d3'}}}