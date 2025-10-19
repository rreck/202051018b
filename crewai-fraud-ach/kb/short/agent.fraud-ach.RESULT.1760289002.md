```json
{
  "id": "182623605310cbee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289002,
  "host_pid": "9e6742732c60:1",
  "hash": "620c74f2dfd61ae1ddad4dbc9a7e61142541cb103617865f2742b3330a3492ae",
  "cid": "QmV1620c74f2dfd61ae1ddad4dbc9a7e61142541cb10",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289002,
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
      "evaluated_at": 1760289002
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
  "sig": "ab68c7332cfeb7fb9c10d6078d2ae69ec27c75240737f3e283ba2c494945be41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462224628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 25628900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': '4ca3be34af08dccb'}}}