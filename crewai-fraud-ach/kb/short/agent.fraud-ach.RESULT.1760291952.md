```json
{
  "id": "50416055c1a915a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291952,
  "host_pid": "9e6742732c60:1",
  "hash": "946dd8be6570eeb458bf8e5462c4dfd1c504b4cc752f1b45f3a00ce14ffb2d3b",
  "cid": "QmV1946dd8be6570eeb458bf8e5462c4dfd1c504b4cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291952,
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
      "evaluated_at": 1760291953
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
  "sig": "14cd646f5b7fc07dbfb1e8ec3d351f545730f4f7cbaa85feccdaecd69151a379"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 568426902254568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 72169284, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '885fc97ad7583ad3'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '568426909', 'validation_error': 'Invalid routing number checksum'}}}