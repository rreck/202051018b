```json
{
  "id": "cf7c467a308549b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285258,
  "host_pid": "9e6742732c60:1",
  "hash": "08394e1071b0a933fc8f50b38a1e814d14fd2ee3e5730fa2965dfe7123635a43",
  "cid": "QmV108394e1071b0a933fc8f50b38a1e814d14fd2ee3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285258,
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
      "evaluated_at": 1760285258
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2422c7d194f02d0ed344233c0d2488d3f7f7dbc40c82d8c4936803fee2fe2e21"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105154969717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11161864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760284979, 'matching_hash': '5065063b494c04f4'}}}