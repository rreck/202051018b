```json
{
  "id": "8e223b7aeda33716",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287279,
  "host_pid": "9e6742732c60:1",
  "hash": "7928afdfdf68d37b345da0562e47e907c7ed44454ad77ac96af4cb21daa675f7",
  "cid": "QmV17928afdfdf68d37b345da0562e47e907c7ed4445",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287279,
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
      "evaluated_at": 1760287279
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
  "sig": "f09da8fb0cf006fc9719d8c4b870f1adf18a0ff79ce83dcfdee750dbf2a7c934"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 649338001689495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 17979408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285765, 'matching_hash': '47ca0a67ca137c75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649338005', 'validation_error': 'Invalid routing number checksum'}}}