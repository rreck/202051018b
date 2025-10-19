```json
{
  "id": "cdf52bf801fe4c86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290545,
  "host_pid": "9e6742732c60:1",
  "hash": "d1407b5e3c291b5520d108f4bd8fbb72869e333f1b46e67778bc73d3257f54b8",
  "cid": "QmV1d1407b5e3c291b5520d108f4bd8fbb72869e333f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290545,
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
      "evaluated_at": 1760290545
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
  "sig": "120dcb97cb4c002a5fbca84993dc35004668488f03991865c1169147bf49cded"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 208726937303978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 50802426, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '49fe8226d43b3ae7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '208726934', 'validation_error': 'Invalid routing number checksum'}}}