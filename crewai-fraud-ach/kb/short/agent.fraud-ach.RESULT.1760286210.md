```json
{
  "id": "8b7c50b7d6df7b01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286210,
  "host_pid": "9e6742732c60:1",
  "hash": "f60cf1b29d7bbeaa6dd1b3e40fb1c763d902c183be04bfbc976b34cc77914a11",
  "cid": "QmV1f60cf1b29d7bbeaa6dd1b3e40fb1c763d902c183",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286210,
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
      "evaluated_at": 1760286210
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
  "sig": "a9739dc1e52eccd766dc706123df392b71b40cefecf3a6f1e571b68b9aca7ec7"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000020947870
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '1f43c37f0aae1875'}}}