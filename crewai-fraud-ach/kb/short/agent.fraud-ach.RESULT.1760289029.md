```json
{
  "id": "fa3b7556453cc4ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289029,
  "host_pid": "9e6742732c60:1",
  "hash": "845ab83548673eff2a999f6fb8b77f4ba87516a631bd0a4a0cda47d95220b72f",
  "cid": "QmV1845ab83548673eff2a999f6fb8b77f4ba87516a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289029,
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
      "evaluated_at": 1760289029
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
  "sig": "06dc9d96c5d04e1f9eb5e28d19e98d629dcbeaced4f576aa003f1f434ac7dd86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 55397547, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}