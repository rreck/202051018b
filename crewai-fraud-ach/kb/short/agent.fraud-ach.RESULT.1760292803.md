```json
{
  "id": "8630e8505cac1d9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292803,
  "host_pid": "9e6742732c60:1",
  "hash": "38c861cd020fc20fc8b0bb10c4d8705bab04a41e15c6028c2d55991590cc53dd",
  "cid": "QmV138c861cd020fc20fc8b0bb10c4d8705bab04a41e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292803,
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
      "evaluated_at": 1760292803
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
  "sig": "a6747ff463f57cc8aacf13234f854bb2910035d1d233e9832b24c5d9ca98ca37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469922578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 25156575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}