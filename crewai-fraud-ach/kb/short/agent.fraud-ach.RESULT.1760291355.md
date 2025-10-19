```json
{
  "id": "7679fb0ab49cdf67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291355,
  "host_pid": "9e6742732c60:1",
  "hash": "46b536d547964307881f85c28143474100867b0bbfd3ea34000c42502eb6d767",
  "cid": "QmV146b536d547964307881f85c28143474100867b0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291355,
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
      "evaluated_at": 1760291355
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
  "sig": "c74948a2d1f6755126276e56136ad74ad06f7f664cd41933a81045dae0c64e45"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 614505621863127
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 48025146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285764, 'matching_hash': '8748c624c8dfcb5e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}