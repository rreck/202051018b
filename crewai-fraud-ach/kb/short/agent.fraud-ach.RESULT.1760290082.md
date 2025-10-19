```json
{
  "id": "ecd7fa86fdd00b1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290082,
  "host_pid": "9e6742732c60:1",
  "hash": "b38b0399821f50ac69cf7bcb732c17a5ab47cc78654707dbf830ebae12425b6d",
  "cid": "QmV1b38b0399821f50ac69cf7bcb732c17a5ab47cc78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290082,
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
      "evaluated_at": 1760290082
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
  "sig": "95fe892f66d8943b9b60ac08817b4d3fa7add377ac1e56882e289e3514fd4960"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272276410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 25154682, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285764, 'matching_hash': '97f823784b1b19f6'}}}