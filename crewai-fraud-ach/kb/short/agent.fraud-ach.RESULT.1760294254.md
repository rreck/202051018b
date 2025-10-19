```json
{
  "id": "a975c3861df54997",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294254,
  "host_pid": "9e6742732c60:1",
  "hash": "6aa60d6a658640da9b9422834f6df955553a0531efa89e54e9060c99bcb36e59",
  "cid": "QmV16aa60d6a658640da9b9422834f6df955553a0531",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294254,
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
      "evaluated_at": 1760294254
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
  "sig": "413b400996ffbcba246d5f7d1a2b4036a025254074876bd2ca1c8c9f2fa5dbc2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 69657822, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}