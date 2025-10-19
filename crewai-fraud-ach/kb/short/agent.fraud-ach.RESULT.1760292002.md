```json
{
  "id": "8f3209336c3878fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292002,
  "host_pid": "9e6742732c60:1",
  "hash": "462c42cca8c11bd07fd908fa36dd915b2958d020c49e603613fc157e1e59e1c3",
  "cid": "QmV1462c42cca8c11bd07fd908fa36dd915b2958d020",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292002,
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
      "evaluated_at": 1760292002
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
  "sig": "3c8b97877732f961f810acab41867c7bab430dafa0b35400b7950a7df059a14a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158076407
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 27926460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': 'bd01239b3993ff64'}}}