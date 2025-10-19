```json
{
  "id": "b14bb0fd97103f47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289710,
  "host_pid": "9e6742732c60:1",
  "hash": "800593b5d6e6f4cab55df7cb176ba04bc6bbe836e5478d6974217bfca8a99030",
  "cid": "QmV1800593b5d6e6f4cab55df7cb176ba04bc6bbe836",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289710,
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
      "evaluated_at": 1760289710
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
  "sig": "0ee29527ae53348209a5e12c5eeb23676020930e99f885badd7c115a51cf4868"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 085520768954692
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 63616089, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '4f8cdcee5609bbf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}