```json
{
  "id": "60a61d40e98704b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290702,
  "host_pid": "9e6742732c60:1",
  "hash": "ae8dbb1cddee6092b0cb4607a54420baec682b7545634dcceb50c85f79a20b7e",
  "cid": "QmV1ae8dbb1cddee6092b0cb4607a54420baec682b75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290702,
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
      "evaluated_at": 1760290702
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
  "sig": "86f7aead6c0299ffc7bbc9b6312d19814e7093a643b0c378aaf7b4d9153d76d6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594139699
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 72553625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '7ab15b33947f4722'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}