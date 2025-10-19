```json
{
  "id": "efb638e24e80264b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293330,
  "host_pid": "9e6742732c60:1",
  "hash": "64290d7123b6a7bf0b8f1675eeee8b67f5de98a3efae0b4b4817baec7b8cde25",
  "cid": "QmV164290d7123b6a7bf0b8f1675eeee8b67f5de98a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293330,
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
      "evaluated_at": 1760293331
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
  "sig": "a1c212b1341b5b85b0bff5e2d922d37167f89edecb957529e2c798f83243463b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245928241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 73860336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '062a48cd408462a2'}}}