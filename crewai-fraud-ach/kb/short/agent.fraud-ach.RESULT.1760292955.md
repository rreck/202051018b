```json
{
  "id": "15c9b5b395381656",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292955,
  "host_pid": "9e6742732c60:1",
  "hash": "ed6b2ed208f1f2473d6fe6734c418214df3105d7561c0fd9f95137af25c24a7d",
  "cid": "QmV1ed6b2ed208f1f2473d6fe6734c418214df3105d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292955,
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
      "evaluated_at": 1760292955
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
  "sig": "40c49327fe904c1c213ccea412bcf7e08e709b81dfdb64898e3b8c20cca4e1bd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 699349871536240
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 77734800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '372ab63252fc0966'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '699349873', 'validation_error': 'Invalid routing number checksum'}}}