```json
{
  "id": "61bf170dec9bc7c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290856,
  "host_pid": "9e6742732c60:1",
  "hash": "c4f5f4a661243547f57cde749ccddf62ce4a75204874bc7d6248096555a2c5fa",
  "cid": "QmV1c4f5f4a661243547f57cde749ccddf62ce4a7520",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290856,
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
      "evaluated_at": 1760290856
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
  "sig": "c074a527635c8085229267f0fa3c69dab38e7cdc6922b2ebedd1f0a433fe1c28"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 824845893834283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 44761381, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': '751a36f41382ae06'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}