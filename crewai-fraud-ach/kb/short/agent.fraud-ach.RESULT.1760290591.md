```json
{
  "id": "bf4be2aad590a724",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290591,
  "host_pid": "9e6742732c60:1",
  "hash": "93ad3431701707c848765ec8a2f450367bd3563e73b9ce426df15c269a37d077",
  "cid": "QmV193ad3431701707c848765ec8a2f450367bd3563e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290591,
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
      "evaluated_at": 1760290591
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
  "sig": "ab2e54176593c0b50d2d244ce351c955e5db1349a3362c6c2651ea31f9286c3b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593870321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 12670350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'ac61827ecd1197f0'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}