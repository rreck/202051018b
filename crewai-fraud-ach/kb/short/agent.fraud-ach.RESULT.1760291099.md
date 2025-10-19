```json
{
  "id": "5554767c7d87abef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291099,
  "host_pid": "9e6742732c60:1",
  "hash": "e4b6395341cb6dac5d825c7b5332ebd512f7b09be7341bd8aeebbc1af9117db7",
  "cid": "QmV1e4b6395341cb6dac5d825c7b5332ebd512f7b09b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291099,
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
      "evaluated_at": 1760291099
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
  "sig": "208fb1d34f06d56e71be4b9b0855913d04de87f6f8ad1144bcc53e8a842b46eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033621272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 24906714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'd5b1a20ced8a5769'}}}