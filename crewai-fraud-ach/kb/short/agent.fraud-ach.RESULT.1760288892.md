```json
{
  "id": "44113158d63b41a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288892,
  "host_pid": "9e6742732c60:1",
  "hash": "bb156a2fcdc45e71ca204902eb7937c7b2421c62f7a2516c60f852b3ffb4bee5",
  "cid": "QmV1bb156a2fcdc45e71ca204902eb7937c7b2421c62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288892,
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
      "evaluated_at": 1760288892
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
  "sig": "7e61a43c2f936044adf42a3da60e139dd1ff1164d4c6575e6ea6cc66adcf3926"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 12219721, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285765, 'matching_hash': '253a69ee76b5426a'}}}