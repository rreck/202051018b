```json
{
  "id": "66b44b4c3165161a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290428,
  "host_pid": "9e6742732c60:1",
  "hash": "eb1990e62b3778b7d8aee9323597efea3c5729476e5f02eab52c7692577e51ac",
  "cid": "QmV1eb1990e62b3778b7d8aee9323597efea3c572947",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290428,
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
      "evaluated_at": 1760290428
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
  "sig": "0960038a46ddc5ad98cb7de4a1db5895607f8d93f50e9b7ae0c37888e669310a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 607486347609576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 65632650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '01e47067eb24b5e9'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}