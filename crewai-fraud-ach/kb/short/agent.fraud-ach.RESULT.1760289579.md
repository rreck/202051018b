```json
{
  "id": "6c9b800ce7c8f218",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289579,
  "host_pid": "9e6742732c60:1",
  "hash": "4696692328bf078722eadaab05521d8498def12193702f6c3debfbfc7588be97",
  "cid": "QmV14696692328bf078722eadaab05521d8498def121",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289579,
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
      "evaluated_at": 1760289579
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
  "sig": "a57ac0cc0ed193074d2e931df9b020f7c354fb5bdb8080fd3ab85097c60a3cbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034981344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 48234092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': '0030d58ae3a464b4'}}}