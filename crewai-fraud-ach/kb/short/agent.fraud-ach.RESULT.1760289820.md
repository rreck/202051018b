```json
{
  "id": "d2a8809d515f6cdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289820,
  "host_pid": "9e6742732c60:1",
  "hash": "fce8b89418e7af451800eae209289568d73c4528191fe7d25631ec911c4fed9e",
  "cid": "QmV1fce8b89418e7af451800eae209289568d73c4528",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289820,
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
      "evaluated_at": 1760289820
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
  "sig": "ab38ef0722e4a4bb2432a0fcffe5b5aa732ace5d197a2b014edd63aa42228360"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241647784
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 14731156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': '5747783cddc76b25'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}