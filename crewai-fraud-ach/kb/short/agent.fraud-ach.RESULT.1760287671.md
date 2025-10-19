```json
{
  "id": "dae5703c20a9cea4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287671,
  "host_pid": "9e6742732c60:1",
  "hash": "1fd8178a1eb23ca8fdf72fba915d2af631141a9e8faf328a136caa33bee9ad8f",
  "cid": "QmV11fd8178a1eb23ca8fdf72fba915d2af631141a9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287671,
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
      "evaluated_at": 1760287671
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
  "sig": "c9444f16689f67763e0711ac22b052efa52e0f8b98a53f53a988ef1e001d4cba"
}
```

Fraud detected: invalid_routing (score: 88)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 20475480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}