```json
{
  "id": "832b93fcd9eeb840",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294811,
  "host_pid": "9e6742732c60:1",
  "hash": "8c2541146591afe2760528937488bd06bd2af0b6695eb11436d661155ad5d41b",
  "cid": "QmV18c2541146591afe2760528937488bd06bd2af0b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294811,
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
      "evaluated_at": 1760294811
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
  "sig": "fa9b1bc7ff5182dd540541f200ea453ff84bbb4fb014ba6743e4efd72e99e6bd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 041887157928370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 106565935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '40835df504bb3fdd'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}s': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6161479}}}}