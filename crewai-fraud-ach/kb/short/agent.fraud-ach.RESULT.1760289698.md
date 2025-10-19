```json
{
  "id": "63ede3773aede7e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289698,
  "host_pid": "9e6742732c60:1",
  "hash": "7f462961e4a13f727f4177cac56abd398c900e245b8e82c35324f6dcd03d5614",
  "cid": "QmV17f462961e4a13f727f4177cac56abd398c900e24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289698,
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
      "evaluated_at": 1760289698
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
  "sig": "49a291390c555b9c9dfa36ce32d8a54a60d53bbcd5d05c13530cdd68003267e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 41372240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}