```json
{
  "id": "a34323cb0155ed2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289534,
  "host_pid": "9e6742732c60:1",
  "hash": "3bedbd8f89e890706ebc0e8c596e58b3b513e92e74344443e1a3f44ca4bf1f85",
  "cid": "QmV13bedbd8f89e890706ebc0e8c596e58b3b513e92e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289534,
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
      "evaluated_at": 1760289534
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
  "sig": "8fe7a61336d84153b2e4055721606b975e6764cb1713c192aa903d00af4390c2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 542300578273472
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 31409028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285764, 'matching_hash': '6580c6d1de434ae0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '542300570', 'validation_error': 'Invalid routing number checksum'}}}