```json
{
  "id": "620f89eff11dafaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294413,
  "host_pid": "9e6742732c60:1",
  "hash": "42b8790b9c704b01b9a5af7b8d8603bcfe5746403d4f00d9d230eb04c19d5b33",
  "cid": "QmV142b8790b9c704b01b9a5af7b8d8603bcfe574640",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294413,
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
      "evaluated_at": 1760294413
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
  "sig": "2553a21421f9767ce6419a2ab83810175f94271b79f719d91df9916a2df69bfb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022605707
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 65367918, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '50e001b692c48bf8'}}}