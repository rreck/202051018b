```json
{
  "id": "926c69f4f3b2642d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286132,
  "host_pid": "9e6742732c60:1",
  "hash": "8a757d1c2462ec285310ea794b345c1fa532bf0b058e8af5d932c5121b2b57e4",
  "cid": "QmV18a757d1c2462ec285310ea794b345c1fa532bf0b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286132,
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
      "evaluated_at": 1760286132
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
  "sig": "15b11e437cbb35c85c8404f159035ef8b9d1e490709aff4bf2b483e8dcfa5b2d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000035733360
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}