```json
{
  "id": "a2ad61783c8bbd80",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292254,
  "host_pid": "9e6742732c60:1",
  "hash": "c0b0968e84a7f1a05cb43042751521e8a2f40c82bf0ecd1e629f1acee4e52e8d",
  "cid": "QmV1c0b0968e84a7f1a05cb43042751521e8a2f40c82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292254,
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
      "evaluated_at": 1760292254
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
  "sig": "1d4c5d27706f612537e6fb46af1af840bb053a2f538c794902c73315d872d9c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 61421864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}