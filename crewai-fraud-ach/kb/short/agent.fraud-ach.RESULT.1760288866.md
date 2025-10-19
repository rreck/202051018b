```json
{
  "id": "ab9fe509d20db944",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288866,
  "host_pid": "9e6742732c60:1",
  "hash": "2833e326de4c058652e704829fb77b5e496c12c88f9e984c90bb277a1997faf6",
  "cid": "QmV12833e326de4c058652e704829fb77b5e496c12c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288866,
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
      "evaluated_at": 1760288866
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
  "sig": "6e0694ad91201b79426176143e4fe8bb4e3d80ea1c41e1987e31b677f9c09ac1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026828395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285765, 'matching_hash': '40ce51f53058bb71'}}}