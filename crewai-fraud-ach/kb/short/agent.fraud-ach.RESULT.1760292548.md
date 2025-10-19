```json
{
  "id": "60b8bc8f005b709a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292548,
  "host_pid": "9e6742732c60:1",
  "hash": "be65535cc32937bff641b6454dd9186a19dfb689a31f871500ece3e313450b34",
  "cid": "QmV1be65535cc32937bff641b6454dd9186a19dfb689",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292548,
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
      "evaluated_at": 1760292548
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
  "sig": "2c3af27136680b9d37e1827604be5db0682a2a9b4847d6403b5f9e3d0dd53895"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 542300578273472
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 49855600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': '6580c6d1de434ae0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '542300570', 'validation_error': 'Invalid routing number checksum'}}}