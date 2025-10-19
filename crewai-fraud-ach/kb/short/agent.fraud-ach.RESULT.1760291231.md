```json
{
  "id": "d826db3c55247e77",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291231,
  "host_pid": "9e6742732c60:1",
  "hash": "1cb81a871f0a8658d85781aba9e6c74b36f4cbd80629f5640b97405615859d62",
  "cid": "QmV11cb81a871f0a8658d85781aba9e6c74b36f4cbd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291231,
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
      "evaluated_at": 1760291231
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
  "sig": "b407ef6066265eb4f738135f021389eb1865c66174db15131225f03953a068eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155324238
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 80062690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285764, 'matching_hash': '6027d2fe89c09f43'}}}