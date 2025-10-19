```json
{
  "id": "84f7f21faaa03d3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287306,
  "host_pid": "9e6742732c60:1",
  "hash": "bfe83c77eca007fecda0d88817491ecb65078da48f2393797dc6d26a10544280",
  "cid": "QmV1bfe83c77eca007fecda0d88817491ecb65078da4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287306,
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
      "evaluated_at": 1760287306
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
  "sig": "189651f366822c83017e27cb9de8413c60633ecadafbbf28cb38e25996f52945"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000025339678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 22198770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '57e7473926bfe00b'}}}