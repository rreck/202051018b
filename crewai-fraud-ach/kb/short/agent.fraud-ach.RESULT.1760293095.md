```json
{
  "id": "511cb85e50155fb6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293095,
  "host_pid": "9e6742732c60:1",
  "hash": "26ca35ffbd657686688ddc643f125d4e58e3f0f9e98f92e620a5095adb4c2809",
  "cid": "QmV126ca35ffbd657686688ddc643f125d4e58e3f0f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293095,
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
      "evaluated_at": 1760293095
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
  "sig": "21dda939e36cadb7f31568468cc126e9bb659617879a1a38adc318d5aac86fe6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 45059683, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}