```json
{
  "id": "df7f4f2eff1e6574",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290170,
  "host_pid": "9e6742732c60:1",
  "hash": "ee6e617aed117efdd1a1c1c83f0e3280b845498fa166a1933ef13e26f43fc704",
  "cid": "QmV1ee6e617aed117efdd1a1c1c83f0e3280b845498f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290170,
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
      "evaluated_at": 1760290170
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
  "sig": "e1fde782decbe107edfb5772158d4cf7206b372758b29f83b18fa51d3dddb6e0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 479377306721842
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 46709806, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285764, 'matching_hash': '9b6eff4280210a62'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '479377304', 'validation_error': 'Invalid routing number checksum'}}}