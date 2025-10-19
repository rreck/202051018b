```json
{
  "id": "d1d94545aa409fc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290679,
  "host_pid": "9e6742732c60:1",
  "hash": "3757a83cb9ff1dc65526632910397456f649d24a45b838dec0ec432b26628eb7",
  "cid": "QmV13757a83cb9ff1dc65526632910397456f649d24a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290679,
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
      "evaluated_at": 1760290679
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
  "sig": "b972f2f329289b3b83f5d8da8d193d016455f14e3239736a40dee49f4625abf6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 76946532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}