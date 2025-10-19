```json
{
  "id": "c147904b95771a28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293221,
  "host_pid": "9e6742732c60:1",
  "hash": "0a1ce1028b6264166b5908a723d0280e9221ac498e753c5a69b3b9522ec1e487",
  "cid": "QmV10a1ce1028b6264166b5908a723d0280e9221ac49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293221,
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
      "evaluated_at": 1760293221
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
  "sig": "3b1f1da16126b42b66614cecb825ef8fc0e3b72e1bc6691f0ef6f2eb028b01c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591790243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 15029862, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '8c245acd6e70ddc0'}}}