```json
{
  "id": "5072a31b141d4815",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292871,
  "host_pid": "9e6742732c60:1",
  "hash": "00d39f44e33d651fdf161982130e224ba87e53c41891c3cdb4b3fbed7bfa3023",
  "cid": "QmV100d39f44e33d651fdf161982130e224ba87e53c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292871,
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
      "evaluated_at": 1760292871
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
  "sig": "ae11c4a67085156c9a5ca5afd9941f8e240018ef546a66282af35f3b2e51d1a2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 580123061332551
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 43584885, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'b65f94a39c8828ce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}