```json
{
  "id": "18dc5834aacc4343",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291827,
  "host_pid": "9e6742732c60:1",
  "hash": "41fba32cac8989fc64e15ee5813f0006e3c4f85a0036e74c1d136205a73fac48",
  "cid": "QmV141fba32cac8989fc64e15ee5813f0006e3c4f85a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291827,
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
      "evaluated_at": 1760291828
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
  "sig": "dda932d31f576c0835d7597a1b09bfe9c706fb5b338fcfbc4c71b0705136d2e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272276410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 32825968, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285764, 'matching_hash': '97f823784b1b19f6'}}}