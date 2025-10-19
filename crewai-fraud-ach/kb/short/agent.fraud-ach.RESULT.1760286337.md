```json
{
  "id": "e51e201de774705f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286337,
  "host_pid": "9e6742732c60:1",
  "hash": "4660714be1430baa3fa1c1e7fa4186367f1e9aa0d07bb3cb01eaf91589356402",
  "cid": "QmV14660714be1430baa3fa1c1e7fa4186367f1e9aa0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286337,
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
      "evaluated_at": 1760286337
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
  "sig": "68f70d069e9fdfd10caeb3d978bede6f2f45df0c82eb765c4857722b3a8fd16d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 20977978, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}