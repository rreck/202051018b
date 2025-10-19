```json
{
  "id": "c6bd739e34529743",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286506,
  "host_pid": "9e6742732c60:1",
  "hash": "06d3f0d9aefd2c2b9ca0db0af08186eeea463d72fc1ae16a2cd58f8afac1573f",
  "cid": "QmV106d3f0d9aefd2c2b9ca0db0af08186eeea463d72",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286506,
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
      "evaluated_at": 1760286506
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
  "sig": "ad26b0a27421ca78c029f35384e5b5d87361b841fc55df8a664ecd3c375a4375"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 507153179781967
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': 'b9dbbc4d232307f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '507153176', 'validation_error': 'Invalid routing number checksum'}}}