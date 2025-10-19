```json
{
  "id": "03a715fad5a1df08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294144,
  "host_pid": "9e6742732c60:1",
  "hash": "65ee0a60f8a0fe8289aa9e3a9dff0c7af981a7272ad3d064848ecb5b406264a6",
  "cid": "QmV165ee0a60f8a0fe8289aa9e3a9dff0c7af981a727",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294144,
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
      "evaluated_at": 1760294144
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
  "sig": "c8b1011c41b7c07e035d96169a8bb14e0ca5f87daf0c245b0d73377d4c396ba2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 70389960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}