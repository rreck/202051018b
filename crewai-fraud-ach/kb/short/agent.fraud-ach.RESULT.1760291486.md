```json
{
  "id": "e5ec228591a38f56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291486,
  "host_pid": "9e6742732c60:1",
  "hash": "4f31f0528e2f21f1419d1551120f4fb6008dc505549ce8134d591718adf96dc9",
  "cid": "QmV14f31f0528e2f21f1419d1551120f4fb6008dc505",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291486,
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
      "evaluated_at": 1760291486
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
  "sig": "4b533dd98af42db9fed89958503645053063d6c9a73b8753b4feb8a00e925fa7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 607486347609576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 77008976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '01e47067eb24b5e9'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}