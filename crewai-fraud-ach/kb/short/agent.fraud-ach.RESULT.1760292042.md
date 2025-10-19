```json
{
  "id": "5360c1598eab6845",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292042,
  "host_pid": "9e6742732c60:1",
  "hash": "04cfe72f004b9333b44a1209ec1f66514c7961bab1e18deb5e4fc6146b920ad9",
  "cid": "QmV104cfe72f004b9333b44a1209ec1f66514c7961ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292042,
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
      "evaluated_at": 1760292042
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
  "sig": "9661baf9b8856da0401db7b4aa8e9630ccba082081814ce70e4f10af714dedf7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 361190719534797
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 66066084, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '0d1ced523145a886'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '361190711', 'validation_error': 'Invalid routing number checksum'}}}