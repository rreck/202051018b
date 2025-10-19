```json
{
  "id": "467a8c9e5d6f0f24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288208,
  "host_pid": "9e6742732c60:1",
  "hash": "5289e3b967b9cd982daa5144ede7f7511a4b499c199170f3325c9065afca76f3",
  "cid": "QmV15289e3b967b9cd982daa5144ede7f7511a4b499c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288208,
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
      "evaluated_at": 1760288208
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
  "sig": "48a277ce3047d2044b8b0ae953002945c1ed1441fddbbb27f224390b11939563"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029384681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285764, 'matching_hash': '45a3ccbce684d395'}}}een': 1760285763, 'matching_hash': 'ac75b07ed83ae58c'}}}