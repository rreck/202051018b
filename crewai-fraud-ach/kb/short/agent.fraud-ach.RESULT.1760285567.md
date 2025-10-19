```json
{
  "id": "1fdeac8910ebcf95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285567,
  "host_pid": "9e6742732c60:1",
  "hash": "c262e809b01ac16de0fdbd3e1493f5e32f4af91b92dccb59743339748394b4fd",
  "cid": "QmV1c262e809b01ac16de0fdbd3e1493f5e32f4af91b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285567,
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
      "evaluated_at": 1760285567
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
  "sig": "ba4a9828a5c584192b962aa7a4ab76aca842b19f55cc8cf926be06c1a06c640e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 24440852, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}