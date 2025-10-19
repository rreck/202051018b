```json
{
  "id": "ebd1d81ba988e986",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292967,
  "host_pid": "9e6742732c60:1",
  "hash": "b7eb9b40fa13ca93ee1351ea011c2cbb0abfdea9bfdc4c2ad5e6d616d6a6ac14",
  "cid": "QmV1b7eb9b40fa13ca93ee1351ea011c2cbb0abfdea9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292967,
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
      "evaluated_at": 1760292967
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "3710de29b97f7ca1d3878dc12e63553a2025b6087fdf1b2efae3b35741b4e198"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 561028999821965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 29257701, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '09f745cfd1242827'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}