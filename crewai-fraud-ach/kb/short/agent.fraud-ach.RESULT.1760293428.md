```json
{
  "id": "97e919cbe61a6734",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293428,
  "host_pid": "9e6742732c60:1",
  "hash": "c7dc9597afdad0fcb231d82577a62885928c7994da39a49be6baaeb2f88d70e6",
  "cid": "QmV1c7dc9597afdad0fcb231d82577a62885928c7994",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293428,
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
      "evaluated_at": 1760293428
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
  "sig": "02021e295020556e6af8f5c2f774a4d825491229c191898c068c2fb2202efb01"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 906924177607497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 56242038, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}