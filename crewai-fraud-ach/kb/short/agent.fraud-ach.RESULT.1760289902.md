```json
{
  "id": "869b8ef992a1fee7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289902,
  "host_pid": "9e6742732c60:1",
  "hash": "8d62eafbc5a7b1b2ef4844e468bb5e6886c4fea3ff948d2211a98bde7fd60238",
  "cid": "QmV18d62eafbc5a7b1b2ef4844e468bb5e6886c4fea3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289902,
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
      "evaluated_at": 1760289902
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
  "sig": "3952f683561d757ccb1a3c2e3bb0fd3aa3f08b92eb56e7ab84effa2e11b498b4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248019681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 62556192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'd399d5f74d941af5'}}}