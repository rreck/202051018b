```json
{
  "id": "0286d5d03096add3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287039,
  "host_pid": "9e6742732c60:1",
  "hash": "a6e6d4013c0bf4ac53307b8ab3f8c4faf98d3fa5ae5c068d43f18e2ecb263e62",
  "cid": "QmV1a6e6d4013c0bf4ac53307b8ab3f8c4faf98d3fa5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287039,
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
      "evaluated_at": 1760287039
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "b26c3a5d7c84b14760cf8e1ef2702e5226d13169b7d61984c7e01e2e7b1bb6a7"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000037688830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11754472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285764, 'matching_hash': 'a1e0090e71bf48f4'}}}