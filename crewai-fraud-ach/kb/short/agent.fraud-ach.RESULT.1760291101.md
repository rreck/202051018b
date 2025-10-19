```json
{
  "id": "f9476d94eebf3cda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291101,
  "host_pid": "9e6742732c60:1",
  "hash": "b766973fbfd7726d401229f2f7bde3687b7f340f37e35545323b0ea0db384bce",
  "cid": "QmV1b766973fbfd7726d401229f2f7bde3687b7f340f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291101,
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
      "evaluated_at": 1760291101
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
  "sig": "1157aa62611b33fb45a543be1cf7e9187c13359dbb07d2ef52cac93382970af5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024843981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 24631164, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285764, 'matching_hash': 'a5434e6981d8724b'}}}