```json
{
  "id": "c2b3c8aab7a226b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292323,
  "host_pid": "9e6742732c60:1",
  "hash": "41896e81a4b6556eefca30c76a8bf6d512d81f76ea823679c9999ad2aaf3d3af",
  "cid": "QmV141896e81a4b6556eefca30c76a8bf6d512d81f76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292323,
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
      "evaluated_at": 1760292323
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
  "sig": "2280e3f8c8fdd69d1b4926672c0ee69cba545894df3d6c0e51710eb8a691813b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 051442861806700
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 83076825, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': '36501cb7899f5f80'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}