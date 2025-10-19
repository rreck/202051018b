```json
{
  "id": "a5375782e7e8968d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288232,
  "host_pid": "9e6742732c60:1",
  "hash": "8e9dbf2d8f2fa2c7624883f341c732b2f5a48a4087bf0f6e73baedf65f41c61c",
  "cid": "QmV18e9dbf2d8f2fa2c7624883f341c732b2f5a48a40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288232,
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
      "evaluated_at": 1760288232
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
  "sig": "2452eeb1a759c45fed8396e3ff95bc0ed589aa962bba330e961b255fc77e140f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 20249250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}