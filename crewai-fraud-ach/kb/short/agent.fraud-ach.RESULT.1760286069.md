```json
{
  "id": "c6646c250942831e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286069,
  "host_pid": "9e6742732c60:1",
  "hash": "88b5f73406ec4bba83ec016a22580cb73e75102f3772696d3691b3ef8cf1c7b9",
  "cid": "QmV188b5f73406ec4bba83ec016a22580cb73e75102f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286069,
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
      "evaluated_at": 1760286069
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
  "sig": "4a54d2e0dca7fe7f7fb791506ff95f05b16799974e5957a0233c9e123f1bc3a8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248125638
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}