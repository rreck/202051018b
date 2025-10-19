```json
{
  "id": "39cce21703d0e258",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292540,
  "host_pid": "9e6742732c60:1",
  "hash": "8960316d70b9b1c397fb1f923b415823d0bc2463eb222dcf2e3c7053e4a9d64d",
  "cid": "QmV18960316d70b9b1c397fb1f923b415823d0bc2463",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292540,
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
      "evaluated_at": 1760292540
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
  "sig": "c5e3160bf6eb8bef8a59e785683c53c123245c221989a25ea56f1bc93d5c1884"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594497049
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 40966200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'c5255ffe70702a12'}}}