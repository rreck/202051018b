```json
{
  "id": "11e67772e2b3049e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289723,
  "host_pid": "9e6742732c60:1",
  "hash": "12f68edd0a36c34a86e5e15c38634691916adafce21e97ce65dbdaa66842862e",
  "cid": "QmV112f68edd0a36c34a86e5e15c38634691916adafc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289723,
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
      "evaluated_at": 1760289723
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
  "sig": "04e38835662ed95b2946b62d03c5aaefbd389e1b0d0c2a220c333090dc2d9d23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 19311234, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}