```json
{
  "id": "5a0e00da6102d77f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292244,
  "host_pid": "9e6742732c60:1",
  "hash": "d2096597a1d1e78ac6da7a4279efb5b816335459b64b9ca3b3e2ecabe1ae1465",
  "cid": "QmV1d2096597a1d1e78ac6da7a4279efb5b816335459",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292244,
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
      "evaluated_at": 1760292244
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
  "sig": "dd950f5c3dba9a4583913acae3de2b5d114de64a6193cd64d78904aa3507aa45"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598290210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 12364931, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': '255d3759171e1aec'}}}