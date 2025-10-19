```json
{
  "id": "8eb02382dedc4839",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291663,
  "host_pid": "9e6742732c60:1",
  "hash": "b8f253150023e8e03396d6755637f9b48d80df3fcbd91eea9cf1314aab2f24b2",
  "cid": "QmV1b8f253150023e8e03396d6755637f9b48d80df3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291663,
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
      "evaluated_at": 1760291663
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
  "sig": "feb73c32496569384d200554dafe0dffb691b4147195d09bb482f6db81501193"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 671070000820328
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 256, 'threshold': 50, 'total_amount': 57315840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 255, 'first_seen': 1760284979, 'matching_hash': '6a7cc3d9f67da590'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '671070002', 'validation_error': 'Invalid routing number checksum'}}}