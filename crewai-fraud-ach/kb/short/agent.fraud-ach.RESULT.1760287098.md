```json
{
  "id": "b4fffe5ccd053f02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287098,
  "host_pid": "9e6742732c60:1",
  "hash": "3a3cd22fa09f9a870707f1935ea7de5980b2c875f8f941360f16cb951f5097e8",
  "cid": "QmV13a3cd22fa09f9a870707f1935ea7de5980b2c875",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287098,
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
      "evaluated_at": 1760287098
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
  "sig": "c95e9c74afa117b5d4b5a30561a8f744323e55f183a0976374c726945c7d540e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100277495051
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 23372784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285763, 'matching_hash': 'b54d2b84a0558fd6'}}}