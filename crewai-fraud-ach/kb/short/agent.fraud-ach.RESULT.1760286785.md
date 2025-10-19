```json
{
  "id": "c504583fbe31f18c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286785,
  "host_pid": "9e6742732c60:1",
  "hash": "29d6d936277fc392818e7a9b7949f4b1d2d6b09cac3ede5b4689a80e1bccf842",
  "cid": "QmV129d6d936277fc392818e7a9b7949f4b1d2d6b09c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286785,
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
      "evaluated_at": 1760286785
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
  "sig": "42facc6c7e1573bae1a8e47b1e411e425b1bea8bd935ba3331d5f4ea8f5bf159"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598660548
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285763, 'matching_hash': '4ba6ddd8e6715c89'}}}