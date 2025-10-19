```json
{
  "id": "1ab8c6de2157e08d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293704,
  "host_pid": "9e6742732c60:1",
  "hash": "daf5ade2d00ca08eab4426b91847d383bcdef51a126c0cf9a728dfb6bc475bd6",
  "cid": "QmV1daf5ade2d00ca08eab4426b91847d383bcdef51a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293704,
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
      "evaluated_at": 1760293704
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
  "sig": "3967fee9f717d9662f3a93fed097f81b85bcd14c00975c7040fa27321250548e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244096993316032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 58209536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'b69a4a680810c6df'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}