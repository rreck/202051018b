```json
{
  "id": "957fe90aefc9dea5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294111,
  "host_pid": "9e6742732c60:1",
  "hash": "697de064ed1d4b78d2aa31f7b9a4ab254c74b5c248ff55322e4d5d5273404799",
  "cid": "QmV1697de064ed1d4b78d2aa31f7b9a4ab254c74b5c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294111,
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
      "evaluated_at": 1760294111
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
  "sig": "05a1dd7fbad63157cb2ac053e914797cc070c33823a8a171586189e296a0ac02"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467386779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 58000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'cfffbd2ec30a8ce4'}}}