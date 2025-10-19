```json
{
  "id": "90908df027b5bbd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291444,
  "host_pid": "9e6742732c60:1",
  "hash": "3c0f4281d0dfcea96434b736e5a5e5f68d42fb13457a7c818688f5a42bbd8a1f",
  "cid": "QmV13c0f4281d0dfcea96434b736e5a5e5f68d42fb13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291444,
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
      "evaluated_at": 1760291444
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
  "sig": "de3eafab1ffe48b69292f17450d16595037b22955d26e91bef97340a1949f937"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596636125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 77924350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': 'de29ac64387e8e3f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '529024315', 'validation_error': 'Invalid routing number checksum'}}}