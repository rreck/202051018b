```json
{
  "id": "ea0494c9e0b241d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293192,
  "host_pid": "9e6742732c60:1",
  "hash": "9862bb52ab90141963bc6c9e581dc3f32ef72ceb0634461c1996add277f7643f",
  "cid": "QmV19862bb52ab90141963bc6c9e581dc3f32ef72ceb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293192,
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
      "evaluated_at": 1760293192
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
  "sig": "37cbcd7fd5b8aad440a900c31083a77e05b964a5d0d40008d3ac8ae81e5f24d7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 130120308000996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 52234842, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': 'd5206edc25c84cce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '130120307', 'validation_error': 'Invalid routing number checksum'}}}