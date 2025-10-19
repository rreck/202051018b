```json
{
  "id": "4ff67197bdc1c739",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288589,
  "host_pid": "9e6742732c60:1",
  "hash": "5982c980b2962a56f9da7f924311439135e5112786e80af56448212d63a340e4",
  "cid": "QmV15982c980b2962a56f9da7f924311439135e51127",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288589,
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
      "evaluated_at": 1760288589
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "c2dbffd5197d32c806957c9fcd795514aa997c7ebf64ae0ad446f5ffbbc8cbfb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245652457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '6ac12dd8f1799493'}}}5763, 'matching_hash': 'e24b6b5408d67f01'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}