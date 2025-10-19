```json
{
  "id": "fe624d159b6a999d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293042,
  "host_pid": "9e6742732c60:1",
  "hash": "62159e1733f6f395e93cdf9533036b3fdfc1023b28f311dbfc0729bdbfbe504e",
  "cid": "QmV162159e1733f6f395e93cdf9533036b3fdfc1023b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293042,
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
      "evaluated_at": 1760293042
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
  "sig": "e0f411a5f121f9afcb8269837b94c91c12a78814203d38fa3317e24585481558"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 491975137325012
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 61885320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}