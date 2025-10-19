```json
{
  "id": "a33f6d3eeeb963cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287899,
  "host_pid": "9e6742732c60:1",
  "hash": "1e9f9255262e6722b24b8874db894ac4d0b22eb60548f16f45368baecef75d3d",
  "cid": "QmV11e9f9255262e6722b24b8874db894ac4d0b22eb6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287899,
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
      "evaluated_at": 1760287899
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
  "sig": "c672d1d9250a101af1c4f2803a156c5714965d7039be099b2cd8c53565ddf7cb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 098545588857560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 10308564, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}