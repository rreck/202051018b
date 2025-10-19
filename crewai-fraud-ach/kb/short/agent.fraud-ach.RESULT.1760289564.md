```json
{
  "id": "3c4e30261696feb9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289564,
  "host_pid": "9e6742732c60:1",
  "hash": "18546594c0ba447e82034d82281d053bde2604de69ac12f1d697b4e6b3596532",
  "cid": "QmV118546594c0ba447e82034d82281d053bde2604de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289564,
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
      "evaluated_at": 1760289564
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
  "sig": "ce1c3826aaa635de06918a52509590461f2a975099af11479d00c836d60a6aed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024315039
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': '88c1ddc0062d7899'}}}een': 1760285763, 'matching_hash': '40dace0dcec07d54'}}}