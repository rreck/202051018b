```json
{
  "id": "47ada5312ae2b575",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287273,
  "host_pid": "9e6742732c60:1",
  "hash": "5c61e800d96ba972d858e241f54ddeb1b0c9753cf0e9b623d3c09500f0bda075",
  "cid": "QmV15c61e800d96ba972d858e241f54ddeb1b0c9753c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287273,
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
      "evaluated_at": 1760287273
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
  "sig": "e6695d41cd5d7f166d35d01b61c67f6496b334b2c1dfd667b6983e6256aba7f8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 18344232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}