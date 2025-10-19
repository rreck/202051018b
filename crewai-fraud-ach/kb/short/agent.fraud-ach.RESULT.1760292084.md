```json
{
  "id": "e5274b520438e54b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292084,
  "host_pid": "9e6742732c60:1",
  "hash": "895d2af3045e4ee601a4bb8ca5a736b917307059b9462620697dd8a17ed4e5b4",
  "cid": "QmV1895d2af3045e4ee601a4bb8ca5a736b917307059",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292084,
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
      "evaluated_at": 1760292084
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
  "sig": "150c5e98b05c679325a39fef3b9dbdf47f7ad0690f5fb9c9f7748bd37928be60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244506997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 65743040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '00a59e186c59db13'}}}