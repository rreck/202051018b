```json
{
  "id": "505a60b6ae95cf29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293809,
  "host_pid": "9e6742732c60:1",
  "hash": "20e065476c79d9e8e24afe394e4d68046ecfa733915f5de35ca6558ffbecd837",
  "cid": "QmV120e065476c79d9e8e24afe394e4d68046ecfa733",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293809,
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
      "evaluated_at": 1760293809
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
  "sig": "67b2ad5205c6fef696f763432da3a7266ca6ad01e14e3656319c77350cb0bbc3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241053391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 96837158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}