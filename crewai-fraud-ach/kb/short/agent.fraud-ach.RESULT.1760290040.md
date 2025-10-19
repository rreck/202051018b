```json
{
  "id": "03179b0642727a0a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290040,
  "host_pid": "9e6742732c60:1",
  "hash": "029726924ddbc13f82e8210522caca9987082fac617e19bd59cc219434ef3045",
  "cid": "QmV1029726924ddbc13f82e8210522caca9987082fac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290040,
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
      "evaluated_at": 1760290040
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
  "sig": "ecaed14e9fe6b4bb8e6c1982a5c5d355c98fdea206f8d681aedb249225ad663e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027005922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 40122320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '8fe7ed8865cd9a2a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}