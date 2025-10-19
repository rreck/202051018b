```json
{
  "id": "62e658ce80c89da7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289032,
  "host_pid": "9e6742732c60:1",
  "hash": "5e2ebba84eb71ac243b3e25d7ca4d0b2b32827582092a4d70b703c885f60288e",
  "cid": "QmV15e2ebba84eb71ac243b3e25d7ca4d0b2b3282758",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289032,
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
      "evaluated_at": 1760289032
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
  "sig": "9352fb353998b56560186e3c78ce11085e1cb06c8f15409f63b4858481fa1065"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 10522689, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}