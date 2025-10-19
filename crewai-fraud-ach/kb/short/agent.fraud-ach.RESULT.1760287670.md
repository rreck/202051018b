```json
{
  "id": "13871a0742328a79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287670,
  "host_pid": "9e6742732c60:1",
  "hash": "549e62c9d1513beb32e9b29bf18cf1e8293eef728408d90ca0189ec6d339c1b0",
  "cid": "QmV1549e62c9d1513beb32e9b29bf18cf1e8293eef72",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287670,
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
      "evaluated_at": 1760287670
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
  "sig": "5c0a1814163a3494b2c8aab3b133c47f419e56ec9e857a9f89a63975e0eef7ef"
}
```

Fraud detected: invalid_routing (score: 88)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 30161400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}