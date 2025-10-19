```json
{
  "id": "2eb339cc5e150ecb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291871,
  "host_pid": "9e6742732c60:1",
  "hash": "0dac670826596da2a6ef661d429b47de8d4620c3e9d396acc7c13cc866eea1d6",
  "cid": "QmV10dac670826596da2a6ef661d429b47de8d4620c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291871,
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
      "evaluated_at": 1760291871
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
  "sig": "5f86066d02bd45420c992ad8b7c6bb10aca33e401ed4487eacd7a28e8523ea92"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 498752223480159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 72851705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '492624c5b9a9c8c0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}