```json
{
  "id": "45cb5e5fa4f7f8ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293283,
  "host_pid": "9e6742732c60:1",
  "hash": "69de420e464c1acb6fdd66cff780606ff082540d938bcc7d18391812d330225f",
  "cid": "QmV169de420e464c1acb6fdd66cff780606ff082540d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293283,
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
      "evaluated_at": 1760293283
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
  "sig": "71745c6c641634e1cf980df7aab5c6c88ba862e46c4da6fd7dc977c5db4f49b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597785743
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 10750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': 'c11d2019f761950d'}}}