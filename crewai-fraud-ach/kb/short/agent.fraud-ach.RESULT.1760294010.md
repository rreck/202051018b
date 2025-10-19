```json
{
  "id": "8939a2dea3bb95a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294010,
  "host_pid": "9e6742732c60:1",
  "hash": "a9f34aad2769f37c7f656eda0300a3a58d8425c33b3523c3ac1105a7a2c45a67",
  "cid": "QmV1a9f34aad2769f37c7f656eda0300a3a58d8425c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294010,
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
      "evaluated_at": 1760294010
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "37bcd9b0a4a2e0ebf4961e16a1c3029d8528926a3f43bbbd09d7d86201763301"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022025451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 107742350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '147c6cadc877e9f2'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}