```json
{
  "id": "3c5f6308606fe940",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290860,
  "host_pid": "9e6742732c60:1",
  "hash": "f800b5c2f29a7c0a06ddfd35f9f8aecd4f68bb77b385fa0ef010cb2843503c75",
  "cid": "QmV1f800b5c2f29a7c0a06ddfd35f9f8aecd4f68bb77",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290860,
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
      "evaluated_at": 1760290860
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
  "sig": "49699b827d5786f33dc7c9c812b292b14d53a9bac63e31902e36f33cd1881e98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028384993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 58841153, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': '07aae5a269425bd8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}