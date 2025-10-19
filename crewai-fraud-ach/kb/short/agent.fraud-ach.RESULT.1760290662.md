```json
{
  "id": "051ab4bac39d6ad4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290662,
  "host_pid": "9e6742732c60:1",
  "hash": "d887cb150131fdba92217c022cace0dbc78e576ad1e5965c78b5f9a364fd78ed",
  "cid": "QmV1d887cb150131fdba92217c022cace0dbc78e576a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290662,
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
      "evaluated_at": 1760290662
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
  "sig": "ea6d5a7c40565b1c7e224957f5049d101017b13d51f0fd1275664ab1a3f44a05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026959997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 35432124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285764, 'matching_hash': '4bd6adbc5f3cfca3'}}}