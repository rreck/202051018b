```json
{
  "id": "ffcc7d41a7e50baf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292505,
  "host_pid": "9e6742732c60:1",
  "hash": "6bf3029d6feb2082695ab132083f04cad6009468708a3c26c9352222a777efc4",
  "cid": "QmV16bf3029d6feb2082695ab132083f04cad6009468",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292505,
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
      "evaluated_at": 1760292505
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
  "sig": "9395302d631bff5a84b65b1c0d5281e77bfce843a234fe9e1c2e4a4094c6979f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022711139
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 85603432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '282a945486899803'}}}