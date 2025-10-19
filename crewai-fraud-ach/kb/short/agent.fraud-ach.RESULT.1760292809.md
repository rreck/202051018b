```json
{
  "id": "c03c0120679a8400",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292809,
  "host_pid": "9e6742732c60:1",
  "hash": "c16f24721b4069b99ff463ab04cb5277bb4819b1fd85f6c28adc0dd2b0727c13",
  "cid": "QmV1c16f24721b4069b99ff463ab04cb5277bb4819b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292809,
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
      "evaluated_at": 1760292809
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
  "sig": "ff2971967a19605dce90f4352e305a7e9b1d2445cca891a662bc5ad18d662485"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 18155620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}