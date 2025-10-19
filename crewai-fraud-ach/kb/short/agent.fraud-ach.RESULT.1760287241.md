```json
{
  "id": "91e2440f573e2e4e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287241,
  "host_pid": "9e6742732c60:1",
  "hash": "6527d1ba46e98482c58c89482a42e29e16efded4f3679101092021c890b195e9",
  "cid": "QmV16527d1ba46e98482c58c89482a42e29e16efded4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287241,
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
      "evaluated_at": 1760287241
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
  "sig": "037290c05d0dea3bda0ef0a7b40aa3d0b4db817ea69fa40fa78323b39d296cbd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 000042122595756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 50926104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}