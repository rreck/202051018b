```json
{
  "id": "2a477652c268e5c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288160,
  "host_pid": "9e6742732c60:1",
  "hash": "98d44c488b53b22ce4b2d1f8f9cf1403656c0d0b4b76f2bd123d8a7e3c8e1e42",
  "cid": "QmV198d44c488b53b22ce4b2d1f8f9cf1403656c0d0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288160,
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
      "evaluated_at": 1760288160
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
  "sig": "72e0c8dc0ef27e5ff6ba4552b8b6bf4bfa1ad7273727e71f663050703efa9c0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 26732832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}