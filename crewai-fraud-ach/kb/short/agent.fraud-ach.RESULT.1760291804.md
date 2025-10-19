```json
{
  "id": "8dbde9620c6bb8cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291804,
  "host_pid": "9e6742732c60:1",
  "hash": "93bdb2b1578de3a6fd39616152d315e40f76ac0df8011b86ed11706428a2e318",
  "cid": "QmV193bdb2b1578de3a6fd39616152d315e40f76ac0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291804,
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
      "evaluated_at": 1760291804
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
  "sig": "310802fee5b4900c7cac2d14f077b132035bf4cff1c39c04b6d155e91038e139"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029236644
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 41686485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': 'c69cf0de1758a1d7'}}}