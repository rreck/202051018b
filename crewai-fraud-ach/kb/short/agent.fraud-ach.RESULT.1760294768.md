```json
{
  "id": "a6b875801b264b38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294768,
  "host_pid": "9e6742732c60:1",
  "hash": "4f83b5342e1f3ec348aee1e4b8ccff20991ef799c528d0dcab3bf08f0d935a57",
  "cid": "QmV14f83b5342e1f3ec348aee1e4b8ccff20991ef799",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294768,
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
      "evaluated_at": 1760294768
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
  "sig": "e89dafb83b3d10646a158b3913a114a1630c6ab535b92eccb7ab8fef7c873d2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248764263
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 88620312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}