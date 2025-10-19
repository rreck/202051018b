```json
{
  "id": "ba2df111c4dc1425",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290433,
  "host_pid": "9e6742732c60:1",
  "hash": "dae3745a5bc3dbd62af891ffb7166bbd8795df684f1881e9cb03c6bec90b59f1",
  "cid": "QmV1dae3745a5bc3dbd62af891ffb7166bbd8795df68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290433,
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
      "evaluated_at": 1760290433
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
  "sig": "c39ed2e78e7a81a6c38862245b63d2d710e68984f5e01e66d8a91e804bed5d94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 17130450, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '253a69ee76b5426a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '612898023', 'validation_error': 'Invalid routing number checksum'}}}