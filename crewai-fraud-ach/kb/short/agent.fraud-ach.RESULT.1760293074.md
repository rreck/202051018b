```json
{
  "id": "2dabccf44d1ed7c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293074,
  "host_pid": "9e6742732c60:1",
  "hash": "01e078c7bdf344ca5b9e4abd6440f7f23cda07f70453eafe862e9fce581eaec9",
  "cid": "QmV101e078c7bdf344ca5b9e4abd6440f7f23cda07f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293074,
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
      "evaluated_at": 1760293074
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
  "sig": "c972a61e7cb715164c4f19f0fef2559f2b1deaf7fb6229685cf8098eecedd030"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 020899457068496
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 83221143, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': '41b228ccdaf61559'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}