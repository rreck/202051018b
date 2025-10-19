```json
{
  "id": "b88e684ad0a39ed3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290320,
  "host_pid": "9e6742732c60:1",
  "hash": "645e63daaf3a4c82d395dd7f9da9af68ac69fd00d27721320acf95d4fc0f6322",
  "cid": "QmV1645e63daaf3a4c82d395dd7f9da9af68ac69fd00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290320,
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
      "evaluated_at": 1760290320
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
  "sig": "478dc2bde3c4e7930b541bade0c92a624843948d7eaac205b1105d36e40b9df2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 033505362547520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 34913823, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '3154a67bf8f8af44'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}