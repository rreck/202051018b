```json
{
  "id": "c8fff8389ba124ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289083,
  "host_pid": "9e6742732c60:1",
  "hash": "226cb482f6fe2b6d503cd80dc7ceb5a4cd6630543a560a2d7fb4be06f5a8a03d",
  "cid": "QmV1226cb482f6fe2b6d503cd80dc7ceb5a4cd663054",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289083,
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
      "evaluated_at": 1760289083
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
  "sig": "ec02ea466f02989e2f372693d6a86f94049def9a5c9746c94bef0def3bc949da"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 085520768954692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 54874947, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}