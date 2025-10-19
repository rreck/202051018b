```json
{
  "id": "0e133519c33a04b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289799,
  "host_pid": "9e6742732c60:1",
  "hash": "8def1b18870a99dd0583d011b98de5f96785be294e38145a85db01cf4f36f5c2",
  "cid": "QmV18def1b18870a99dd0583d011b98de5f96785be29",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289799,
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
      "evaluated_at": 1760289799
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
  "sig": "2617beff98e206e984b5587c99a0f81ad039ea8830571bc155b05f8395b6871f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152206156
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 32696454, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285764, 'matching_hash': '90dfebdd1b129ec8'}}}