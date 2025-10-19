```json
{
  "id": "eb5c4e2a3f918529",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290446,
  "host_pid": "9e6742732c60:1",
  "hash": "8e843e3c9cc7c6c6a4229cf84d866901dd2c0b5b188cf5ba1ae9549a29e04626",
  "cid": "QmV18e843e3c9cc7c6c6a4229cf84d866901dd2c0b5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290446,
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
      "evaluated_at": 1760290446
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
  "sig": "8405e4b07701c567eb896a61cb91010e34f604c17e0f9ba0577cb41994b9f93a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 47737200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}