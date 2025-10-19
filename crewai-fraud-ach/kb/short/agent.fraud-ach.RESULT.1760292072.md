```json
{
  "id": "59f610c1d5ccb62b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292072,
  "host_pid": "9e6742732c60:1",
  "hash": "9afa4e20556b4a26bc5b92f18eafc4cc92eacd3d322675ac84e19ce2a968c7bc",
  "cid": "QmV19afa4e20556b4a26bc5b92f18eafc4cc92eacd3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292072,
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
      "evaluated_at": 1760292072
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
  "sig": "82a70c30b62ada4e986f9e70a607b242cc4177251d84693f0f28e477bd24a0b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 20939499, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}