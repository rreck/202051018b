```json
{
  "id": "453c26e2ded83a0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286100,
  "host_pid": "9e6742732c60:1",
  "hash": "770ce5ccea4229e48dcba2fc3d7e193ccac6d3cc1c8535ad75d7813a8a893ee6",
  "cid": "QmV1770ce5ccea4229e48dcba2fc3d7e193ccac6d3cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286100,
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
      "evaluated_at": 1760286100
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
  "sig": "55e5ab9b9ca92191a38ffceb51b826de31169229f0aeec7eceb7e9eef7b55b65"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100271167358
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285764, 'matching_hash': '04665d3443258f76'}}}