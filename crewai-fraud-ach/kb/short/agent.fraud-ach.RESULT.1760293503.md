```json
{
  "id": "21709e1d301ad7ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293503,
  "host_pid": "9e6742732c60:1",
  "hash": "556974a30d588486477835825c6b1c02d1c21165a8b21659ef6bf779af1ad326",
  "cid": "QmV1556974a30d588486477835825c6b1c02d1c21165",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293503,
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
      "evaluated_at": 1760293503
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
  "sig": "92db3e0a9e6c0094d39ae684c6d5c44d116e1541ae3002ff4f4b7cd59d806bb5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 93496700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}