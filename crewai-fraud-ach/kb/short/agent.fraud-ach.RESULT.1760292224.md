```json
{
  "id": "9ce00458ab38d375",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292224,
  "host_pid": "9e6742732c60:1",
  "hash": "378ad58ee682e8ab9bd3403cf4a1179a2546883c467687fdec7d746274d13443",
  "cid": "QmV1378ad58ee682e8ab9bd3403cf4a1179a2546883c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292224,
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
      "evaluated_at": 1760292225
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
  "sig": "c7ec1739a2d277a97be9c5d93055066e9399cf2e882e30ca4a400a8d27992e74"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 013419647478508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 48888444, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': 'f6be81dddddc1883'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}