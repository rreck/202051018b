```json
{
  "id": "997d7abc6b253f54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289292,
  "host_pid": "9e6742732c60:1",
  "hash": "a11d2e376e195a8b5c3b6a78eb126e569c687e5de21256f14439a411e0ccb424",
  "cid": "QmV1a11d2e376e195a8b5c3b6a78eb126e569c687e5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289292,
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
      "evaluated_at": 1760289292
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
  "sig": "1aec917232794fd1181bad63b8fac435cecbd98e5286bcb3d7c6c41c1b86ec2e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 098545588857560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 16141041, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}