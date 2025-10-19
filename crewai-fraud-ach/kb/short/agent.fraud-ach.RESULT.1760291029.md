```json
{
  "id": "d599ccab6cf19e2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291029,
  "host_pid": "9e6742732c60:1",
  "hash": "47ca2c1a5675e0193a3736d673178deb32bdb87a90ffc931e4b486e7bc2e28f3",
  "cid": "QmV147ca2c1a5675e0193a3736d673178deb32bdb87a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291029,
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
      "evaluated_at": 1760291029
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
  "sig": "ab5c13ef90598e67d58ee75f09bebd77f248707faa1fa871e6695094231d108f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 000042122595756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 95141016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}