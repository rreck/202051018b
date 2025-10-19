```json
{
  "id": "75ec0c40b11221e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289287,
  "host_pid": "9e6742732c60:1",
  "hash": "84fa4afdd7eca6ac39710854e1efee938b985b88bae670b3da5ae9f2c0fcbe17",
  "cid": "QmV184fa4afdd7eca6ac39710854e1efee938b985b88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289287,
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
      "evaluated_at": 1760289287
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
  "sig": "5b02ff022a0104c40b2f6ec23848771dfbb97bd97813e16d108033055b1c031a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 361190719534797
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 41597164, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': '0d1ced523145a886'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '361190711', 'validation_error': 'Invalid routing number checksum'}}}