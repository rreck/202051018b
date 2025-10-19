```json
{
  "id": "d1196546fd85d9f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285916,
  "host_pid": "9e6742732c60:1",
  "hash": "32102fc3c51ef73b56a42cdd0eb9c6346eec12e8eccd234cd518649c36913555",
  "cid": "QmV132102fc3c51ef73b56a42cdd0eb9c6346eec12e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285916,
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
      "evaluated_at": 1760285916
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
  "sig": "d4954d7dc78aa7e214ee73e9688f02fc4f7250b87e6b7af249a01868c8761922"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243741176
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}