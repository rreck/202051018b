```json
{
  "id": "80ecae8bd66afa81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290910,
  "host_pid": "9e6742732c60:1",
  "hash": "29c46a723410e8aa8e6e42398bdc3fa10aa0e5021080c642567df9bb41990153",
  "cid": "QmV129c46a723410e8aa8e6e42398bdc3fa10aa0e502",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290910,
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
      "evaluated_at": 1760290910
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
  "sig": "0f194181fc321d3174fa6f616787cb675c3a4b5a16ccf02a9c3afd987564710d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 24925482, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}