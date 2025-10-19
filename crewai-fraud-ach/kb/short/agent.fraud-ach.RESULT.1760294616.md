```json
{
  "id": "0f39969fa102bc78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294616,
  "host_pid": "9e6742732c60:1",
  "hash": "771e7bca0c4d9b39a646cff4d92c4b43c43f0693cecb31510eedc062f5c5c216",
  "cid": "QmV1771e7bca0c4d9b39a646cff4d92c4b43c43f0693",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294616,
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
      "evaluated_at": 1760294616
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
  "sig": "ba0695512254aa198a741e6539d58defc16994943d91d00856b807ce0e1477b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240849779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 46547945, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}