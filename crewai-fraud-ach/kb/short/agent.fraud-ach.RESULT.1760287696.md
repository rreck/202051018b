```json
{
  "id": "03f61b8e12638a87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287696,
  "host_pid": "9e6742732c60:1",
  "hash": "de5019967ee24bb4eb4f17da36647cbc0010165118859e3eb9e72aba8119fc70",
  "cid": "QmV1de5019967ee24bb4eb4f17da36647cbc00101651",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287696,
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
      "evaluated_at": 1760287696
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
  "sig": "aca18a8bc4d5ee6d59e75c99a7a4d910959bba13eda451163e90529147ea6fcd"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 13779369, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}