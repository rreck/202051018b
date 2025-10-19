```json
{
  "id": "86efed8a8bee7015",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293624,
  "host_pid": "9e6742732c60:1",
  "hash": "ebe3e58088befa2d63134391d754ebb9b2c7c0ea26c4ef9c26e73351cbae2599",
  "cid": "QmV1ebe3e58088befa2d63134391d754ebb9b2c7c0ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293624,
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
      "evaluated_at": 1760293624
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
  "sig": "9207986c8359c5b77b881bfdc9afab07637e25ddd1d6d0b3858dd0a90ea75abc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461002751
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 74622192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}