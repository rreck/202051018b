```json
{
  "id": "014b273fe53beb67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293432,
  "host_pid": "9e6742732c60:1",
  "hash": "ed119528f803e38c8b84354457d520db06921286c7b52a9ce3ac6529b46500d2",
  "cid": "QmV1ed119528f803e38c8b84354457d520db06921286",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293432,
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
      "evaluated_at": 1760293432
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
  "sig": "21f21ee52981690da40ab81133463ee89b9efe0a63342a3dccdc895e77fb05aa"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 51131246, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}