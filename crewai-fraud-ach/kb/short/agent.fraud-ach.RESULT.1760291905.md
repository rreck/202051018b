```json
{
  "id": "655e10b3c65c0ed3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291905,
  "host_pid": "9e6742732c60:1",
  "hash": "8f4be63f8a4f4f1570200a59930b67bd84a16b0c791255acc3e3c8a02462d30d",
  "cid": "QmV18f4be63f8a4f4f1570200a59930b67bd84a16b0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291905,
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
      "evaluated_at": 1760291905
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
  "sig": "124aaa65177b6fde700a07e8d16c3e61d806c47cf5875f821674324e24e721b6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 580123061332551
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 39163230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'b65f94a39c8828ce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}