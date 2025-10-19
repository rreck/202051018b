```json
{
  "id": "21e39af443e1fb41",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288525,
  "host_pid": "9e6742732c60:1",
  "hash": "41a5af31138364442c0824d094360c79f37b6798023d7c40bfaab575a7f94cf2",
  "cid": "QmV141a5af31138364442c0824d094360c79f37b6798",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288525,
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
      "evaluated_at": 1760288525
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
  "sig": "0d42c333bd17740b3ce5a6aa36ecb87610f22261c476f423ae7b874ad46c8570"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 24734688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}