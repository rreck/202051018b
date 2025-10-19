```json
{
  "id": "162d89b9edd537ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294699,
  "host_pid": "9e6742732c60:1",
  "hash": "2716cc56ff250d7588935e1b0c40a83016d955a844512490cc5b6b3426a32eae",
  "cid": "QmV12716cc56ff250d7588935e1b0c40a83016d955a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294699,
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
      "evaluated_at": 1760294699
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
  "sig": "18e3d316bdae92795aa20fc2846e910f501240b19a95b0ca2299cb8b21dc3e5a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 085520768954692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 118005417, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}