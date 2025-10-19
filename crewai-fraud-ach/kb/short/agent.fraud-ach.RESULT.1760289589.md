```json
{
  "id": "0fbb111c922ba117",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289589,
  "host_pid": "9e6742732c60:1",
  "hash": "6afec0be5fab560576e8c63d768d900331ae92016a37b7b586aa920e10c15b0b",
  "cid": "QmV16afec0be5fab560576e8c63d768d900331ae9201",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289589,
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
      "evaluated_at": 1760289589
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
  "sig": "d1fe675ffbe52728f3d7654cc32886c15d174b1099adf1a2751cd2e70fbd5308"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 14070457, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}