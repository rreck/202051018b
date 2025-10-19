```json
{
  "id": "31f4874aac80a629",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286375,
  "host_pid": "9e6742732c60:1",
  "hash": "80fa895846d4a96a685b2d8ee1693d4e28ae53d79d4035e38cadc408ce145e1a",
  "cid": "QmV180fa895846d4a96a685b2d8ee1693d4e28ae53d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286375,
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
      "evaluated_at": 1760286375
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
  "sig": "c6dedacf0041d374559533b8bfa304ac414cb3c435082d1f18df10263acabdba"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025001245
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}