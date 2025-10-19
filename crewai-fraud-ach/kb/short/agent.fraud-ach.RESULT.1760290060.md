```json
{
  "id": "8e363a0074e34f17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290060,
  "host_pid": "9e6742732c60:1",
  "hash": "a527b6c6e337893d2363f7dc8864111026bb8d0c9479d03210ffc2aee619eb53",
  "cid": "QmV1a527b6c6e337893d2363f7dc8864111026bb8d0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290060,
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
      "evaluated_at": 1760290060
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
  "sig": "f2b6196f3fbfbe35bf3382e1d9972cebf737922a6205a52e9bcb325bf8697074"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593801655
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 50232560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': '965a85028669bcfb'}}}