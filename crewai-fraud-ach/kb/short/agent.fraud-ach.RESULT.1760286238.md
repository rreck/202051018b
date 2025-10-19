```json
{
  "id": "d7e7c24d7ff331b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286238,
  "host_pid": "9e6742732c60:1",
  "hash": "fdf82fe512e726f6b327c0317f4a9e9045fbc7ff1722f9d670c20bd441a193d7",
  "cid": "QmV1fdf82fe512e726f6b327c0317f4a9e9045fbc7ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286238,
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
      "evaluated_at": 1760286238
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
  "sig": "919d2994dac6efa1237e6d643af5d4a8c02b061b8ae84e9aa5e0c2f3bcdc1552"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000027741847
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': '4cdb4cc94f6cfd73'}}}