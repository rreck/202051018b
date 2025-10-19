```json
{
  "id": "a95172ea8b98857e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290859,
  "host_pid": "9e6742732c60:1",
  "hash": "d15950a6c869e32dc48f3954c3cbb8fa5cb50466896f301e282893cd1b54809c",
  "cid": "QmV1d15950a6c869e32dc48f3954c3cbb8fa5cb50466",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290859,
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
      "evaluated_at": 1760290859
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
  "sig": "0d45e0efe6492feb8325e4c272cbd9220e0fd0f9ee77a7b1b3ee1e0819d1cef1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467071616
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 72408784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': 'cbd6f8586f75cfb9'}}}