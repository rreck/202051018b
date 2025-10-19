```json
{
  "id": "c8bc14be17c08859",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293217,
  "host_pid": "9e6742732c60:1",
  "hash": "7082dedf1ac78926b741d1c677b3ab11db3358282942a8ce3007c98b8664412b",
  "cid": "QmV17082dedf1ac78926b741d1c677b3ab11db335828",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293217,
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
      "evaluated_at": 1760293217
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
  "sig": "ba6c816fb88a2a9ee95be048dc777f951399b38a480c5d9eed4f74894faf06af"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244890024234480
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 82212808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'a93bcfd9fdd9d60c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244890022', 'validation_error': 'Invalid routing number checksum'}}}