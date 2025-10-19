```json
{
  "id": "7ce3b51cb5fa7891",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286738,
  "host_pid": "9e6742732c60:1",
  "hash": "3e66805bb3a2813a420996575bc79a4cc5427ba30919bd21f961a67e240383a9",
  "cid": "QmV13e66805bb3a2813a420996575bc79a4cc5427ba3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286738,
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
      "evaluated_at": 1760286738
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
  "sig": "7472cc1e1193b8ba1e105e7120c5c957d94582e22b069c7a8146fa1eb9aa1654"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15844465, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}