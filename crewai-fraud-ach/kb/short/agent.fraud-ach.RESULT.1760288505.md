```json
{
  "id": "9079fac816d00080",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288505,
  "host_pid": "9e6742732c60:1",
  "hash": "2025dbc68504d69b7d8477f3f7e24f8965fde43b2b8dca44fc5785fe1d518e8a",
  "cid": "QmV12025dbc68504d69b7d8477f3f7e24f8965fde43b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288505,
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
      "evaluated_at": 1760288505
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
  "sig": "f8f8d44991c89b0846cdbb14fc18ef9b35cac880e0e131b69533f8baf89e7a57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020716291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 17962790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': 'a2f2d41c7f22f612'}}}