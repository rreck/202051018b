```json
{
  "id": "0feb4814a8c0b208",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289027,
  "host_pid": "9e6742732c60:1",
  "hash": "085af551bc6b51dfb3fc4fd2292fa84c06a89e59b73c4c7e60fb7d333af0e16d",
  "cid": "QmV1085af551bc6b51dfb3fc4fd2292fa84c06a89e59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289027,
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
      "evaluated_at": 1760289027
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
  "sig": "cbf922a940a0ff16f7af898ae463ba8f837aef359dc013028aa02eecfc8033cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158219859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 47016159, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}