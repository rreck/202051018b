```json
{
  "id": "ccb789d28d84ae03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287304,
  "host_pid": "9e6742732c60:1",
  "hash": "b3a5f633bb5f091a2bb7917e8538127d490085d4a3631bcb9dd5fa20ae7e897b",
  "cid": "QmV1b3a5f633bb5f091a2bb7917e8538127d490085d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287304,
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
      "evaluated_at": 1760287304
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
  "sig": "9da18695bcf5534fb35ffa6b2ae50e4d2bcde5572c82e29cc920f1bbe889eb82"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201467876303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 24069870, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': 'ffdb832f59bf640d'}}}