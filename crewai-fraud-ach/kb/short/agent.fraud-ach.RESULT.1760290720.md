```json
{
  "id": "3f3154328b9e2a29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290720,
  "host_pid": "9e6742732c60:1",
  "hash": "7b5715bf8cc8796d593f710b0cf0276394486aaf4186a8ce4c710be58edd1677",
  "cid": "QmV17b5715bf8cc8796d593f710b0cf0276394486aaf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290720,
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
      "evaluated_at": 1760290720
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
  "sig": "4491e6c53018b86361955ec48853d82ab95c56df496045cc10a2fd63d40a709b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 49964936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}