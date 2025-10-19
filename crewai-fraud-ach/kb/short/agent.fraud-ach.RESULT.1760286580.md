```json
{
  "id": "f2455abbb3918d8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286580,
  "host_pid": "9e6742732c60:1",
  "hash": "9d82aab17532f97c49eb69d466c669209c06b047c8722c360141c02d81cf0da7",
  "cid": "QmV19d82aab17532f97c49eb69d466c669209c06b047",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286580,
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
      "evaluated_at": 1760286580
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
  "sig": "5d122ebdecd0dde8029e4eb5a9a29c8c7c0c1e6b63429c46284d8c9de63532e4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000022243585
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285764, 'matching_hash': '763c66b493018133'}}}