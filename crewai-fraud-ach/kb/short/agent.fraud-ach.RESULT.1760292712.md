```json
{
  "id": "427e87806401417d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292712,
  "host_pid": "9e6742732c60:1",
  "hash": "7662a247d2ad5fb1309fde80854c212ffb8a21d65d70831038015b398414a699",
  "cid": "QmV17662a247d2ad5fb1309fde80854c212ffb8a21d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292712,
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
      "evaluated_at": 1760292712
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
  "sig": "183d730ef6ace8653e775f47e9196cf5451f633351407c685175d33b5c7707d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 79616600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}