```json
{
  "id": "7b6aff0ee4bda047",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292180,
  "host_pid": "9e6742732c60:1",
  "hash": "6412529d997c60f603259969a57a37cfa72a6558da5cb4f7c198c844d2362794",
  "cid": "QmV16412529d997c60f603259969a57a37cfa72a6558",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292180,
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
      "evaluated_at": 1760292180
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
  "sig": "5963c7b1abf007a4f392f7557071ecda164d8c9e3ab391b87e2385fb25185313"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039250274
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 21794880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'd24fc6d094fa29d9'}}}