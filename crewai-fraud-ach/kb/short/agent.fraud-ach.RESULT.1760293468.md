```json
{
  "id": "478f087c77028d76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293468,
  "host_pid": "9e6742732c60:1",
  "hash": "69d99e13fd6f53a32347b59463e2ec0aa1172ed9f899b43415b14b6ddd71b416",
  "cid": "QmV169d99e13fd6f53a32347b59463e2ec0aa1172ed9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293468,
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
      "evaluated_at": 1760293468
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
  "sig": "d3caa12e15aceb70025e2d3bb768e5c7a0e10360455138c61e59271a5438e838"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 529024316192383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 55413789, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': 'dc6c8a77c50d9997'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '529024315', 'validation_error': 'Invalid routing number checksum'}}}